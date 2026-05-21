// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

if (navToggle && mainNav) {
  navToggle.addEventListener('click', function (e) {
    e.stopPropagation();
    mainNav.classList.toggle('open');
    const isOpen = mainNav.classList.contains('open');
    navToggle.setAttribute('aria-expanded', isOpen);
  });
}

// Close nav on outside click
document.addEventListener('click', function (e) {
  if (mainNav && mainNav.classList.contains('open')) {
    if (!mainNav.contains(e.target) && e.target !== navToggle) {
      mainNav.classList.remove('open');
      if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
    }
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      // Close mobile nav if open
      if (mainNav) mainNav.classList.remove('open');
    }
  });
});
