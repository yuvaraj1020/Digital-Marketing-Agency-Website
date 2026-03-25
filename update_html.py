import os
import re

PAGES_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\frontend\pages"
ADMIN_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\admin-dashboard"

def update_files(directory):
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Replace src="/assets/..." -> src="{{ url_for('static', filename='...') }}"
                content = re.sub(r'src="/assets/([^"]+)"', r'src="{{ url_for(\'static\', filename=\'\1\') }}"', content)
                
                # Replace href="/assets/..." -> href="{{ url_for('static', filename='...') }}"
                content = re.sub(r'href="/assets/([^"]+)"', r'href="{{ url_for(\'static\', filename=\'\1\') }}"', content)
                
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {f}")

update_files(PAGES_DIR)
update_files(ADMIN_DIR)
print("Finished applying Jinja2 url_for templates across all HTML pages!")
