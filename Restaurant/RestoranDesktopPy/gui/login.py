"""
Giriş pəncərəsi - Ultra modern dizayn
"""

import tkinter as tk
from tkinter import ttk, messagebox

class LoginWindow:
    def __init__(self, parent, success_callback):
        self.parent = parent
        self.success_callback = success_callback
        
        # Ana pəncərə
        self.login_window = tk.Tk()
        self.login_window.title("Restoran İdarə Sistemi - Giriş")
        self.login_window.geometry("500x700")
        self.login_window.resizable(False, False)
        self.login_window.configure(bg='#e8f4fd')
        
        # Pəncərəni mərkəzləşdir
        self.center_window()
        
        # İnterfeys yarat
        self.create_interface()
        
        # İlk fokus
        self.username_entry.focus()
        
        # Enter düyməsi ilə giriş
        self.login_window.bind('<Return>', lambda e: self.authenticate())
        
        # Bağlanma hadisəsi
        self.login_window.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def center_window(self):
        """Pəncərəni mərkəzləşdir"""
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()
        
        x = (screen_width - 500) // 2
        y = (screen_height - 700) // 2
        self.login_window.geometry(f"500x700+{x}+{y}")
    
    def create_interface(self):
        """Modern interfeys yarat"""
        # Ana konteyner
        main_container = tk.Frame(self.login_window, bg='#e8f4fd')
        main_container.pack(fill=tk.BOTH, expand=True, padx=40, pady=50)
        
        # Logo və başlıq
        logo_frame = tk.Frame(main_container, bg='#e8f4fd')
        logo_frame.pack(pady=(0, 40))
        
        logo_label = tk.Label(
            logo_frame,
            text="🍽️",
            font=("Segoe UI Emoji", 48),
            bg='#e8f4fd',
            fg='#007bff'
        )
        logo_label.pack()
        
        title_label = tk.Label(
            logo_frame,
            text="RESTORAN İDARƏ SİSTEMİ",
            font=("Segoe UI", 18, "bold"),
            bg='#e8f4fd',
            fg='#2c3e50'
        )
        title_label.pack(pady=(10, 5))
        
        subtitle_label = tk.Label(
            logo_frame,
            text="Daxil olmaq üçün istifadəçi adı və parol daxil edin",
            font=("Segoe UI", 11),
            bg='#e8f4fd',
            fg='#6c757d'
        )
        subtitle_label.pack()
        
        # Giriş formu
        form_frame = tk.Frame(main_container, bg='white', relief='solid', bd=1)
        form_frame.pack(fill=tk.X, pady=(0, 30))
        
        # Kart kölgəsi effekti
        shadow_frame = tk.Frame(main_container, bg='#dee2e6', height=2)
        shadow_frame.pack(fill=tk.X, pady=(0, 28))
        
        # İçərik konteyner
        content_frame = tk.Frame(form_frame, bg='white')
        content_frame.pack(fill=tk.X, padx=30, pady=30)
        
        # İstifadəçi adı
        username_label = tk.Label(
            content_frame,
            text="İstifadəçi adı",
            font=("Segoe UI", 11, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        username_label.pack(anchor=tk.W, pady=(0, 8))
        
        # İstifadəçi adı input konteyner
        username_container = tk.Frame(content_frame, bg='#f8f9fa', relief='solid', bd=1)
        username_container.pack(fill=tk.X, ipady=2)
        
        # Sol padding üçün boş space
        username_padding = tk.Label(username_container, text="  ", bg='#f8f9fa', font=("Segoe UI", 12))
        username_padding.pack(side=tk.LEFT)
        
        self.username_entry = tk.Entry(
            username_container,
            font=("Segoe UI", 12),
            bg='#f8f9fa',
            fg='#2c3e50',
            relief='flat',
            bd=0,
            highlightthickness=0,
            insertbackground='#2c3e50'
        )
        self.username_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=10)
        
        # Fokus effektləri
        def username_focus_in(e):
            username_container.configure(relief='solid', bd=2, bg='#ffffff')
            username_padding.configure(bg='#ffffff')
            self.username_entry.configure(bg='#ffffff')
        
        def username_focus_out(e):
            username_container.configure(relief='solid', bd=1, bg='#f8f9fa')
            username_padding.configure(bg='#f8f9fa')
            self.username_entry.configure(bg='#f8f9fa')
        
        self.username_entry.bind('<FocusIn>', username_focus_in)
        self.username_entry.bind('<FocusOut>', username_focus_out)
        
        # Parol
        password_label = tk.Label(
            content_frame,
            text="Parol",
            font=("Segoe UI", 11, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        password_label.pack(anchor=tk.W, pady=(25, 8))
        
        # Parol input konteyner
        password_container = tk.Frame(content_frame, bg='#f8f9fa', relief='solid', bd=1)
        password_container.pack(fill=tk.X, ipady=2)
        
        # Sol padding üçün boş space
        password_padding = tk.Label(password_container, text="  ", bg='#f8f9fa', font=("Segoe UI", 12))
        password_padding.pack(side=tk.LEFT)
        
        self.password_entry = tk.Entry(
            password_container,
            font=("Segoe UI", 12),
            bg='#f8f9fa',
            fg='#2c3e50',
            relief='flat',
            bd=0,
            show='*',
            highlightthickness=0,
            insertbackground='#2c3e50'
        )
        self.password_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=10)
        
        # Fokus effektləri
        def password_focus_in(e):
            password_container.configure(relief='solid', bd=2, bg='#ffffff')
            password_padding.configure(bg='#ffffff')
            self.password_entry.configure(bg='#ffffff')
        
        def password_focus_out(e):
            password_container.configure(relief='solid', bd=1, bg='#f8f9fa')
            password_padding.configure(bg='#f8f9fa')
            self.password_entry.configure(bg='#f8f9fa')
        
        self.password_entry.bind('<FocusIn>', password_focus_in)
        self.password_entry.bind('<FocusOut>', password_focus_out)
        
        # Giriş düyməsi - cox sadə
        button_space = tk.Frame(content_frame, bg='white', height=30)
        button_space.pack(fill=tk.X)
        
        # Sadə düymə
        self.login_button = tk.Button(
            content_frame,
            text="DAXİL OL",
            font=("Segoe UI", 12, "bold"),
            bg='#28a745',
            fg='white',
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.authenticate
        )
        self.login_button.pack(fill=tk.X, pady=10, ipady=12)
        
        # Demo hesablar
        demo_frame = tk.Frame(main_container, bg='#e8f4fd')
        demo_frame.pack(fill=tk.X, pady=(20, 0))
        
        demo_title = tk.Label(
            demo_frame,
            text="Demo Hesablar:",
            font=("Segoe UI", 10, "bold"),
            bg='#e8f4fd',
            fg='#495057'
        )
        demo_title.pack()
        
        demo_info = tk.Label(
            demo_frame,
            text="Admin: admin / admin123\nOfisiant: ofisiant / 123",
            font=("Segoe UI", 9),
            bg='#e8f4fd',
            fg='#6c757d',
            justify=tk.CENTER
        )
        demo_info.pack(pady=(5, 0))
    
    def authenticate(self):
        """İstifadəçi doğrulama"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            self.show_error("Bütün sahələri doldurun!")
            return
        
        # Demo istifadəçilər
        demo_users = {
            'admin': {'password': 'admin123', 'role': 'admin'},
            'ofisiant': {'password': '123', 'role': 'waiter'}
        }
        
        if username in demo_users and demo_users[username]['password'] == password:
            # Uğurlu giriş
            user_data = {
                'username': username,
                'role': demo_users[username]['role']
            }
            
            self.login_window.destroy()
            self.success_callback(user_data)
        else:
            self.show_error("Yanlış istifadəçi adı və ya parol!")
            self.password_entry.delete(0, tk.END)
    
    def show_error(self, message):
        """Xəta mesajı göstər"""
        messagebox.showerror("Xəta", message, parent=self.login_window)
    
    def on_close(self):
        """Pəncərə bağlandıqda"""
        self.login_window.quit()
        if self.parent:
            self.parent.quit()
