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

// Hero Slideshow
(function () {
  const slides = document.querySelectorAll('.hero-slide');
  if (!slides.length) return;

  const INTERVAL = 6000;
  const kbAnims = ['kb1', 'kb2', 'kb3', 'kb4', 'kb5'];
  let current = 0;
  let timer;

  function showSlide(idx) {
    const slide = slides[idx];
    slide.style.animation = 'none';
    void slide.getBoundingClientRect();
    slide.style.animation = kbAnims[idx % kbAnims.length] + ' 8s ease-in-out forwards';
    slide.classList.add('is-active');
  }

  function advance() {
    slides[current].classList.remove('is-active');
    current = (current + 1) % slides.length;
    showSlide(current);
    // Preload slide after next
    const preloadIdx = (current + 1) % slides.length;
    const bg = slides[preloadIdx].style.backgroundImage.replace(/url\(['"]?|['"]?\)/g, '');
    if (bg) { const i = new Image(); i.src = bg; }
  }

  showSlide(0);
  timer = setInterval(advance, INTERVAL);

  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      clearInterval(timer);
    } else {
      timer = setInterval(advance, INTERVAL);
    }
  });
})();

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
