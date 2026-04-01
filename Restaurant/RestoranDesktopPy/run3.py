"""
HOTELUP – Otel İdarə Etmə Sistemi
Ana proqram faylı
"""

import tkinter as tk  # GUI (qrafik interfeys) üçün modul
from tkinter import messagebox  # Mesaj qutuları göstərmək üçün
import sys
import os

# Layihə qovluğunu sistem yoluna əlavə et
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Verilənlər bazası modulu
from database.db_manager import DatabaseManager  # Otelə aid DB sinifi

class HotelApp:  # Otel idarəetmə tətbiqinin əsas sinifi
    def __init__(self):
        self.root = tk.Tk()  # Ana pəncərə
        self.root.title("HOTELUP – Otel İdarə Sistemi")  # Pəncərə başlığı
        self.root.geometry("1x1")  # Minimum ölçüdə başlasın
        self.root.withdraw()  # Pəncərəni gizlət

        # Verilənlər bazasını işə sal
        self.db_manager = DatabaseManager()

        # Giriş pəncərəsini göstər
        self.show_login()

    def show_login(self):
        """Giriş pəncərəsini göstər"""
        from gui.login import LoginWindow  # Giriş pəncərəsi
        self.login_window = LoginWindow(self.root, self.on_login_success)

    def on_login_success(self, user_data):
        """Uğurlu giriş zamanı əsas paneli aç"""
        self.root.deiconify()  # Gizli pəncərəni göstər
        from gui.main_window import MainWindow  # Əsas idarə paneli
        self.main_window = MainWindow(self.root, user_data, self.db_manager)

    def run(self):
        """Proqramı işə sal"""
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Xəta", f"Proqramda xəta baş verdi: {str(e)}")

# Əgər birbaşa bu fayl işə düşürsə, tətbiqi başlat
if __name__ == "__main__":
    app = HotelApp()
    app.run()
