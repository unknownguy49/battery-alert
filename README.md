# Battery Alert

**Battery Alert** is a lightweight Windows utility that displays a popup window when your laptop battery reaches 100%, prompting you to disconnect the charger and extend your battery life.


## Features

- Native Windows-style popup using MessageBox
- Monitors battery percentage in background
- Easy setup and auto-start on boot


## Folder Structure

```
project-root/
├── battery_notify.py       # Main script (Windows only)
├── battery_notify.spec     # PyInstaller spec file
├── build/                  # Auto-generated build files
└── dist/                   # Contains battery_notify.exe (final output)
```


## How to Use

1. Download `battery_notify.exe` from the `dist/` folder.
2. Press `Win + R`, type `shell:startup`, hit Enter.
3. Copy `battery_notify.exe` into the folder that opens.
4. Done! The popup will appear when your battery hits 100% and is plugged in.

---