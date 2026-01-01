import os
from PIL import Image, ImageDraw
from datetime import date

# --- CONFIGURATION ---
# This fetches your hidden birthday. If missing, it defaults to 2000-01-01.
birthday_str = os.environ.get("USER_BIRTHDAY", "2000-01-01")
try:
    y, m, d = map(int, birthday_str.split('-'))
    BIRTHDAY = date(y, m, d)
except ValueError:
    BIRTHDAY = date(2000, 1, 1)

LIFESPAN_YEARS = 90
SCREEN_SIZE = (1170, 2532)
BG_COLOR = (0, 0, 0)         # Black
DOT_COLOR_FILLED = (255, 255, 255) # White
DOT_COLOR_EMPTY = (50, 50, 50)     # Dark Gray

def create_wallpaper():
    today = date.today()
    weeks_lived = (today - BIRTHDAY).days // 7
    img = Image.new('RGB', SCREEN_SIZE, color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Grid Settings
    margin_x = 100
    margin_y = 400
    cols = 52
    rows = LIFESPAN_YEARS
    
    available_width = SCREEN_SIZE[0] - (2 * margin_x)
    gap = 8 
    dot_size = (available_width - (cols - 1) * gap) / cols
    
    current_week_index = 0
    for row in range(rows):
        for col in range(cols):
            x = margin_x + col * (dot_size + gap)
            y = margin_y + row * (dot_size + gap)
            
            if current_week_index < weeks_lived:
                draw.ellipse([x, y, x + dot_size, y + dot_size], fill=DOT_COLOR_FILLED)
            else:
                draw.ellipse([x, y, x + dot_size, y + dot_size], fill=DOT_COLOR_EMPTY)
            current_week_index += 1

    img.save("wallpaper.png")
    print("Wallpaper generated.")

if __name__ == "__main__":
    create_wallpaper()
