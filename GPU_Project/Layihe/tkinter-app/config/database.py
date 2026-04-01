# Verilənlər bazası idarəetməsi

"""
SQLite verilənlər bazası ilə əlaqə və əməliyyatlar
"""

import sqlite3
import os
from datetime import datetime
from config.settings import DATABASE_PATH, DATA_DIR, DEFAULT_CATEGORIES

class DatabaseManager:
    """Verilənlər bazası əməliyyatlarını idarə edir"""
    
    def __init__(self):
        """Konstruktor - verilənlər bazası əlaqəsini qurur"""
        self.database_path = DATABASE_PATH
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Data qovluğunun mövcudluğunu yoxlayır, yoxdursa yaradır"""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
    
    def get_connection(self):
        """Verilənlər bazasına bağlantı alır"""
        try:
            conn = sqlite3.connect(self.database_path)
            conn.row_factory = sqlite3.Row  # Dict kimi istifadə etmək üçün
            return conn
        except sqlite3.Error as e:
            raise Exception(f"Verilənlər bazasına bağlantı xətası: {e}")
    
    def initialize_database(self):
        """Verilənlər bazasını yaradır və cədvəlləri qurur"""
        try:
            with self.get_connection() as conn:
                # Tasks cədvəli
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        status TEXT DEFAULT 'pending',
                        priority TEXT DEFAULT 'medium',
                        category TEXT DEFAULT 'general',
                        due_date DATE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Notes cədvəli
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT,
                        category TEXT DEFAULT 'general',
                        tags TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Categories cədvəli
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL,
                        color TEXT DEFAULT '#6c757d',
                        type TEXT DEFAULT 'general'
                    )
                ''')
                
                # Settings cədvəli
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS settings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        key TEXT UNIQUE NOT NULL,
                        value TEXT,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                conn.commit()
                
                # Default kateqoriyaları əlavə et
                self._insert_default_categories(conn)
                
        except sqlite3.Error as e:
            raise Exception(f"Verilənlər bazası yaradılarkən xəta: {e}")
    
    def _insert_default_categories(self, conn):
        """Default kateqoriyaları bazaya əlavə edir"""
        try:
            for category in DEFAULT_CATEGORIES:
                conn.execute('''
                    INSERT OR IGNORE INTO categories (name, color, type)
                    VALUES (?, ?, ?)
                ''', (category["name"], category["color"], category["type"]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Default kateqoriyalar əlavə edilərkən xəta: {e}")
    
    def execute_query(self, query, params=None):
        """Sorğu icra edir və nəticəni qaytarır"""
        try:
            with self.get_connection() as conn:
                if params:
                    cursor = conn.execute(query, params)
                else:
                    cursor = conn.execute(query)
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Sorğu icra edilərkən xəta: {e}")
    
    def execute_update(self, query, params=None):
        """Update/Insert/Delete sorğularını icra edir"""
        try:
            with self.get_connection() as conn:
                if params:
                    cursor = conn.execute(query, params)
                else:
                    cursor = conn.execute(query)
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            raise Exception(f"Sorğu icra edilərkən xəta: {e}")
    
    def get_last_insert_id(self):
        """Sonuncu əlavə edilən sətirin ID-sini qaytarır"""
        try:
            with self.get_connection() as conn:
                cursor = conn.execute("SELECT last_insert_rowid()")
                return cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise Exception(f"Last insert ID alınarkən xəta: {e}")
    
    def backup_database(self, backup_path=None):
        """Verilənlər bazasını backup edir"""
        try:
            if not backup_path:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_filename = f"backup_{timestamp}.db"
                backup_dir = os.path.join(DATA_DIR, "backups")
                if not os.path.exists(backup_dir):
                    os.makedirs(backup_dir)
                backup_path = os.path.join(backup_dir, backup_filename)
            
            # Faylı kopyalamaq
            import shutil
            shutil.copy2(self.database_path, backup_path)
            return backup_path
            
        except Exception as e:
            raise Exception(f"Backup zamanı xəta: {e}")
    
    def close_connection(self):
        """Bağlantını bağlayır"""
        # Context manager istifadə etdiyimiz üçün avtomatik bağlanır
        pass