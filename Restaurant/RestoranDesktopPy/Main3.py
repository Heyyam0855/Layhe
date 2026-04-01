import tkinter as tk  # Tkinter kitabxanasını 'tk' adı ilə yükləyirik (qrafik interfeys üçün)
from tkinter import messagebox  # Tkinter içindən 'messagebox' modulunu gətiririk (mesaj pəncərələri üçün)
import sys  # Sistem əmrlərinə və Python mühitinə çıxış üçün modul
import os  # Əməliyyat sistemi ilə işləmək üçün modul

# Proyekt yolunu əlavə et
current_dir = os.path.dirname(os.path.abspath(__file__))  # Hazırda işləyən faylın tam yolunu müəyyən edir
sys.path.insert(0, current_dir)  # Mövcud qovluğu Python axtarış yolunun əvvəlinə əlavə edir

# Import modulları
from database.db_manager import DatabaseManager  # Verilənlər bazası idarəetmə modulunu gətirir

class RestaurantApp:  # Restoran idarəetmə tətbiqinin əsas sinfi
    def __init__(self): # Sinif yaradılarkən avtomatik işləyən konstruktor funksiyası
        self.root = tk.Tk()  # Əsas Tkinter pəncərəsini yarad
        self.root.title("Restoran İdarə Sistemi")  # Pəncərənin başlığını təyin et
        self.root.geometry("1x1")  # Minimum ölçünü təyin edir (1x1 piksellik gizli pəncərə)
        self.root.withdraw()  # Ana pəncərəni dərhal gizlədir
        
        # Verilənlər bazasını başlat
        self.db_manager = DatabaseManager()
        
        # Giriş pəncərəsini aç
        self.show_login()
    
# Giriş pəncərəsini açmaq üçün funksiya
    def show_login(self):
        """Giriş pəncərəsini göstər"""
        from gui.login import LoginWindow  # Giriş pəncərəsi modulunu gətirir
        self.login_window = LoginWindow(self.root, self.on_login_success)  # Giriş pəncərəsini açır
    
    def on_login_success(self, user_data):
        """Uğurlu giriş zamanı çağırılan funksiya"""
        # Ana pəncərəni göstər və qur
        self.root.deiconify()  # Gizli pəncərəni yenidən görünən edir
        from gui.main_window import MainWindow  # Əsas pəncərə modulunu gətirir
        self.main_window = MainWindow(self.root, user_data, self.db_manager)  # Əsas pəncərəni işə salır
    
    def run(self):
        """Proqramı başlat"""
        try:
            self.root.mainloop()  # Tkinter hadisələr döngəsini işə salır
        except Exception as e:  # Əgər xəta baş verərsə
            messagebox.showerror("Xəta", f"Proqram xətası: {str(e)}")  # Xəta mesajı göstərir

if __name__ == "__main__":  # Əgər bu fayl birbaşa işə salınırsa
    app = RestaurantApp()  # Tətbiq nümunəsini yarad
    app.run()  # Tətbiqi işə sal
