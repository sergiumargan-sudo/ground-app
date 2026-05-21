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

// Reviews carousel
(function () {
  const track = document.querySelector('.rc-track');
  if (!track) return;

  let slides = Array.from(track.querySelectorAll('.rc-slide'));
  const dots   = Array.from(document.querySelectorAll('.rc-dot'));
  const prevBtn = document.querySelector('.rc-prev');
  const nextBtn = document.querySelector('.rc-next');
  const outer   = document.querySelector('.rc-outer');
  const INTERVAL = 5500;

  // Shuffle order randomly on each page load
  for (let i = slides.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    track.appendChild(slides[j]);
    [slides[i], slides[j]] = [slides[j], slides[i]];
  }
  slides = Array.from(track.querySelectorAll('.rc-slide'));

  let current = 0;
  let timer;

  function show(idx) {
    slides.forEach((s, i) => s.classList.toggle('rc-active', i === idx));
    dots.forEach((d, i)  => d.classList.toggle('active',    i === idx));
    track.style.height = slides[idx].scrollHeight + 'px';
    current = idx;
  }

  function advance() { show((current + 1) % slides.length); }
  function retreat() { show((current - 1 + slides.length) % slides.length); }

  function startTimer() { timer = setInterval(advance, INTERVAL); }
  function stopTimer()  { clearInterval(timer); }

  show(0);
  startTimer();

  if (nextBtn) nextBtn.addEventListener('click', () => { stopTimer(); advance(); startTimer(); });
  if (prevBtn) prevBtn.addEventListener('click', () => { stopTimer(); retreat(); startTimer(); });

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => { stopTimer(); show(i); startTimer(); });
  });

  if (outer) {
    outer.addEventListener('mouseenter', stopTimer);
    outer.addEventListener('mouseleave', startTimer);
  }

  window.addEventListener('resize', () => {
    track.style.height = slides[current].scrollHeight + 'px';
  });

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stopTimer(); else startTimer();
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
