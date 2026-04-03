import os
import glob

pages_dir = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\frontend\pages"
admin_dir = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\admin-dashboard"

# Define mappings
replacements = {
    '../css/': '/assets/css/',
    '../images/': '/assets/images/',
    '../js/': '/assets/js/',
    'css/': '/assets/css/',    # For some admin files if they use relative
    'js/': '/assets/js/'       # For some admin files if they use relative
}

def process_dir(directory):
    for filepath in glob.glob(os.path.join(directory, '*.html')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements.items():
            content = content.replace(f'="{old}', f'="{new}')
            content = content.replace(f"='{old}", f"='{new}")
            content = content.replace(f"({old}", f"({new}") # CSS url(...)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

process_dir(pages_dir)
process_dir(admin_dir)

print("Updated paths successfully.")
