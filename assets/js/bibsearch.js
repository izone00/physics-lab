import { highlightSearchTerm } from "./highlight-search-term.js";

document.addEventListener("DOMContentLoaded", function () {
  let currentPage = 1;
  const itemsPerPage = 10;

  const applyPagination = (scrollToTop = false) => {
    // 1. Reset visibility of all items
    document.querySelectorAll(".bibliography > li").forEach((el) => {
      el.classList.remove("page-hidden");
    });
    document.querySelectorAll("h2.bibliography, ol.bibliography").forEach((el) => {
      el.classList.remove("page-hidden");
    });

    // 2. Filter out items that don't match search (handled in filterItems)
    // 3. Paginate only the items that match the search
    const visibleItems = Array.from(document.querySelectorAll(".bibliography > li:not(.unloaded)"));
    const totalItems = visibleItems.length;
    const totalPages = Math.ceil(totalItems / itemsPerPage);

    visibleItems.forEach((item, index) => {
      if (index < (currentPage - 1) * itemsPerPage || index >= currentPage * itemsPerPage) {
        item.classList.add("page-hidden");
      }
    });

    // 4. Hide empty year headers
    document.querySelectorAll("h2.bibliography").forEach((header) => {
      let next = header.nextElementSibling;
      let hasVisibleContent = false;
      while (next && next.tagName !== "H2") {
        if (next.tagName === "OL") {
          const visibleInList = next.querySelectorAll(":scope > li:not(.unloaded):not(.page-hidden)");
          if (visibleInList.length > 0) {
            hasVisibleContent = true;
            break;
          }
        }
        next = next.nextElementSibling;
      }
      if (!hasVisibleContent) {
        header.classList.add("page-hidden");
        // Also hide the ol if it's empty
        let ol = header.nextElementSibling;
        if (ol && ol.tagName === "OL") ol.classList.add("page-hidden");
      }
    });

    // 5. Update Pagination UI
    updatePaginationUI(totalPages);

    if (scrollToTop) {
      const top = document.querySelector(".publications")?.offsetTop || 0;
      window.scrollTo({ top: top - 80, behavior: "smooth" });
    }
  };

  const updatePaginationUI = (totalPages) => {
    let container = document.querySelector(".bib-pagination");
    if (!container) {
      container = document.createElement("nav");
      container.className = "bib-pagination mt-5 mb-5";
      document.querySelector(".publications")?.appendChild(container);
    }

    if (totalPages <= 1) {
      container.innerHTML = "";
      return;
    }

    let html = '<ul class="pagination justify-content-center">';

    // Prev
    html += `<li class="page-item ${currentPage === 1 ? "disabled" : ""}">
              <a class="page-link" href="#" data-page="${currentPage - 1}">&laquo;</a>
            </li>`;

    // Page Numbers
    for (let i = 1; i <= totalPages; i++) {
      html += `<li class="page-item ${currentPage === i ? "active" : ""}">
                <a class="page-link" href="#" data-page="${i}">${i}</a>
              </li>`;
    }

    // Next
    html += `<li class="page-item ${currentPage === totalPages ? "disabled" : ""}">
              <a class="page-link" href="#" data-page="${currentPage + 1}">&raquo;</a>
            </li>`;

    html += "</ul>";
    container.innerHTML = html;

    // Click handlers
    container.querySelectorAll(".page-link").forEach((link) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        const page = parseInt(link.getAttribute("data-page"));
        if (page >= 1 && page <= totalPages) {
          currentPage = page;
          applyPagination(true);
        }
      });
    });
  };

  const filterItems = (searchTerm) => {
    currentPage = 1;
    document.querySelectorAll(".bibliography > li").forEach((element) => {
      element.classList.remove("unloaded");
    });

    document.querySelectorAll(".bibliography > li").forEach((element) => {
      const text = element.innerText.toLowerCase();
      if (searchTerm && text.indexOf(searchTerm) === -1) {
        element.classList.add("unloaded");
      }
    });

    applyPagination(false);
  };

  const updateInputField = () => {
    const hashValue = decodeURIComponent(window.location.hash.substring(1));
    const input = document.getElementById("bibsearch");
    if (input) {
      input.value = hashValue;
      filterItems(hashValue);
    } else {
      // Fallback if search bar isn't present
      applyPagination(false);
    }
  };

  let timeoutId;
  const searchInput = document.getElementById("bibsearch");
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      clearTimeout(timeoutId);
      const searchTerm = this.value.toLowerCase();
      timeoutId = setTimeout(() => filterItems(searchTerm), 300);
    });
  }

  window.addEventListener("hashchange", updateInputField);
  updateInputField();
});
