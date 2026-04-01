# Personal Task Manager & Notes
# Tkinter Desktop Application

"""
Ana başlanğıc faylı - Tətbiqi işə salır
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Layihə path-ini əlavə etmək
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow
from config.database import DatabaseManager

def main():
    """Ana funksiya - tətbiqi başladır"""
    try:
        # Verilənlər bazasını yoxlamaq və yaratmaq
        db_manager = DatabaseManager()
        db_manager.initialize_database()
        
        # Tkinter root window yaratmaq
        root = tk.Tk()
        
        # Ana tətbiq pəncərəsini yaratmaq
        app = MainWindow(root)
        
        # Event loop başlatmaq
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Error", f"Tətbiq başladılarkən xəta baş verdi:\n{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()