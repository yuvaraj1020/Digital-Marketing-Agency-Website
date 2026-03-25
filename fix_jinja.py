import os

PAGES_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\frontend\pages"
ADMIN_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\admin-dashboard"

def fix_files(directory):
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Jinja2 cannot parse \' so we just replace \' with ' inside the url_for blocks
                # e.g url_for(\'static\' -> url_for('static'
                content = content.replace("\\'", "'")
                
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Fixed {f}")

fix_files(PAGES_DIR)
fix_files(ADMIN_DIR)
print("Finished fixing Jinja syntax!")
