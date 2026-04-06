import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import urllib3

# Suppress insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_soup(url):
    response = requests.get(url, headers=HEADERS, verify=False)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'html.parser')

def extract_professor_info():
    url = "https://npl.pusan.ac.kr/npl/50928/subview.do"
    print(f"Scraping Professor info from {url}...")
    soup = get_soup(url)
    
    # Try to find the generic content wrapper
    content_area = soup.select_one('._contentBuilder, .board-wrap, .content, #sub-content, .sub_content, article')
    if not content_area:
        content_area = soup.body
        
    paragraphs = content_area.find_all(['p', 'h1', 'h2', 'h3', 'li'])
    text_data = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    
    return {
        "greeting": " ".join(text_data[:5]), # Just attempting approximation
        "bio": text_data[5:] if len(text_data) > 5 else []
    }

def extract_members_info():
    url = "https://npl.pusan.ac.kr/npl/50929/subview.do"
    print(f"Scraping Members info from {url}...")
    soup = get_soup(url)
    
    members = []
    profiles = soup.select('ul._prFlList li._prFlLi')
    
    for item in profiles:
        name_tag = item.select_one('.artclTitle a strong')
        name = name_tag.get_text(strip=True) if name_tag else ""
        
        title, email = "", ""
        for dl in item.find_all('dl'):
            dt = dl.find('dt')
            if dt and "직위" in dt.text:
                dd = dl.find('dd')
                title = dd.get_text(strip=True) if dd else ""
            elif dt and "이메일" in dt.text:
                dd = dl.find('dd')
                email = dd.get_text(strip=True) if dd else ""
                
        img = item.find('img')
        img_url = "https://npl.pusan.ac.kr" + img['src'] if img and img.get('src') and not img['src'].startswith('http') else (img['src'] if img and img.get('src') else None)
        
        members.append({
            "name": name,
            "title": title,
            "email": email,
            "photo_url": img_url,
            "raw_text": item.get_text(separator=' ', strip=True)
        })
            
    if not members:
        content = soup.select_one('._contentBuilder, .content, #sub-content')
        if content:
            imgs = content.find_all('img')
            members.append({
                "raw_text": content.get_text(strip=True),
                "images": ["https://npl.pusan.ac.kr" + i['src'] if i.get('src') and not i['src'].startswith('http') else i.get('src') for i in imgs]
            })
            
    return members

def extract_research_info():
    url = "https://npl.pusan.ac.kr/npl/50935/subview.do"
    print(f"Scraping Research info from {url}...")
    soup = get_soup(url)
    
    topics = []
    # Identify headings and corresponding paragraphs
    content_div = soup.select_one('._contentBuilder, .content, #sub-content, .sub_content')
    if content_div:
        headings = content_div.find_all(['h2', 'h3', 'h4', 'strong'])
        for h in headings:
            title = h.get_text(strip=True)
            if not title:
                continue
            
            p = h.find_next_sibling('p')
            desc = p.get_text(strip=True) if p else "Description not found structurally."
            topics.append({
                "title": title,
                "description": desc
            })
    return topics

def extract_publications_selenium():
    url = "https://npl.pusan.ac.kr/npl/50949/subview.do"
    print(f"Scraping Publications (with Selenium) from {url}...")
    publications = []
    
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        driver.get(url)
        time.sleep(2)  # Wait for page to load
        
        while True:
            items = driver.find_elements(By.CSS_SELECTOR, "table tbody tr, .board-list li, .pub-item")
            for item in items:
                text = item.text.strip()
                if text:
                    publications.append({"raw_text": text})
            
            try:
                next_page = driver.find_element(By.CSS_SELECTOR, ".paging .active + a, .pagination .active + a, a.next")
                if next_page:
                    print("Clicking next page...")
                    next_page.click()
                    time.sleep(2)
                else:
                    break
            except Exception:
                break
        driver.quit()
    except Exception as e:
        print(f"Selenium failed (likely Chrome is not installed on this OS): {e}")
        print("Falling back to requests for the first page of Publications...")
        soup = get_soup(url)
        items = soup.select("table tbody tr, .board-list li, .pub-item, ._artclList li")
        if not items:
            content = soup.select_one('._contentBuilder, .content, #sub-content, .board-wrap')
            if content:
                publications.append({"raw_text": content.get_text(separator=' ', strip=True)})
        for item in items:
            publications.append({"raw_text": item.get_text(separator=' ', strip=True)})
            
    return publications

def main():
    print("Starting crawler...")
    data = {}
    
    data['Professor'] = extract_professor_info()
    data['Members'] = extract_members_info()
    data['Research'] = extract_research_info()
    data['Publications'] = extract_publications_selenium()
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Data saved to data.json")

if __name__ == "__main__":
    main()
