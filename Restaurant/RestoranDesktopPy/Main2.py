import tkinter as tk   # tkinter modulunu qısaldılmış ad ilə çağırır (GUI üçün)
from tkinter import ttk, messagebox  # ttk (modern widgetlər) və messagebox (mesaj qutuları) modulunu əlavə edir
import math  # Riyazi hesablama funksiyaları üçün
from datetime import datetime  # Tarix və vaxt ilə işləmək üçün

class MainWindow:  # Əsas Pəncərə sinfi
    def __init__(self, root, user_data, db_manager):  # Sinifin başlanğıc metodu (konstruktor)
        self.root = root  # Əsas pəncərə obyekti
        self.user_data = user_data  # İstifadəçi məlumatlarını saxlayır
        self.db_manager = db_manager  # Məlumat bazası idarəedicisini saxlayır
        self.current_panel = 'dashboard'  # Hal-hazırda aktiv panelin adı (ilk olaraq dashboard)

        self.setup_window()  # Pəncərəni ilkin qurmaq üçün metod çağırılır
        self.create_ultra_modern_interface()  # Ultra-modern interfeys yaratmaq üçün metod çağırılır
