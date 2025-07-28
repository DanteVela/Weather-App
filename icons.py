# icons.py: Defines your icon rules, loads all images once, and picks the right icon. [icon-matching and loading]
# -------------------------------------------------------------------------------------------------------------------------------
import os
import re
import tkinter as tk
from datetime import datetime

# Each entry is (filename, [keywords], time_of_day)
# time_of_day: "day", "night", or "any"
ICON_PATTERNS = [
    ("PartlyCloudyDay.png",    ["partly", "cloudy"],                "day"),
    ("PartlyCloudyNight.png",  ["partly", "cloudy"],                "night"),
    ("CloudyDay.png",          ["cloud", "overcast"],               "day"),
    ("CloudyNight.png",        ["cloud", "overcast"],               "night"),
    ("ClearSunny.png",         ["clear"],                           "day"),
    ("ClearNight.png",         ["clear"],                           "night"),
    ("ScatteredRainDay.png",   ["drizzle"],                         "day"),
    ("ScatteredRainNight.png", ["drizzle"],                         "night"),
    ("Showers.png",            ["rain"],                            "any"),
    ("StormDay.png",           ["thunder", "hurricane"],            "day"),
    ("StormNight.png",         ["thunder", "hurricane"],            "night"),
    ("Snow.png",               ["snow"],                            "any"),
    ("ScatteredSnowDay.png",   ["snow", "drizzle"],                 "day"),
    ("ScatteredSnowNight.png", ["snow", "drizzle"],                 "night"),
    ("Hail.png",               ["hail"],                            "any"),
    ("Fog.png",                ["fog", "mist", "haze"],             "any"),
    ("Tornado.png",            ["tornado"],                         "any"),
    ("Default.png",            [],                                  "any"),
]

class IconManager:
    def __init__(self, icon_dir: str):
        # preload each PNG into a PhotoImage
        self.icons: dict[str, tk.PhotoImage] = {}
        for fname, _, _ in ICON_PATTERNS:
            self.icons[fname] = tk.PhotoImage(file=os.path.join(icon_dir, fname))
        self.default_icon = self.icons["Default.png"]

    def pick_icon(self, description: str) -> tk.PhotoImage:
        # normalize description
        desc = re.sub(r"[^\w\s]", "", description.lower())
        
        # simple day/night detection by local hour
        hour = datetime.now().hour
        is_day = 6 <= hour < 18

        for fname, keywords, when in ICON_PATTERNS:
            # skip if time_of_day doesn't match
            if when == "day" and not is_day:
                continue
            if when == "night" and is_day:
                continue

            # AND logic: all keywords must be in description
            if all(kw in desc for kw in keywords):
                return self.icons[fname]

        return self.default_icon     