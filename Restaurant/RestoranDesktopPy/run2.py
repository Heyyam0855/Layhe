"""
Restoran İdarə Etmə Sistemi
Ana proqram faylı
"""

import tkinter as tk  # GUI (Qrafik interfeys) yaratmaq üçün Python kitabxanası
from tkinter import messagebox  # Xəta və ya məlumat mesajlarını göstərmək üçün modul
import sys  # Sistem ilə əlaqəli funksiyalar üçün modul (məs: komanda sətri, yol ayarları)
import os  # Fayl sistemində əməliyyatlar aparmaq üçün modul (məs: fayl yolları)

# Proyekt yolunu əlavə et
current_dir = os.path.dirname(os.path.abspath(__file__))  
# __file__ → cari faylın yolunu verir
# abspath() → tam yolu alır (absolute path)
# dirname() → həmin yolun yalnız qovluq hissəsini çıxarır
sys.path.insert(0, current_dir)  
# Python-a deyirik ki, bu qovluqdan modul axtar, yəni öz layihəmizin kök qovluğu

# Import modulları
from database.db_manager import DatabaseManager  # Verilənlər bazasını idarə edən sinif

class RestaurantApp:  # Restoran tətbiqi üçün əsas sinif
    def __init__(self):  # Bu sinifdən obyekt yaradıldıqda avtomatik işləyən metod (konstruktor)
        self.root = tk.Tk()  # Əsas (ana) pəncərəni yarat
        self.root.title("Restoran İdarə Sistemi")  # Pəncərənin başlığını təyin et
        self.root.geometry("1x1")  # Pəncərənin ölçüsünü minimum 1x1 piksel qoy
        self.root.withdraw()  # Pəncərəni müvəqqəti gizlət
        
        # Verilənlər bazasını başlat
        self.db_manager = DatabaseManager()
        
        # Giriş pəncərəsini aç
        self.show_login()
    
    def show_login(self):  # Giriş pəncərəsini göstərən metod
        """Giriş pəncərəsini göstər"""
        from gui.login import LoginWindow  # Giriş pəncərəsini təyin edən sinifi əlavə et
        self.login_window = LoginWindow(self.root, self.on_login_success)
        # Giriş pəncərəsini yarat, istifadəçi daxil olduqda `on_login_success` funksiyası çağırılacaq
    
    def on_login_success(self, user_data):  # İstifadəçi uğurla daxil olduqda işləyən metod
        """Uğurlu giriş zamanı çağırılan funksiya"""
        self.root.deiconify()  # Əsas pəncərəni yenidən görünən et
        from gui.main_window import MainWindow  # Əsas menyunu idarə edən sinifi əlavə et
        self.main_window = MainWindow(self.root, user_data, self.db_manager)  
        # Ana pəncərəni göstər və istifadəçi məlumatları ilə işləməyə başla
    
    def run(self):  # Tətbiqi işə salmaq üçün metod
        """Proqramı başlat"""
        try:
            self.root.mainloop()  # Tkinter GUI tətbiqini dövri olaraq işlət (təhlükəsiz şəkildə)
        except Exception as e:  # Əgər hər hansı xəta olsa
            messagebox.showerror("Xəta", f"Proqram xətası: {str(e)}")  
            # Xətanı ekranda istifadəçiyə göstər

if __name__ == "__main__":  # Əgər bu fayl birbaşa işə salınırsa
    app = RestaurantApp()  # Tətbiq obyektini yarat
    app.run()  # Tətbiqi işə sal