import os

PAGES_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\frontend\pages"

nav_replace = """<div class="nav-actions" style="display:flex; gap:1.5rem; align-items:center;">
      <a id="nav-login-btn" href="login.html" style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--white); text-decoration:none; transition:color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--white)'">Login</a>
      <a href="contact.html" class="nav-cta">Get in touch</a>
    </div>"""

auth_script = """  <script>
    // Authentication Check and Dynamic Navbar Update
    fetch('/auth/me')
      .then(res => res.json())
      .then(data => {
        const btn = document.getElementById('nav-login-btn');
        if (data.authenticated) {
          if (btn) {
            btn.textContent = 'Logout';
            btn.href = (data.type === 'admin') ? '/auth/logout' : '/auth/user/logout';
          }
        }
      });
  </script>
</body>"""

for root, _, files in os.walk(PAGES_DIR):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Add Login button to navbar
            if '<a href="contact.html" class="nav-cta">Get in touch</a>' in content:
                content = content.replace(
                    '<a href="contact.html" class="nav-cta">Get in touch</a>',
                    nav_replace
                )
                
            # Add dynamic login/logout state to ALL pages (before body close tag)
            if "Authentication Check and Dynamic Navbar Update" not in content and "</body>" in content:
                content = content.replace("</body>", auth_script)
                
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

print("Navbar updated extensively!")
