import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import sys

# Paths
BASE_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website"
ASSETS_DIR = os.path.join(BASE_DIR, "frontend", "assets")
STATIC_DIR = os.path.join(BASE_DIR, "frontend", "static")
IMAGES_DIR = os.path.join(STATIC_DIR, "images")
PORTFOLIO_DIR = os.path.join(IMAGES_DIR, "portfolio")
AI_IMGS_DIR = r"C:\Users\YUVARAJ\.gemini\antigravity\brain\ae0aa723-6d13-4255-9139-ff0baf4d094e"

# Rename assets to static if exists
if os.path.exists(ASSETS_DIR):
    shutil.move(ASSETS_DIR, STATIC_DIR)
    print("Moved frontend/assets -> frontend/static")

os.makedirs(PORTFOLIO_DIR, exist_ok=True)

def copy_ai_img(ai_prefix, target_name):
    # Find latest file with prefix in AI dir
    try:
        files = [f for f in os.listdir(AI_IMGS_DIR) if f.startswith(ai_prefix) and f.endswith(".png")]
        if files:
            files.sort(key=lambda x: os.path.getmtime(os.path.join(AI_IMGS_DIR, x)), reverse=True)
            source = os.path.join(AI_IMGS_DIR, files[0])
            dest = os.path.join(IMAGES_DIR, target_name)
            shutil.copy2(source, dest)
            print(f"Copied {files[0]} -> {target_name}")
            return True
    except Exception as e:
        print(f"Error copying {ai_prefix}: {e}")
    return False

# Copy successfully generated images
copy_ai_img("team_", "team.jpg")
copy_ai_img("portfolio1_", os.path.join("portfolio", "portfolio1.jpg"))
copy_ai_img("portfolio2_", os.path.join("portfolio", "portfolio2.jpg"))

# Generate placeholders using PIL for remaining
def create_placeholder(text, path, color):
    img = Image.new('RGB', (800, 600), color=color)
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    bbox = d.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    d.text(((800-text_w)/2, (600-text_h)/2), text, fill="white", font=font)
    img.save(path)
    print(f"Generated placeholder -> {path}")

create_placeholder("Resume Builder", os.path.join(PORTFOLIO_DIR, "portfolio1.jpg"), "#1a1a1a") # Fallback if missing
create_placeholder("Personal Portfolio", os.path.join(PORTFOLIO_DIR, "portfolio2.jpg"), "#2a2a2a")
create_placeholder("E-Commerce UI", os.path.join(PORTFOLIO_DIR, "portfolio3.jpg"), "#333333")
create_placeholder("Ad Campaigns", os.path.join(PORTFOLIO_DIR, "portfolio4.jpg"), "#1a1a1a")
create_placeholder("Startup Landing", os.path.join(PORTFOLIO_DIR, "portfolio5.jpg"), "#222222")
create_placeholder("YouTube Analytics", os.path.join(PORTFOLIO_DIR, "portfolio6.jpg"), "#444444")

# Also copy team if not exists
if not os.path.exists(os.path.join(IMAGES_DIR, "team.jpg")):
    create_placeholder("Agency Workspace", os.path.join(IMAGES_DIR, "team.jpg"), "#111111")
