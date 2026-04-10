import os
import glob
import re
import shutil

ROOT_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\TTP\Agency\digital-agency-website"
FRONTEND_DIR = os.path.join(ROOT_DIR, "frontend")
PAGES_DIR = os.path.join(FRONTEND_DIR, "pages")
ADMIN_DIR = os.path.join(FRONTEND_DIR, "admin-dashboard")

# 1. Move HTML files from pages/ to frontend/ root
if os.path.exists(PAGES_DIR):
    for f in os.listdir(PAGES_DIR):
        if f.endswith(".html"):
            src = os.path.join(PAGES_DIR, f)
            dst = os.path.join(FRONTEND_DIR, f)
            shutil.move(src, dst)
            print(f"Moved {f} to frontend/ root.")

# 2. Process all HTML files in frontend/ and frontend/admin-dashboard/
def process_html_files(directory, prefix="/static/"):
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()

                # Regex to match {{ url_for('static', filename='path/to/file.ext') }}
                # and replace with /static/path/to/file.ext
                pattern = r"\{\{\s*url_for\('static',\s*filename=['\"]([^'\"]+)['\"]\)\s*\}\}"
                new_content = re.sub(pattern, lambda m: prefix + m.group(1), content)

                if content != new_content:
                    with open(path, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    print(f"Updated paths in {path}")

process_html_files(FRONTEND_DIR)

print("Finished preparing frontend static files.")
