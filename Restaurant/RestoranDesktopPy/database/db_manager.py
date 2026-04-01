"""
Verilənlər bazası idarəçisi
SQLite ilə işləmək üçün əsas sinflar
"""

import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="restaurant.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Verilənlər bazasını və cədvəlləri yarat"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # İstifadəçilər cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users ( /* İstifadəçilər cədvəli */
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL DEFAULT 'ofisiant',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Müştərilər cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT,
                    email TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Masalar cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tables (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number INTEGER UNIQUE NOT NULL,
                    capacity INTEGER NOT NULL,
                    status TEXT DEFAULT 'boş'
                )
            ''')
            
            # Menyu məhsulları cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS menu_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    category TEXT NOT NULL,
                    available BOOLEAN DEFAULT 1
                )
            ''')
            
            # Sifarişlər cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    table_id INTEGER,
                    customer_id INTEGER,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    status TEXT DEFAULT 'yeni',
                    total REAL DEFAULT 0,
                    FOREIGN KEY (table_id) REFERENCES tables (id),
                    FOREIGN KEY (customer_id) REFERENCES customers (id)
                )
            ''')
            
            # Sifariş məhsulları cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS order_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER,
                    menu_item_id INTEGER,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES orders (id),
                    FOREIGN KEY (menu_item_id) REFERENCES menu_items (id)
                )
            ''')
            
            # Rezervasiyalar cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    table_id INTEGER,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    status TEXT DEFAULT 'aktiv',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (customer_id) REFERENCES customers (id),
                    FOREIGN KEY (table_id) REFERENCES tables (id)
                )
            ''')
            
            # Ödəmələr cədvəli
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER,
                    amount REAL NOT NULL,
                    payment_type TEXT NOT NULL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (order_id) REFERENCES orders (id)
                )
            ''')
            
            # İlk məlumatları əlavə et
            self.insert_initial_data(cursor)
            conn.commit()
    
    def insert_initial_data(self, cursor):
        """İlk istifadəçi və məlumatları əlavə et"""
        # Admin istifadəçisi
        cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = ?", ("admin",)
        )
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                ("admin", "admin123", "admin")
            )
        
        # Nümunə masalar
        cursor.execute("SELECT COUNT(*) FROM tables")
        if cursor.fetchone()[0] == 0:
            for i in range(1, 11):
                cursor.execute(
                    "INSERT INTO tables (number, capacity) VALUES (?, ?)",
                    (i, 4 if i <= 8 else 6)
                )
    
    def get_connection(self):
        """Verilənlər bazası bağlantısını qaytar"""
        return sqlite3.connect(self.db_path)
    
    def execute_query(self, query, params=None):
        """SQL sorğu icra et"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
    
    def execute_insert(self, query, params=None):
        """Insert sorğu icra et və yeni ID-ni qaytar"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor.lastrowid
