/**
 * Sun Wei personal site — progressive enhancement
 * Sticky glass header, mobile nav, scroll reveals
 */

(() => {
  "use strict";

  const header = document.getElementById("site-header");
  const toggle = document.querySelector(".nav-toggle");
  const mobileNav = document.getElementById("mobile-nav");
  const yearEl = document.getElementById("year");

  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  /* Header: strengthen glass edge after scroll */
  const updateHeader = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });

  /* Mobile menu */
  if (toggle && mobileNav) {
    const setOpen = (open) => {
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      mobileNav.hidden = !open;
      document.body.style.overflow = open ? "hidden" : "";
    };

    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") !== "true";
      setOpen(open);
    });

    mobileNav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => setOpen(false));
    });

    window.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  /* Section reveals — skip if user prefers reduced motion */
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const reveals = document.querySelectorAll(".reveal");

  if (!reduceMotion && "IntersectionObserver" in window && reveals.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
    );

    reveals.forEach((el) => observer.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-visible"));
  }
  /* Category filters on list pages */
  const filterBar = document.querySelector("[data-filter-bar]");
  if (filterBar) {
    const buttons = filterBar.querySelectorAll("[data-filter]");
    const items = document.querySelectorAll("[data-category]");

    filterBar.addEventListener("click", (event) => {
      const button = event.target.closest("[data-filter]");
      if (!button) return;

      const filter = button.getAttribute("data-filter");
      buttons.forEach((btn) => {
        const active = btn === button;
        btn.classList.toggle("is-active", active);
        btn.setAttribute("aria-pressed", String(active));
      });

      items.forEach((item) => {
        const category = item.getAttribute("data-category");
        const show = filter === "all" || category === filter;
        item.classList.toggle("is-hidden", !show);
      });
    });
  }
})();
