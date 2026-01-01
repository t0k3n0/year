from PIL import Image, ImageDraw, ImageFont
from datetime import date
import calendar

# --- CONFIGURATION ---
SCREEN_SIZE = (1170, 2532)
BG_COLOR = (20, 20, 20)        # Dark Charcoal (Matches your reference)
FILLED_COLOR = (80, 80, 80)    # Light Gray (Past days)
EMPTY_COLOR = (40, 40, 40)     # Dark Gray (Future days)
ACTIVE_COLOR = (255, 100, 50)  # Orange (Current day)
TEXT_COLOR = (200, 200, 200)   # Light Gray for labels

def create_year_wallpaper():
    today = date.today()
    year = today.year
    is_leap = calendar.isleap(year)
    total_days = 366 if is_leap else 365
    day_of_year = today.timetuple().tm_yday
    
    # Calculate stats
    days_left = total_days - day_of_year
    percent_done = int((day_of_year / total_days) * 100)

    img = Image.new('RGB', SCREEN_SIZE, color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # --- GRID SETTINGS ---
    cols = 7
    rows = 53
    gap = 25                   
    dot_radius = 20            
    dot_size = dot_radius * 2
    
    # Calculate grid dimensions to center it
    grid_width = (cols * dot_size) + ((cols - 1) * gap)
    grid_height = (rows * dot_size) + ((rows - 1) * gap)
    
    # Center Point
    start_x = (SCREEN_SIZE[0] - grid_width) // 2
    start_y = (SCREEN_SIZE[1] - grid_height) // 2

    # --- FONTS ---
    try:
        # Standard fonts on GitHub servers
        font_main = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    except IOError:
        font_main = ImageFont.load_default()
        font_label = ImageFont.load_default()

    # --- LABELS ---
    
    # 1. Top Label: "DAYS"
    # Centered above the grid
    draw.text((SCREEN_SIZE[0]//2, start_y - 70), "DAYS", fill=TEXT_COLOR, font=font_label, anchor="ms")
    
    # 2. Side Label: "WEEKS"
    # Positioned to the left of the grid, vertically centered
    # We subtract 80px from start_x to move it left
    draw.text((start_x - 60, start_y + grid_height//2), "WEEKS", fill=TEXT_COLOR, font=font_label, anchor="rm")

    # --- DRAW GRID ---
    current_day_index = 1
    
    for row in range(rows):
        for col in range(cols):
            if current_day_index > total_days:
                break
                
            x = start_x + col * (dot_size + gap)
            y = start_y + row * (dot_size + gap)
            
            box = [x, y, x + dot_size, y + dot_size]
            
            if current_day_index < day_of_year:
                draw.ellipse(box, fill=FILLED_COLOR)
            elif current_day_index == day_of_year:
                draw.ellipse(box, fill=ACTIVE_COLOR)
            else:
                draw.ellipse(box, fill=EMPTY_COLOR)
            
            current_day_index += 1

    # --- FOOTER STATS ---
    # Matches reference: "364d left • 0%"
    stats_text = f"{days_left}d left  •  {percent_done}%"
    draw.text((SCREEN_SIZE[0]//2, start_y + grid_height + 80), stats_text, fill=ACTIVE_COLOR, font=font_main, anchor="mm")

    img.save("year_progress.png")
    print("Year progress wallpaper generated.")

if __name__ == "__main__":
    create_year_wallpaper()
