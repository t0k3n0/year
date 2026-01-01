from PIL import Image, ImageDraw, ImageFont
from datetime import date
import calendar

# --- CONFIGURATION ---
SCREEN_SIZE = (1170, 2532)
BG_COLOR = (20, 20, 20)        # Dark Charcoal Background (like reference)
FILLED_COLOR = (80, 80, 80)    # Light Gray (Past days)
EMPTY_COLOR = (40, 40, 40)     # Dark Gray (Future days)
ACTIVE_COLOR = (255, 100, 50)  # Orange (Current day)
TEXT_COLOR = (150, 150, 150)   # Dim gray for text

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

    # --- LAYOUT CALCULATIONS ---
    cols = 7
    rows = 53
    gap = 25                   # Space between dots
    dot_radius = 20            # Size of dots
    dot_size = dot_radius * 2
    
    # Calculate total grid size to center it
    grid_width = (cols * dot_size) + ((cols - 1) * gap)
    grid_height = (rows * dot_size) + ((rows - 1) * gap)
    
    start_x = (SCREEN_SIZE[0] - grid_width) // 2
    start_y = (SCREEN_SIZE[1] - grid_height) // 2

    # --- FONTS ---
    # Try to load a standard font (works on GitHub Ubuntu runners)
    try:
        # Size 40 is roughly "size 10" on a high-res phone screen
        font_main = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    except IOError:
        font_main = ImageFont.load_default()
        font_label = ImageFont.load_default()

    # --- DRAW LABELS (AXES) ---
    # X-Axis Label: "DAYS"
    draw.text((start_x + grid_width//2, start_y - 60), "DAYS", fill=TEXT_COLOR, font=font_label, anchor="ms")
    
    # Y-Axis Label: "WEEKS" (Manually drawn vertically)
    # PIL doesn't rotate text easily without making a new image, so we draw letters vertically
    y_label_x = start_x - 50
    y_label_y = start_y + grid_height // 2 - 100
    for i, char in enumerate("WEEKS"):
        draw.text((y_label_x, y_label_y + (i * 35)), char, fill=TEXT_COLOR, font=font_label, anchor="mm")

    # --- DRAW GRID ---
    current_day_index = 1 # Start at 1
    
    for row in range(rows):
        for col in range(cols):
            if current_day_index > total_days:
                break
                
            x = start_x + col * (dot_size + gap)
            y = start_y + row * (dot_size + gap)
            
            box = [x, y, x + dot_size, y + dot_size]
            
            if current_day_index < day_of_year:
                # Past
                draw.ellipse(box, fill=FILLED_COLOR)
            elif current_day_index == day_of_year:
                # Today (Orange)
                draw.ellipse(box, fill=ACTIVE_COLOR)
            else:
                # Future
                draw.ellipse(box, fill=EMPTY_COLOR)
            
            current_day_index += 1

    # --- DRAW FOOTER STATS ---
    # Text: "300d left • 18%"
    stats_text = f"{days_left}d left  •  {percent_done}%"
    
    # Draw at bottom center
    draw.text((SCREEN_SIZE[0]//2, start_y + grid_height + 80), stats_text, fill=ACTIVE_COLOR, font=font_main, anchor="mm")

    img.save("year_progress.png")
    print("Year progress wallpaper generated.")

if __name__ == "__main__":
    create_year_wallpaper()
