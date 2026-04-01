-- Database Schema - SQL
-- Verilənlər bazası sxemi

-- Create database
-- CREATE DATABASE appdb;
-- USE appdb;

-- =============================================
-- Users table - İstifadəçilər cədvəli
-- =============================================
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- =============================================
-- Settings table - Parametrlər cədvəli
-- =============================================
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    setting_key VARCHAR(100) NOT NULL,
    setting_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(user_id, setting_key)
);

-- =============================================
-- Sessions table - Sessiyalar cədvəli
-- =============================================
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    session_token VARCHAR(255) NOT NULL UNIQUE,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- =============================================
-- Logs table - Loglar cədvəli
-- =============================================
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =============================================
-- Create indexes - İndekslər
-- =============================================
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_settings_user_id ON settings(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_token ON sessions(session_token);
CREATE INDEX IF NOT EXISTS idx_logs_level ON logs(level);
CREATE INDEX IF NOT EXISTS idx_logs_created_at ON logs(created_at);

-- =============================================
-- Sample queries - Nümunə sorğular
-- =============================================

-- Insert a new user
-- INSERT INTO users (username, email, password_hash, first_name, last_name)
-- VALUES ('testuser', 'test@example.com', 'hashed_password', 'Test', 'User');

-- Get user by email
-- SELECT * FROM users WHERE email = 'test@example.com';

-- Update user settings
-- INSERT OR REPLACE INTO settings (user_id, setting_key, setting_value)
-- VALUES (1, 'theme', 'dark');

-- Get user settings
-- SELECT s.setting_key, s.setting_value 
-- FROM settings s 
-- WHERE s.user_id = 1;

-- Create session
-- INSERT INTO sessions (user_id, session_token, ip_address, expires_at)
-- VALUES (1, 'random_token_here', '192.168.1.1', datetime('now', '+1 day'));

-- Log entry
-- INSERT INTO logs (level, message, source)
-- VALUES ('INFO', 'User logged in', 'AuthService');

-- Get recent logs
-- SELECT * FROM logs ORDER BY created_at DESC LIMIT 100;
