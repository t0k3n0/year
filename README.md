# Life & Year Progress Wallpapers

A "set and forget" automation that generates a dynamic wallpaper for your iPhone every morning. It runs on GitHub Actions (for free) and updates your lock screen via iOS Shortcuts.

## Features
* **Life in Weeks:** A "Memento Mori" grid showing your past and future weeks.
* **Year Progress:** A daily updated grid of the current year (365 days), highlighting today in orange.
* **Zero Battery Drain:** All graphics are rendered on the server; your phone just downloads the final image.

## Setup Guide

### 1. Fork this Repository
Click the **Fork** button (top right) to create your own copy of this project.

### 2. Set Your Birthday
1.  Go to **Settings** > **Secrets and variables** > **Actions**.
2.  Click **New repository secret**.
3.  **Name:** `USER_BIRTHDAY`
4.  **Secret:** `1995-01-01` (YYYY-MM-DD).
    * *Note: If you skip this, it defaults to the year 2000.*

### 3. Activate the Generator
1.  Go to the **Actions** tab.
2.  Click **Update Wallpapers** on the left.
3.  Click **Run workflow** to generate your first set of images.

---

## 📱 Customizing for Your Phone

The default resolution is set for **iPhone 13/14/15 Pro** (`1170 x 2532`). If you have a Max, Plus, or Mini model, you should update the resolution so the grid is perfectly centered.

### How to Change Resolution
1.  Open `generate_wallpaper.py` (Life) and `generate_year_wallpaper.py` (Year).
2.  Click the **Pencil Icon** to edit.
3.  Find this line near the top:
    ```python
    SCREEN_SIZE = (1170, 2532)
    ```
4.  Change it to your device's resolution:
    * **iPhone 14/15/16 Pro Max:** `(1290, 2796)`
    * **iPhone 13/14 Pro Max:** `(1284, 2778)`
    * **iPhone 11 / XR:** `(828, 1792)`
    * **iPhone 12 / 13 Mini:** `(1080, 2340)`

### Advanced Style Tweaks
Inside `generate_year_wallpaper.py`, you can modify these variables to change the look:

* **Make it Compact/Squared:**
    Change `gap = 4` and replace `draw.ellipse` with `draw.rectangle` in the code.
* **Change Colors:**
    Update `BG_COLOR` (Background) or `ACTIVE_COLOR` (Today's Dot) using RGB values (e.g., `(255, 0, 0)` is Red).

---

## 🔗 iOS Shortcut Setup

You need to create a simple Shortcut on your iPhone to fetch the image.

### Option A: Single Wallpaper
1.  Create a shortcut with **Get Contents of URL**.
2.  Paste your **Raw Image Link**:
    * `https://raw.githubusercontent.com/<YOUR_USERNAME>/year/main/year_progress.png`
    * *(Or use `wallpaper.png` for the Life view)*
3.  Add **Get Image from Input**.
4.  Add **Set Wallpaper** (Turn off "Show Preview").
5.  Set an Automation to run this daily at 4:00 AM.


---

## 🤖 Android Setup

Since Android doesn't have a built-in "Shortcuts" app, you will need a small app to fetch the wallpaper. Here are the three best options (all free).

### Option 1: Remote Wallpaper (Best Open Source)
A tiny, no-nonsense app that does exactly one thing: downloads an image from a URL and sets it as your wallpaper.
* **Download:** [Get the APK here](https://github.com/cssnr/remote-wallpaper-android/releases)
* **Setup:**
  1. Open the app.
  2. **Remote URL:** Paste your Raw GitHub Link (ending in `.png`).
  3. **Interval:** Set to `24 Hours`.
  4. Tap **Start**.

### Option 2: Muzei (Best for Aesthetics)
A polished "Live Wallpaper" app that creates a nice blur/dim effect behind your icons.
* **Download:** [Play Store](https://play.google.com/store/apps/details?id=net.nurik.roman.muzei) or [F-Droid](https://f-droid.org/en/packages/net.nurik.roman.muzei/)
* **Setup:**
  1. Install **Muzei** + the **"With Others"** plugin (or any URL plugin).
  2. Open Muzei and set it as your wallpaper.
  3. Tap **Sources** -> **With Others**.
  4. Paste your Raw GitHub Link.
  5. Set Update Interval to `24h`.

### Option 3: MacroDroid (For Power Users)
If you want complex logic (e.g., randomizing between Life/Year views), use this automation tool.
* **Download:** [Play Store](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid)
* **Setup:**
  1. Create a macro with a **Daily Timer** trigger (e.g., 4:00 AM).
  2. Add Action: **HTTP Request** (GET) -> Paste your URL -> Save to file `wallpaper.png`.
  3. Add Action: **Set Wallpaper** -> Select that file.

### Option
