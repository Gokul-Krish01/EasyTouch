# EasyTouch Pro 🖱️

EasyTouch Pro is a lightweight Python desktop tool that gives quick access to essential system functions like Clipboard, Screenshot, Notepad, Camera, Task Manager, and more—all in one window with system tray support.

---

## 🛠️ Features

- Toggle Tools Menu UI (built with `customtkinter`)
- System shortcuts: Clipboard, Screenshot, Mute, Lock Screen, etc.
- Launch apps: Calculator, Notepad, Camera, Calendar
- System commands: Shutdown, Restart, Clear Temp
- System tray icon support via `pystray`

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install customtkinter keyboard pystray pillow

To Convert python script into EXE file
pyinstaller --onefile --windowed EasyTouch.py
