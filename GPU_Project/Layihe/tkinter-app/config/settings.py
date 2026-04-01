# Tətbiq konfiqurasiya parametrləri

"""
Tətbiqin ümumi parametrlərini saxlayır
"""

import os

# Tətbiq məlumatları
APP_NAME = "Personal Task Manager & Notes"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Portfolio Project"

# Pəncərə parametrləri
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
MIN_WINDOW_WIDTH = 800
MIN_WINDOW_HEIGHT = 600

# Rənglər və temalar
THEMES = {
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "select_bg": "#0078d4",
        "select_fg": "#ffffff",
        "accent": "#0078d4",
        "secondary": "#f3f2f1",
        "border": "#d1d1d1"
    },
    "dark": {
        "bg": "#1e1e1e",
        "fg": "#ffffff",
        "select_bg": "#0078d4",
        "select_fg": "#ffffff",
        "accent": "#0078d4",
        "secondary": "#2d2d30",
        "border": "#3e3e42"
    }
}

# Prioritet rəngləri
PRIORITY_COLORS = {
    "high": "#ff4757",
    "medium": "#ffa726",
    "low": "#26a69a"
}

# Status rəngləri
STATUS_COLORS = {
    "pending": "#6c757d",
    "in_progress": "#007bff",
    "completed": "#28a745"
}

# Fayllar və yollar
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
CONFIG_DIR = os.path.join(BASE_DIR, "config")

# Verilənlər bazası
DATABASE_NAME = "app.db"
DATABASE_PATH = os.path.join(DATA_DIR, DATABASE_NAME)

# Backup parametrləri
BACKUP_DIR = os.path.join(DATA_DIR, "backups")
AUTO_BACKUP_INTERVAL = 24  # saat

# Font parametrləri
DEFAULT_FONT_FAMILY = "Segoe UI"
DEFAULT_FONT_SIZE = 10
TITLE_FONT_SIZE = 12
HEADER_FONT_SIZE = 14

# Data formatı
DATE_FORMAT = "%d/%m/%Y"
DATETIME_FORMAT = "%d/%m/%Y %H:%M"

# Kateqoriyalar
DEFAULT_CATEGORIES = [
    {"name": "General", "color": "#6c757d", "type": "both"},
    {"name": "Work", "color": "#007bff", "type": "both"},
    {"name": "Personal", "color": "#28a745", "type": "both"},
    {"name": "Study", "color": "#ffc107", "type": "both"},
    {"name": "Health", "color": "#dc3545", "type": "both"}
]

# Keyboard shortcuts
SHORTCUTS = {
    "new_task": "Ctrl+T",
    "new_note": "Ctrl+N",
    "save": "Ctrl+S",
    "search": "Ctrl+F",
    "settings": "Ctrl+comma",
    "quit": "Ctrl+Q"
}