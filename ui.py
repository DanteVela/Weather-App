# ui.py: Builds the Tkinter interface, wires up button, and glues in both "weather" and "icons". [all widgets and layout]
# -------------------------------------------------------------------------------------------------------------------------------
# ui.py
import os
import tkinter as tk
import asyncio

from weather import fetch_weather
from icons import IconManager

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("No-API-Key Weather")
        self.geometry("500x300")

        # Load window icon
        icon_dir = os.path.join(os.path.dirname(__file__), "icons")
        # Windows .ico
        ico = os.path.join(icon_dir, "weather.ico")
        if os.path.exists(ico):
            self.iconbitmap(ico)
        # Cross-platform .png
        png = os.path.join(icon_dir, "weather.png")
        if os.path.exists(png):
            img = tk.PhotoImage(file=png)
            self.iconphoto(False, img)
            self._icon_ref = img

        # Inputs
        tk.Label(self, text="State:").pack(pady=(10, 0))
        self.state_entry = tk.Entry(self)
        self.state_entry.pack()

        tk.Label(self, text="City:").pack(pady=(20, 0))
        self.city_entry = tk.Entry(self)
        self.city_entry.pack()

        tk.Button(self, text="Get Weather", command=self.on_click).pack(pady=15)

        # Result display
        self.result = tk.Label(self, text="", wraplength=280)
        self.result.pack()

        # Icon manager
        # icon_dir = os.path.join(os.path.dirname(__file__), "icons")
        self.icon_mgr = IconManager(icon_dir)

        self.icon_label = tk.Label(self, image=self.icon_mgr.default_icon)
        self.icon_label.pack(pady=(10, 20))

    def on_click(self):
        state = self.state_entry.get().strip()
        city = self.city_entry.get().strip()

        if not state or not city:
            self.result.config(text="Please enter both city and state.")
            self.icon_label.config(image=self.icon_mgr.default_icon)
            return

        location = f"{state}, {city}"
        try:
            # Blocks the UI briefly; for production consider asyncio.ensure_future + loop integration
            temp, cond = asyncio.run(fetch_weather(location))
            self.result.config(text=f"{location}: {temp}°F, {cond}")

            icon = self.icon_mgr.pick_icon(cond)
            self.icon_label.config(image=icon)
            self.icon_label.image = icon                                # Prevent Garbage Collection

        except Exception as e:
            self.result.config(text=f"Error: {e}")
            self.icon_label.config(image=self.icon_mgr.default_icon)

if __name__ == "__main__":
    WeatherApp().mainloop()