"""
NPL Research Activity scraper  (v3 – full article body parsing)

Each list item  → fetch detail page → extract:
  - date        : .artclViewHead .right dl[dt=date] dd   (e.g. 2025.12.18)
  - title       : h2.artclViewTitle                      (e.g. [발표]FKPPN …)
  - category    : bracket tag at start of title          (e.g. 발표 / 수상 / …)
  - clean_title : title with the bracket tag removed     (e.g. FKPPN …)
  - author      : .artclViewHead .right dl[dt=author] dd
  - body_text   : .artclView  (plain text, may contain "Title: … (URL)")
  - paper_title : text before first URL in body
  - paper_url   : first http(s) URL in body

Output:
  news_data.json          – structured JSON
  _news/announcement_NNNN.md  – clean Jekyll inline announcements
"""

import json
import re
import time
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE      = "https://npl.pusan.ac.kr"
LIST_URL  = f"{BASE}/bbs/npl/13275/artclList.do"
HEADERS   = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
MAX_PAGES = 10
DELAY     = 0.5   # seconds between requests


# ── fetch helpers ───────────────────────────────────────────────────────────

def get(url: str) -> BeautifulSoup:
    r = requests.get(url, headers=HEADERS, verify=False, timeout=15)
    r.encoding = "utf-8"
    return BeautifulSoup(r.text, "html.parser")

def post(url: str, data: dict) -> BeautifulSoup:
    r = requests.post(url, headers=HEADERS, data=data, verify=False, timeout=15)
    r.encoding = "utf-8"
    return BeautifulSoup(r.text, "html.parser")


# ── date normalisation ───────────────────────────────────────────────────────

def normalise_date(raw: str) -> str:
    """Turn '2025.12.18' or '2025. 12. 17.' or '2025-12-17' → 'YYYY-MM-DD'."""
    m = re.search(r"(\d{4})[.\-]\s*(\d{1,2})[.\-]\s*(\d{1,2})", raw)
    if m:
        return f"{m.group(1)}-{m.group(2).zfill(2)}-{m.group(3).zfill(2)}"
    return ""


# ── collect article URLs from list pages ─────────────────────────────────────

def collect_article_urls(max_pages: int) -> list[str]:
    urls = []
    for page in range(1, max_pages + 1):
        soup = post(LIST_URL, {"page": str(page), "layout": "", "findType": "", "findWord": ""})
        for a in soup.select("ul.artclList > li a.artclLinkView"):
            href = a.get("href", "")
            if href:
                full = BASE + href if not href.startswith("http") else href
                if full not in urls:
                    urls.append(full)
        print(f"  Page {page:2d}: {len(soup.select('ul.artclList > li a.artclLinkView'))} links found")
        time.sleep(DELAY)
    return urls


# ── parse individual article page ────────────────────────────────────────────

def parse_article(url: str) -> dict:
    soup = get(url)
    result = {"url": url}

    # ── date from header ─────────────────────────────────────────────────────
    date_raw = ""
    for dt in soup.select(".artclViewHead .right dl dt"):
        if "date" in dt.get_text(strip=True).lower():
            dd = dt.find_next_sibling("dd")
            if dd:
                date_raw = dd.get_text(strip=True)
                break
    result["date"] = normalise_date(date_raw)

    # ── author ───────────────────────────────────────────────────────────────
    author = ""
    for dt in soup.select(".artclViewHead .right dl dt"):
        if "author" in dt.get_text(strip=True).lower():
            dd = dt.find_next_sibling("dd")
            if dd:
                author = dd.get_text(strip=True)
                break
    result["author"] = author

    # ── full title ───────────────────────────────────────────────────────────
    h2 = soup.select_one("h2.artclViewTitle")
    full_title = h2.get_text(strip=True) if h2 else ""
    result["full_title"] = full_title

    # ── category tag  [발표] / [수상] / … ────────────────────────────────────
    cat_m = re.match(r"^\[([^\]]+)\]", full_title)
    category   = cat_m.group(1) if cat_m else "공지"
    clean_title = full_title[cat_m.end():].strip() if cat_m else full_title
    result["category"]    = category
    result["clean_title"] = clean_title

    # ── date fallback: extract from title text if not found in header ─────────
    if not result["date"]:
        result["date"] = normalise_date(clean_title)

    # ── body text ─────────────────────────────────────────────────────────────
    body_div = soup.select_one(".artclView")
    body_raw  = body_div.get_text(" ", strip=True) if body_div else ""
    # collapse whitespace
    body_text = re.sub(r"\s+", " ", body_raw).strip()
    result["body_text"] = body_text

    # ── paper title & URL from body ───────────────────────────────────────────
    # Pattern:  "Title: Some text (https://...)"  or just "Title: https://..."
    paper_title = ""
    paper_url   = ""

    title_m = re.search(r"Title:\s*(.+?)(?:\s*\(https?://[^\)]+\)|\s*https?://\S+|$)", body_text)
    if title_m:
        paper_title = title_m.group(1).strip()

    url_m = re.search(r"https?://\S+", body_text)
    if url_m:
        paper_url = url_m.group(0).rstrip(")")   # remove stray closing paren

    result["paper_title"] = paper_title
    result["paper_url"]   = paper_url

    return result


# ── Jekyll announcement file writer ─────────────────────────────────────────

def _badge(category: str) -> str:
    colour = {
        "발표": "#1565c0",
        "수상": "#b71c1c",
        "과제선정": "#1b5e20",
        "출판": "#4a148c",
    }.get(category, "#37474f")
    return (
        f'<span style="background:{colour};color:#fff;padding:1px 6px;'
        f'border-radius:3px;font-size:.78em;margin-right:4px;">{category}</span>'
    )

def write_jekyll_files(items: list[dict], news_dir: Path) -> None:
    news_dir.mkdir(exist_ok=True)

    # remove old auto-generated files
    for old in sorted(news_dir.glob("announcement_[0-9][0-9][0-9][0-9].md")):
        old.unlink()

    for idx, item in enumerate(items, start=10):
        fname  = news_dir / f"announcement_{idx:04d}.md"
        date   = item["date"] or "2025-01-01"

        # news_title: clean title without the [category] bracket
        news_title = item["clean_title"]

        # news_description: paper title + link, or fallback to NPL post link
        if item["paper_url"]:
            link_text   = item["paper_title"] or "원문 보기"
            description = f'→ <a href="{item["paper_url"]}" target="_blank">{link_text}</a>'
        elif item["url"]:
            description = f'→ <a href="{item["url"]}" target="_blank">게시글 보기</a>'
        else:
            description = ""

        # category: used by news.liquid for the badge class
        category = item["category"]

        content = f"""---
layout: post
date: {date} 09:00:00+0900
inline: true
related_posts: false
category: "{category}"
news_title: "{news_title}"
news_description: '{description}'
---
"""
        fname.write_text(content, encoding="utf-8")


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    print(f"Step 1: Collecting article URLs from {MAX_PAGES} list pages …")
    urls = collect_article_urls(MAX_PAGES)
    print(f"  → {len(urls)} unique articles found\n")

    print("Step 2: Fetching each article detail page …")
    items = []
    for i, url in enumerate(urls, 1):
        item = parse_article(url)
        items.append(item)
        print(f"  [{i:3d}/{len(urls)}] [{item['date'] or '----'}] "
              f"[{item['category']}] {item['clean_title'][:55]}")
        time.sleep(DELAY)

    # ── save JSON ────────────────────────────────────────────────────────────
    out_json = Path("news_data.json")
    out_json.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSaved {len(items)} items → {out_json}")

    # ── write Jekyll files ───────────────────────────────────────────────────
    write_jekyll_files(items, Path("_news"))
    print(f"Written {len(items)} Jekyll announcement files → _news/")
    print("\nDone!")


if __name__ == "__main__":
    main()
