import customtkinter as ctk
import os
import keyboard
import pystray
from PIL import Image, ImageDraw
from tkinter import messagebox
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class EasyTouch(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EasyTouch Pro")
        self.geometry("260x90")
        self.iconbitmap(default=None)  # Add icon path if needed
        self.resizable(False, False)
        self.expanded = False

        self.toggle_btn = ctk.CTkButton(self, text="▶ Tools Menu", command=self.toggle_dropdown, width=240)
        self.toggle_btn.pack(pady=10)

        self.dropdown_frame = ctk.CTkFrame(self)
        buttons = [
            ("📋 Clipboard", self.open_clipboard),
            ("📷 Screenshot", self.take_screenshot),
            ("🧮 Calculator", self.open_calculator),
            ("📸 Camera", self.open_camera),
            ("📝 Notepad", self.open_notepad),
            ("🗓 Calendar", self.open_calendar),
            ("🔊 Mute / Unmute", self.toggle_mute),
            ("🧹 Clear Temp", self.clear_temp),
            ("⚙️ Task Manager", self.open_task_manager),
            ("🖥 File Explorer", self.open_file_explorer),
            ("📶 Wi-Fi Settings", self.open_wifi_settings),
            ("🔌 Bluetooth", self.open_bluetooth),
            ("⏻ Shutdown", self.shutdown),
            ("🔁 Restart", self.restart),
            ("🔐 Lock Screen", self.lock_screen),
        ]

        self.tool_buttons = []
        for text, command in buttons:
            btn = ctk.CTkButton(self.dropdown_frame, text=text, command=command, width=240)
            btn.pack(pady=2)
            self.tool_buttons.append(btn)

        threading.Thread(target=self.create_tray_icon, daemon=True).start()

    def toggle_dropdown(self):
     if self.expanded:
        self.dropdown_frame.pack_forget()
        self.geometry("260x90")
        self.toggle_btn.configure(text="▶ Tools Menu")
     else:
        self.dropdown_frame.pack(pady=5)
        total_height = 90 + (len(self.tool_buttons) * 30) + 29  
        self.geometry(f"260x{total_height}")
        self.toggle_btn.configure(text="▼ Tools Menu")
     self.expanded = not self.expanded

    def open_clipboard(self):
        keyboard.press_and_release('win+v')

    def take_screenshot(self):
        keyboard.press_and_release('win+shift+s')

    def open_calculator(self):
        os.system("start calc")

    def open_camera(self):
        os.system("start microsoft.windows.camera:")

    def open_notepad(self):
        os.system("start notepad")

    def open_calendar(self):
        os.system("start outlookcal:")

    def toggle_mute(self):
        keyboard.press_and_release("volume_mute")

    def clear_temp(self):
        os.system("del /q/f/s %TEMP%\\*")

    def open_task_manager(self):
        os.system("start taskmgr")

    def open_file_explorer(self):
        os.system("explorer")

    def open_wifi_settings(self):
        os.system("start ms-settings:network-wifi")

    def open_bluetooth(self):
        os.system("start ms-settings:bluetooth")

    def shutdown(self):
     if messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown?"):
        os.system("shutdown /s /t 1")

    def restart(self):
     if messagebox.askyesno("Confirm Restart", "Are you sure you want to restart?"):
        os.system("shutdown /r /t 1")


    def lock_screen(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")

    # ================ Tray Icon ================
    def create_tray_icon(self):
        icon_image = Image.new('RGB', (64, 64), "green")
        draw = ImageDraw.Draw(icon_image)
        draw.rectangle((20, 20, 44, 44), fill="white")

        def on_quit(icon, item):
            icon.stop()
            self.destroy()

        def on_show(icon, item):
            self.after(0, self.deiconify)

        menu = pystray.Menu(
            pystray.MenuItem("Show", on_show),
            pystray.MenuItem("Exit", on_quit)
        )
        icon = pystray.Icon("EasyTouch", icon_image, "EasyTouch Pro", menu)
        icon.run()


if __name__ == "__main__":
    app = EasyTouch()
    app.mainloop()
