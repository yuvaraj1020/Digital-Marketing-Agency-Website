import os
import glob
from PIL import Image

ARTIFACTS_DIR = r"C:\Users\YUVARAJ\.gemini\antigravity\brain\ae0aa723-6d13-4255-9139-ff0baf4d094e"
TARGET_DIR = r"c:\Users\YUVARAJ\OneDrive\Desktop\Agency\digital-agency-website\frontend\static\images\portfolio"

os.makedirs(TARGET_DIR, exist_ok=True)

patterns = [
    ("portfolio_resume", "portfolio1.jpg"),
    ("portfolio_personal", "portfolio2.jpg"),
    ("portfolio_ecommerce", "portfolio3.jpg"),
    ("portfolio_social", "portfolio4.jpg"),
    ("portfolio_startup", "portfolio5.jpg"),
    ("portfolio_youtube", "portfolio6.jpg")
]

for prefix, dest_filename in patterns:
    files = glob.glob(os.path.join(ARTIFACTS_DIR, f"{prefix}*.png"))
    if files:
        latest_file = max(files, key=os.path.getmtime)
        try:
            img = Image.open(latest_file)
            rgb_im = img.convert('RGB')
            # Save strictly as .jpg to match index.html implementation
            target_path = os.path.join(TARGET_DIR, dest_filename)
            rgb_im.save(target_path, "JPEG", quality=90)
            print(f"Mapped {prefix} to {dest_filename}")
        except Exception as e:
            print(f"Failed to copy {prefix}: {e}")
    else:
        print(f"Skipped {prefix} (not found)")

print("Migration complete!")
