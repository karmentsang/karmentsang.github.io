
 /* =========================  TEXT WITH BLINKING CURSOR  ========================= */

const text = "A portfolio that brings together the things I create!";
const element = document.getElementById('blinking');

// Create a text node with the full text instantly
const textNode = document.createTextNode(text);

// Create the blinking cursor span
const cursor = document.createElement('span');
cursor.className = 'blink';
cursor.textContent = '_';

element.appendChild(textNode);
element.appendChild(cursor);


/* =========================  INTERSECTION OBSERVER  ========================= */

document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const caption = entry.target.querySelector('.textfade');
      if (!caption) return;

      if (entry.isIntersecting) {
        caption.classList.add('in-view');   // fade / slide in
      } else {
        caption.classList.remove('in-view'); // fade / slide out
      }
    });
  }, { threshold: 0.4 });   // 40% of the section is visible

  document.querySelectorAll('.hero').forEach(hero => observer.observe(hero));
});

/* =========================  FOOTER ANIMATION  ========================= */


(() => {
  const footer          = document.querySelector('.footer_background');
  const EXTRA_SCROLL_PX = 120;   // how far user must "push" past bottom
  const SCROLL_LOCK_GAP = 2;     // px we nudge page after footer closed
  let   footerVisible   = false; // current state
  let   scrollLocked    = false; // block real scroll while footer animates
  let   touchStartY     = 0;     // for swipe detection

  /* =========================  HELPERS  ========================= */
  const nearBottom = () => {
    const pageBottom   = window.scrollY + window.innerHeight;
    const maxScrollPos = document.documentElement.scrollHeight;
    return maxScrollPos - pageBottom < EXTRA_SCROLL_PX;
  };

  const showFooter = () => {
    footer.classList.add('visible');
    footerVisible = true;
  };

  const hideFooterThenUnlock = () => {
    scrollLocked = true;          // freeze page for the animation
    footer.classList.remove('visible');
    footer.addEventListener('transitionend', () => {
      scrollLocked = false;
      window.scrollBy(0, -SCROLL_LOCK_GAP); // give the page a gentle nudge up
      footerVisible = false;
    }, { once: true });
  };

  /* =========================  SCROLL LISTENER  ========================= */
  window.addEventListener('scroll', () => {
    if (!footerVisible) return;   // nothing to do

    // If user is no longer near bottom, hide immediately (no lock needed)
    if (!nearBottom()) footer.classList.remove('visible'), footerVisible = false;
  });

  /* =========================  MOUSEWHEEL / TRACKPAD  ========================= */
  window.addEventListener('wheel', e => {
    if (scrollLocked) { e.preventDefault(); return; }

    // ↓ scrolling down
    if (e.deltaY > 0 && !footerVisible && nearBottom()) {
      showFooter();
      return; // allow the "push" down event
    }

    // ↑ scrolling up while footer showing
    if (e.deltaY < 0 && footerVisible) {
      e.preventDefault();         // stop page from moving
      hideFooterThenUnlock();
    }
  }, { passive:false });

  /* =========================  TOUCH - MOBILE TABLET  ========================= */
  window.addEventListener('touchstart', e => { touchStartY = e.touches[0].clientY; });

  window.addEventListener('touchmove', e => {
    if (scrollLocked) { e.preventDefault(); return; }

    const deltaY = touchStartY - e.touches[0].clientY; // positive = swipe up

    // swipe‑up near bottom → show footer
    if (deltaY > 8 && !footerVisible && nearBottom()) {
      showFooter();
      return;
    }

    // swipe‑down while footer visible → hide footer first
    if (deltaY < -8 && footerVisible) {
      e.preventDefault();
      hideFooterThenUnlock();
    }
  }, { passive:false });
})();

