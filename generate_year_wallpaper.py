from PIL import Image, ImageDraw
from datetime import date
import calendar

# --- CONFIGURATION ---
SCREEN_SIZE = (1170, 2532)
BG_COLOR = (0, 0, 0)           # Black
FILLED_COLOR = (255, 255, 255) # White (Days passed)
EMPTY_COLOR = (50, 50, 50)     # Dark Gray (Future days)

def create_year_wallpaper():
    today = date.today()
    year = today.year
    is_leap = calendar.isleap(year)
    total_days = 366 if is_leap else 365
    
    # Get current day number (1 to 365/366)
    day_of_year = today.timetuple().tm_yday

    img = Image.new('RGB', SCREEN_SIZE, color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Grid Settings for a 7-column layout (Weeks)
    cols = 7 
    rows = 53 # Max weeks in a year
    
    margin_x = 150
    margin_y = 400
    
    # Calculate spacing
    available_width = SCREEN_SIZE[0] - (2 * margin_x)
    gap = 15
    # Calculate square size based on width
    square_size = (available_width - (cols - 1) * gap) / cols

    current_day_index = 0
    
    for row in range(rows):
        for col in range(cols):
            if current_day_index >= total_days:
                break
                
            x = margin_x + col * (square_size + gap)
            y = margin_y + row * (square_size + gap)
            
            # Draw Square
            # passed days are filled, today is filled, future is empty
            if current_day_index < day_of_year:
                draw.rectangle([x, y, x + square_size, y + square_size], fill=FILLED_COLOR)
            else:
                draw.rectangle([x, y, x + square_size, y + square_size], fill=EMPTY_COLOR)
            
            current_day_index += 1

    img.save("year_progress.png")
    print("Year progress wallpaper generated.")

if __name__ == "__main__":
    create_year_wallpaper()
