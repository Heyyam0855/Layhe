"""
Restoran İdarə Etmə Sistemi
Ana proqram faylı
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Proyekt yolunu əlavə et
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import modulları
from database.db_manager import DatabaseManager

class RestaurantApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restoran İdarə Sistemi")
        self.root.geometry("1x1")  # Minimum ölçü
        self.root.withdraw()  # Ana pəncərəni gizlə
        
        # Verilənlər bazasını başlat
        self.db_manager = DatabaseManager()
        
        # Giriş pəncərəsini aç
        self.show_login()
    
    def show_login(self):
        """Giriş pəncərəsini göstər"""
        from gui.login import LoginWindow
        self.login_window = LoginWindow(self.root, self.on_login_success)
    
    def on_login_success(self, user_data):
        """Uğurlu giriş zamanı çağırılan funksiya"""
        # Ana pəncərəni göstər və qur
        self.root.deiconify()
        from gui.main_window import MainWindow
        self.main_window = MainWindow(self.root, user_data, self.db_manager)
    
    def run(self):
        """Proqramı başlat"""
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Xəta", f"Proqram xətası: {str(e)}")

if __name__ == "__main__":
    app = RestaurantApp()
    app.run()
