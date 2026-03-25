/* ── BhAAi Fans Digital AA — form.js ── */

document.addEventListener('DOMContentLoaded', () => {

  const form = document.getElementById('contact-form');
  if (!form) return;

  const inputs = form.querySelectorAll('input, textarea, select');

  // Floating label animation
  inputs.forEach(input => {
    input.addEventListener('focus', () => {
      input.closest('.form-group')?.classList.add('focused');
    });
    input.addEventListener('blur', () => {
      const g = input.closest('.form-group');
      if (!input.value) g?.classList.remove('focused');
      else g?.classList.add('has-value');
    });
    if (input.value) input.closest('.form-group')?.classList.add('has-value');
  });

  // Validation
  const validate = (field) => {
    const val = field.value.trim();
    const type = field.type;
    const name = field.name;
    const group = field.closest('.form-group');
    let valid = true;
    let msg = '';
    if (field.hasAttribute('required') && !val) {
      valid = false; msg = 'This field is required.';
    } else if (type === 'email' && val && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
      valid = false; msg = 'Please enter a valid email.';
    } else if (name === 'phone' && val && !/^[\d\s\+\-\(\)]{7,15}$/.test(val)) {
      valid = false; msg = 'Please enter a valid phone number.';
    }
    if (group) {
      group.classList.toggle('error', !valid);
      group.classList.toggle('success', valid && !!val);
      let err = group.querySelector('.error-msg');
      if (!valid) {
        if (!err) { err = document.createElement('span'); err.className = 'error-msg'; group.appendChild(err); }
        err.textContent = msg;
      } else if (err) err.remove();
    }
    return valid;
  };

  inputs.forEach(input => {
    input.addEventListener('blur', () => validate(input));
    input.addEventListener('input', () => {
      if (input.closest('.form-group')?.classList.contains('error')) validate(input);
    });
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    let allValid = true;
    inputs.forEach(input => { if (!validate(input)) allValid = false; });
    if (!allValid) return;

    const submitBtn = form.querySelector('[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    const data = Object.fromEntries(new FormData(form).entries());

    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      if (res.ok) {
        form.innerHTML = `
          <div class="form-success">
            <div class="success-icon">✓</div>
            <h3>Message received.</h3>
            <p>We'll get back to you within 24 hours.</p>
          </div>`;
      } else {
        throw new Error('Server error');
      }
    } catch {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      const err = form.querySelector('.form-error-global') || document.createElement('p');
      err.className = 'form-error-global';
      err.textContent = 'Something went wrong. Please try again or email us directly.';
      form.prepend(err);
    }
  });

});
