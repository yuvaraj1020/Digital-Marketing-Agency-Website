/* ── BhAAi Fans Digital AA — animations.js ── */

document.addEventListener('DOMContentLoaded', () => {

  // ── Page load intro ──
  const intro = document.createElement('div');
  intro.id = 'page-intro';
  intro.style.cssText = `
    position:fixed;inset:0;background:#0a0a0a;z-index:9000;
    display:flex;align-items:center;justify-content:center;
    transition:opacity 0.6s ease, transform 0.6s ease;
  `;
  intro.innerHTML = `
    <div style="text-align:center;">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:3rem;letter-spacing:0.1em;color:#f5f0e8;opacity:0;transition:opacity 0.5s ease;" id="intro-logo">BhAAi Fans</div>
      <div style="font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:0.3em;text-transform:uppercase;color:#c8ff00;margin-top:0.5rem;opacity:0;transition:opacity 0.5s ease 0.2s;" id="intro-sub">Digital AA</div>
      <div style="width:60px;height:1px;background:#c8ff00;margin:1.5rem auto 0;transform:scaleX(0);transform-origin:left;transition:transform 0.8s ease 0.4s;" id="intro-line"></div>
    </div>`;
  document.body.prepend(intro);

  requestAnimationFrame(() => {
    document.getElementById('intro-logo').style.opacity = '1';
    document.getElementById('intro-sub').style.opacity = '1';
    document.getElementById('intro-line').style.transform = 'scaleX(1)';
  });

  setTimeout(() => {
    intro.style.opacity = '0';
    intro.style.transform = 'translateY(-100%)';
    setTimeout(() => intro.remove(), 600);
  }, 1400);

  // ── Stagger hero text ──
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle) {
    const text = heroTitle.innerHTML;
    heroTitle.style.opacity = '0';
    heroTitle.style.transform = 'translateY(60px)';
    setTimeout(() => {
      heroTitle.style.transition = 'opacity 1s ease 1.6s, transform 1s ease 1.6s';
      heroTitle.style.opacity = '1';
      heroTitle.style.transform = 'translateY(0)';
    }, 100);
  }

  document.querySelectorAll('.hero-eyebrow, .hero-tagline, .hero-actions').forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    setTimeout(() => {
      el.style.transition = `opacity 0.8s ease ${1.8 + i * 0.15}s, transform 0.8s ease ${1.8 + i * 0.15}s`;
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    }, 100);
  });

  // ── Magnetic buttons ──
  document.querySelectorAll('.btn-primary, .btn-ghost, .btn-dark').forEach(btn => {
    btn.addEventListener('mousemove', e => {
      const r = btn.getBoundingClientRect();
      const x = e.clientX - r.left - r.width / 2;
      const y = e.clientY - r.top - r.height / 2;
      btn.style.transform = `translate(${x * 0.18}px, ${y * 0.18}px)`;
    });
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = '';
    });
  });

  // ── Text scramble on hover for section labels ──
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  document.querySelectorAll('.section-label').forEach(el => {
    const original = el.textContent;
    let interval;
    el.addEventListener('mouseenter', () => {
      let iter = 0;
      clearInterval(interval);
      interval = setInterval(() => {
        el.textContent = original.split('').map((c, i) => {
          if (i < iter) return original[i];
          if (c === ' ') return ' ';
          return chars[Math.floor(Math.random() * chars.length)];
        }).join('');
        if (iter >= original.length) clearInterval(interval);
        iter += 1.5;
      }, 30);
    });
    el.addEventListener('mouseleave', () => {
      clearInterval(interval);
      el.textContent = original;
    });
  });

  // ── Parallax on hero ──
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      heroBg.style.transform = `translateY(${y * 0.3}px)`;
    }, { passive: true });
  }

});
