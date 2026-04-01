"""
Ana pəncərə - Ultra modern Dashboard dizayn
Fluent Design və Material Design prinsipləri ilə
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
from datetime import datetime

class MainWindow:
    def __init__(self, root, user_data, db_manager):
        self.root = root
        self.user_data = user_data
        self.db_manager = db_manager
        self.current_panel = 'dashboard'
        
        self.setup_window()
        self.create_ultra_modern_interface()
        
    def setup_window(self):
        """Ana pəncərəni qur"""
        self.root.title("Restoran İdarə Sistemi")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 572)
        self.root.configure(bg='#f8f9fa')
        
        # Modern ikon
        try:
            self.root.iconbitmap(default='icon.ico')
        except:
            pass
        
        # Mərkəzləşdir
        self.center_window()
        
        # Modern stillər
        self.setup_ultra_modern_styles()
        
        # Bağlanma hadisəsi
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def center_window(self):
        """Pəncərəni mərkəzləşdir"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - 1600) // 2
        y = (screen_height - 900) // 2
        self.root.geometry(f"1600x900+{x}+{y}")
    
    def setup_ultra_modern_styles(self):
        """Ultra modern stil sistemi"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Modern card stili
        style.configure(
            "Card.TFrame",
            background="white",
            relief="flat",
            borderwidth=0
        )
        
        # Sidebar düymələri
        style.configure(
            "Sidebar.TButton",
            font=("Segoe UI", 11),
            padding=(25, 18),
            background="#2c3e50",
            foreground="white",
            borderwidth=0,
            focuscolor="none"
        )
        
        style.map(
            "Sidebar.TButton",
            background=[('active', '#34495e'), ('pressed', '#1abc9c')]
        )
        
        # Aktiv düymə
        style.configure(
            "Active.TButton",
            font=("Segoe UI", 11, "bold"),
            padding=(25, 18),
            background="#1abc9c",
            foreground="white",
            borderwidth=0
        )
    
    def create_ultra_modern_interface(self):
        """Ultra modern interfeys yarad"""
        # Ana konteyner
        main_container = tk.Frame(self.root, bg='#ecf0f1')
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Top Navigation Bar
        self.create_top_navigation(main_container)
        
        # Body Container
        body_container = tk.Frame(main_container, bg='#ecf0f1')
        body_container.pack(fill=tk.BOTH, expand=True)
        
        # Left Sidebar
        self.create_modern_sidebar(body_container)
        
        # Main Content Area
        self.create_content_area(body_container)
        
        # Initialize with dashboard
        self.show_dashboard()
    
    def create_top_navigation(self, parent):
        """Modern üst navigasiya"""
        nav_container = tk.Frame(parent, bg='white', height=80)
        nav_container.pack(fill=tk.X)
        nav_container.pack_propagate(False)
        
        # Sol tərəf - Brand
        left_nav = tk.Frame(nav_container, bg='white')
        left_nav.pack(side=tk.LEFT, fill=tk.Y, padx=30)
        
        # Logo və brand
        brand_frame = tk.Frame(left_nav, bg='white')
        brand_frame.pack(side=tk.LEFT, pady=20)
        
        logo_label = tk.Label(
            brand_frame,
            text="🍽️",
            font=("Segoe UI Emoji", 24),
            bg='white',
            fg='#2c3e50'
        )
        logo_label.pack(side=tk.LEFT, padx=(0, 10))
        
        brand_label = tk.Label(
            brand_frame,
            text="RESTORAN İDARƏ",
            font=("Segoe UI", 18, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        brand_label.pack(side=tk.LEFT)
        
        # Sağ tərəf - İstifadəçi məlumatı və vaxt
        right_nav = tk.Frame(nav_container, bg='white')
        right_nav.pack(side=tk.RIGHT, fill=tk.Y, padx=30)
        
        # Vaxt göstərici
        time_frame = tk.Frame(right_nav, bg='white')
        time_frame.pack(side=tk.RIGHT, pady=20, padx=(0, 30))
        
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %b %Y")
        
        time_label = tk.Label(
            time_frame,
            text=current_time,
            font=("Segoe UI", 16, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        time_label.pack()
        
        date_label = tk.Label(
            time_frame,
            text=current_date,
            font=("Segoe UI", 10),
            bg='white',
            fg='#7f8c8d'
        )
        date_label.pack()
        
        # İstifadəçi məlumatı
        user_frame = tk.Frame(right_nav, bg='#3498db', relief='flat')
        user_frame.pack(side=tk.RIGHT, pady=15, padx=(0, 20))
        
        user_icon = tk.Label(
            user_frame,
            text="👤",
            font=("Segoe UI Emoji", 16),
            bg='#3498db',
            fg='white'
        )
        user_icon.pack(side=tk.LEFT, padx=(15, 5), pady=10)
        
        user_info = tk.Label(
            user_frame,
            text=f"{self.user_data['username']}\\n{self.user_data['role'].title()}",
            font=("Segoe UI", 10, "bold"),
            bg='#3498db',
            fg='white',
            justify=tk.LEFT
        )
        user_info.pack(side=tk.LEFT, padx=(0, 15), pady=10)
        
        # Alt ayırıcı xətt
        separator = tk.Frame(nav_container, bg='#bdc3c7', height=1)
        separator.pack(fill=tk.X, side=tk.BOTTOM)
    
    def create_modern_sidebar(self, parent):
        """Ultra modern sidebar"""
        self.sidebar = tk.Frame(parent, bg='#2c3e50', width=280)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        # Sidebar başlığı
        sidebar_header = tk.Frame(self.sidebar, bg='#2c3e50')
        sidebar_header.pack(fill=tk.X, pady=(30, 20))
        
        header_label = tk.Label(
            sidebar_header,
            text="MODULLAR",
            font=("Segoe UI", 12, "bold"),
            bg='#2c3e50',
            fg='#95a5a6'
        )
        header_label.pack()
        
        # Menu düymələri
        self.menu_buttons = {}
        menu_items = [
            ("dashboard", "📊", "Ana Səhifə", True),
            ("orders", "📋", "Sifarişlər", False),
            ("tables", "🪑", "Masalar", False),
            ("customers", "👥", "Müştərilər", False),
            ("menu", "🍽️", "Menyu", False),
            ("reservations", "📅", "Rezervasiyalar", False),
        ]
        
        if self.user_data['role'] == 'admin':
            menu_items.extend([
                ("separator", "", "", False),
                ("reports", "📈", "Hesabatlar", False),
                ("settings", "⚙️", "Tənzimləmələr", False)
            ])
        
        for item_id, icon, text, is_active in menu_items:
            if item_id == "separator":
                # Ayırıcı
                sep_frame = tk.Frame(self.sidebar, bg='#34495e', height=1)
                sep_frame.pack(fill=tk.X, padx=20, pady=15)
                continue
            
            self.create_sidebar_button(item_id, icon, text, is_active)
        
        # Alt hissə - Çıxış
        logout_frame = tk.Frame(self.sidebar, bg='#2c3e50')
        logout_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=30)
        
        logout_btn = tk.Button(
            logout_frame,
            text="🚪  Çıxış",
            font=("Segoe UI", 11, "bold"),
            bg='#e74c3c',
            fg='white',
            bd=0,
            padx=25,
            pady=18,
            cursor='hand2',
            command=self.on_close
        )
        logout_btn.pack(fill=tk.X, padx=20)
        
        # Hover effect
        logout_btn.bind('<Enter>', lambda e: logout_btn.configure(bg='#c0392b'))
        logout_btn.bind('<Leave>', lambda e: logout_btn.configure(bg='#e74c3c'))
    
    def create_sidebar_button(self, item_id, icon, text, is_active):
        """Sidebar düyməsi yarat"""
        bg_color = '#1abc9c' if is_active else '#2c3e50'
        
        btn = tk.Button(
            self.sidebar,
            text=f"{icon}  {text}",
            font=("Segoe UI", 11, "bold" if is_active else "normal"),
            bg=bg_color,
            fg='white',
            bd=0,
            padx=25,
            pady=18,
            anchor='w',
            cursor='hand2',
            command=lambda: self.switch_panel(item_id)
        )
        btn.pack(fill=tk.X, padx=15, pady=3)
        
        # Hover effects
        if not is_active:
            btn.bind('<Enter>', lambda e: btn.configure(bg='#34495e'))
            btn.bind('<Leave>', lambda e: btn.configure(bg='#2c3e50'))
        
        self.menu_buttons[item_id] = btn
    
    def create_content_area(self, parent):
        """Məzmun sahəsi"""
        # Content container
        self.content_area = tk.Frame(parent, bg='#ecf0f1')
        self.content_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Content frame
        self.content_frame = tk.Frame(self.content_area, bg='#ecf0f1')
        self.content_frame.pack(fill=tk.BOTH, expand=True)
    
    def switch_panel(self, panel_name):
        """Panel dəyişdir"""
        if panel_name == self.current_panel:
            return
        
        # Düymə stilini yenilə
        for name, button in self.menu_buttons.items():
            if name == panel_name:
                button.configure(bg='#1abc9c', font=("Segoe UI", 11, "bold"))
                button.unbind('<Enter>')
                button.unbind('<Leave>')
            else:
                button.configure(bg='#2c3e50', font=("Segoe UI", 11, "normal"))
                button.bind('<Enter>', lambda e, b=button: b.configure(bg='#34495e'))
                button.bind('<Leave>', lambda e, b=button: b.configure(bg='#2c3e50'))
        
        self.current_panel = panel_name
        
        # Məzmunu dəyişdir
        if panel_name == 'dashboard':
            self.show_dashboard()
        elif panel_name == 'orders':
            self.show_orders()
        elif panel_name == 'tables':
            self.show_tables()
        elif panel_name == 'customers':
            self.show_customers()
        elif panel_name == 'menu':
            self.show_menu()
        elif panel_name == 'reservations':
            self.show_reservations()
        elif panel_name == 'reports':
            self.show_reports()
        elif panel_name == 'settings':
            self.show_settings()
    
    def clear_content(self):
        """Məzmunu təmizlə"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_dashboard(self):
        """Ultra modern dashboard"""
        self.clear_content()
        
        # Page header
        header_frame = tk.Frame(self.content_frame, bg='#ecf0f1')
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        page_title = tk.Label(
            header_frame,
            text="📊 Ana Səhifə",
            font=("Segoe UI", 28, "bold"),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        page_title.pack(anchor=tk.W)
        
        page_subtitle = tk.Label(
            header_frame,
            text="Restoran fəaliyyətinin ümumi görünüşü və canlı statistikalar",
            font=("Segoe UI", 14),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        page_subtitle.pack(anchor=tk.W, pady=(5, 0))
        
        # Statistics Cards Row
        stats_container = tk.Frame(self.content_frame, bg='#ecf0f1')
        stats_container.pack(fill=tk.X, pady=(0, 30))
        
        # Create 4 modern stat cards
        stats_data = [
            ("Günlük Sifarişlər", "24", "+12%", "#e74c3c", "📋"),
            ("Aktiv Masalar", "8/12", "67%", "#3498db", "🪑"),
            ("Günlük Gəlir", "1,250 ₼", "+8%", "#27ae60", "💰"),
            ("Rezervasiyalar", "6", "Bu gün", "#f39c12", "📅")
        ]
        
        for i, (title, value, change, color, icon) in enumerate(stats_data):
            self.create_modern_stat_card(stats_container, title, value, change, color, icon, i)
        
        # Charts and Activity Row
        bottom_container = tk.Frame(self.content_frame, bg='#ecf0f1')
        bottom_container.pack(fill=tk.BOTH, expand=True)
        
        # Left side - Recent Activity
        activity_card = self.create_card(bottom_container, "Son Fəaliyyətlər")
        activity_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        activities = [
            ("🍽️", "Masa 5 - Yeni sifariş", "2 dəqiqə əvvəl", "#3498db"),
            ("💰", "Masa 3 - Ödəmə tamamlandı", "5 dəqiqə əvvəl", "#27ae60"),
            ("📅", "Sabah 19:00 - Rezervasiya", "15 dəqiqə əvvəl", "#f39c12"),
            ("👥", "Yeni müştəri qeydiyyatı", "20 dəqiqə əvvəl", "#9b59b6"),
            ("🪑", "Masa 7 - Təmizləmə", "25 dəqiqə əvvəl", "#e74c3c")
        ]
        
        for icon, text, time, color in activities:
            self.create_activity_item(activity_card, icon, text, time, color)
        
        # Right side - Quick Actions
        actions_card = self.create_card(bottom_container, "Tez Əməliyyatlar")
        actions_card.pack(side=tk.RIGHT, fill=tk.Y, padx=(15, 0))
        
        quick_actions = [
            ("📋", "Yeni Sifariş", "#3498db", lambda: self.switch_panel('orders')),
            ("🪑", "Masa Bax", "#27ae60", lambda: self.switch_panel('tables')),
            ("👥", "Müştəri Əlavə Et", "#f39c12", lambda: self.switch_panel('customers')),
            ("📅", "Rezervasiya Yarat", "#9b59b6", lambda: self.switch_panel('reservations'))
        ]
        
        for icon, text, color, command in quick_actions:
            self.create_action_button(actions_card, icon, text, color, command)
    
    def create_modern_stat_card(self, parent, title, value, change, color, icon, index):
        """Modern statistika kartı"""
        card = tk.Frame(parent, bg='white', relief='flat', bd=0)
        card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10 if index > 0 else 0)
        
        # Card shadow effect (simulated)
        shadow = tk.Frame(card, bg='#d5dbdb', height=2)
        shadow.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Card content
        content = tk.Frame(card, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        # Top row - Icon and change
        top_row = tk.Frame(content, bg='white')
        top_row.pack(fill=tk.X, pady=(0, 15))
        
        icon_label = tk.Label(
            top_row,
            text=icon,
            font=("Segoe UI Emoji", 24),
            bg='white',
            fg=color
        )
        icon_label.pack(side=tk.LEFT)
        
        change_label = tk.Label(
            top_row,
            text=change,
            font=("Segoe UI", 10, "bold"),
            bg='white',
            fg='#27ae60' if '+' in change else '#7f8c8d'
        )
        change_label.pack(side=tk.RIGHT)
        
        # Value
        value_label = tk.Label(
            content,
            text=value,
            font=("Segoe UI", 24, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        value_label.pack(anchor=tk.W)
        
        # Title
        title_label = tk.Label(
            content,
            text=title,
            font=("Segoe UI", 12),
            bg='white',
            fg='#7f8c8d'
        )
        title_label.pack(anchor=tk.W, pady=(5, 0))
    
    def create_card(self, parent, title):
        """Ümumi kart yarad"""
        card = tk.Frame(parent, bg='white', relief='flat', bd=0)
        
        # Card shadow
        shadow = tk.Frame(card, bg='#d5dbdb', height=2)
        shadow.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Card header
        header = tk.Frame(card, bg='white')
        header.pack(fill=tk.X, padx=25, pady=(25, 15))
        
        title_label = tk.Label(
            header,
            text=title,
            font=("Segoe UI", 16, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        title_label.pack(anchor=tk.W)
        
        # Card content area
        content = tk.Frame(card, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=25, pady=(0, 25))
        
        return content
    
    def create_activity_item(self, parent, icon, text, time, color):
        """Fəaliyyət elementi"""
        item_frame = tk.Frame(parent, bg='white')
        item_frame.pack(fill=tk.X, pady=5)
        
        # Icon
        icon_frame = tk.Frame(item_frame, bg=color, width=40, height=40)
        icon_frame.pack(side=tk.LEFT, padx=(0, 15))
        icon_frame.pack_propagate(False)
        
        icon_label = tk.Label(
            icon_frame,
            text=icon,
            font=("Segoe UI Emoji", 16),
            bg=color,
            fg='white'
        )
        icon_label.pack(expand=True)
        
        # Text content
        text_frame = tk.Frame(item_frame, bg='white')
        text_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        text_label = tk.Label(
            text_frame,
            text=text,
            font=("Segoe UI", 11, "bold"),
            bg='white',
            fg='#2c3e50',
            anchor='w'
        )
        text_label.pack(anchor=tk.W)
        
        time_label = tk.Label(
            text_frame,
            text=time,
            font=("Segoe UI", 9),
            bg='white',
            fg='#7f8c8d',
            anchor='w'
        )
        time_label.pack(anchor=tk.W)
    
    def create_action_button(self, parent, icon, text, color, command):
        """Tez əməliyyat düyməsi"""
        btn_frame = tk.Frame(parent, bg=color, cursor='hand2')
        btn_frame.pack(fill=tk.X, pady=8)
        
        btn_content = tk.Frame(btn_frame, bg=color)
        btn_content.pack(fill=tk.X, padx=20, pady=15)
        
        icon_label = tk.Label(
            btn_content,
            text=icon,
            font=("Segoe UI Emoji", 16),
            bg=color,
            fg='white'
        )
        icon_label.pack(side=tk.LEFT, padx=(0, 10))
        
        text_label = tk.Label(
            btn_content,
            text=text,
            font=("Segoe UI", 11, "bold"),
            bg=color,
            fg='white'
        )
        text_label.pack(side=tk.LEFT)
        
        # Click event
        btn_frame.bind('<Button-1>', lambda e: command())
        btn_content.bind('<Button-1>', lambda e: command())
        icon_label.bind('<Button-1>', lambda e: command())
        text_label.bind('<Button-1>', lambda e: command())
        
        # Hover effect
        def on_enter(e):
            # Darken color
            darker_colors = {
                '#3498db': '#2980b9',
                '#27ae60': '#229954',
                '#f39c12': '#e67e22',
                '#9b59b6': '#8e44ad'
            }
            darker = darker_colors.get(color, color)
            btn_frame.configure(bg=darker)
            btn_content.configure(bg=darker)
            icon_label.configure(bg=darker)
            text_label.configure(bg=darker)
        
        def on_leave(e):
            btn_frame.configure(bg=color)
            btn_content.configure(bg=color)
            icon_label.configure(bg=color)
            text_label.configure(bg=color)
        
        btn_frame.bind('<Enter>', on_enter)
        btn_frame.bind('<Leave>', on_leave)
    
    # Digər panel metodları
    def show_orders(self):
        self.show_coming_soon("Sifarişlər Modulu", "📋")
    
    def show_tables(self):
        self.show_coming_soon("Masalar Modulu", "🪑")
    
    def show_customers(self):
        self.show_coming_soon("Müştərilər Modulu", "👥")
    
    def show_menu(self):
        self.show_coming_soon("Menyu Modulu", "🍽️")
    
    def show_reservations(self):
        self.show_coming_soon("Rezervasiyalar Modulu", "📅")
    
    def show_reports(self):
        self.show_coming_soon("Hesabatlar Modulu", "📈")
    
    def show_settings(self):
        self.show_coming_soon("Tənzimləmələr Modulu", "⚙️")
    
    def show_coming_soon(self, title, icon):
        """Gələcək funksionallıq səhifəsi"""
        self.clear_content()
        
        container = tk.Frame(self.content_frame, bg='#ecf0f1')
        container.pack(expand=True)
        
        icon_label = tk.Label(
            container,
            text=icon,
            font=("Segoe UI Emoji", 64),
            bg='#ecf0f1',
            fg='#bdc3c7'
        )
        icon_label.pack(pady=(50, 20))
        
        title_label = tk.Label(
            container,
            text=title,
            font=("Segoe UI", 24, "bold"),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        title_label.pack(pady=(0, 10))
        
        desc_label = tk.Label(
            container,
            text="Bu modul hazırlanır. Tezliklə əlavə ediləcək.",
            font=("Segoe UI", 14),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        desc_label.pack()
        
        # Geri qayıt düyməsi
        back_btn = tk.Button(
            container,
            text="📊 Ana Səhifəyə Qayıt",
            font=("Segoe UI", 12, "bold"),
            bg='#3498db',
            fg='white',
            bd=0,
            padx=30,
            pady=15,
            cursor='hand2',
            command=lambda: self.switch_panel('dashboard')
        )
        back_btn.pack(pady=30)
        
        # Hover effect
        back_btn.bind('<Enter>', lambda e: back_btn.configure(bg='#2980b9'))
        back_btn.bind('<Leave>', lambda e: back_btn.configure(bg='#3498db'))
    
    def on_close(self):
        """Proqramdan çıxış"""
        result = messagebox.askyesno(
            "Çıxış Təsdiqi",
            "Proqramdan çıxmaq istədiyinizdən əminsiniz?",
            parent=self.root
        )
        if result:
            self.root.quit()
