# Tkinter Desktop Tətbiqi - Texniki Plan

## 🎯 Layihə Məqsədi

Bu Tkinter desktop tətbiqi portfolio layihəsinin bir hissəsidir və Python GUI proqramlaşdırma bacarıqlarını nümayiş etdirmək məqsədini güdür.

## 💡 Tətbiq İdeyası: "Personal Task Manager & Notes"

Şəxsi tapşırıq idarəetməsi və qeyd sistemli desktop tətbiqi hazırlamaq.

## 🚀 Əsas Funksiyalar

### 1. Tapşırıq İdarəetməsi (Task Management)
- ✅ Yeni tapşırıq əlavə etmək
- ✅ Tapşırıqları redaktə etmək
- ✅ Tapşırıqları silmək
- ✅ Tapşırıq statusunu dəyişmək (Pending, In Progress, Completed)
- ✅ Tapşırıqlara prioritet vermək (High, Medium, Low)
- ✅ Tapşırıqlara tarix əlavə etmək (deadline)

### 2. Qeyd Sistemi (Notes System)
- 📝 Qısa qeydlər yazmaq
- 📝 Qeydləri kateqoriyalara ayırmaq
- 📝 Qeydləri axtarmaq və filtirləmək
- 📝 Qeydləri fayl kimi eksport etmək (.txt, .md)

### 3. Əlavə Funksiyalar
- 🎨 Tema dəyişikliyi (Light/Dark mode)
- 💾 Məlumatları lokal bazada saxlamaq (SQLite)
- 📊 Statistik məlumatlar (tamamlanmış tapşırıqlar, statistika)
- 🔔 Təqvim və xatırlatmalar
- 📤 Məlumatları backup etmək və import etmək

## 🏗️ Texniki Strukturu

### Əsas Texnologiyalar
- **Python 3.8+**
- **Tkinter** (GUI framework)
- **SQLite3** (verilənlər bazası)
- **tkinter.ttk** (modern widget-lər)
- **datetime** (tarix əməliyyatları)
- **json** (konfiqurasiya)

### Layihə Faylları
```
tkinter-app/
├── main.py                 # Əsas başlanğıc faylı
├── config/
│   ├── __init__.py
│   ├── settings.py         # Tətbiq konfiqurasiyası
│   └── database.py         # Verilənlər bazası bağlantısı
├── gui/
│   ├── __init__.py
│   ├── main_window.py      # Əsas pəncərə
│   ├── task_manager.py     # Tapşırıq idarəetməsi GUI
│   ├── notes_manager.py    # Qeydlər GUI
│   ├── settings_window.py  # Parametrlər pəncərəsi
│   └── dialogs.py          # Dialog pəncərələri
├── core/
│   ├── __init__.py
│   ├── task_model.py       # Tapşırıq modeli
│   ├── notes_model.py      # Qeyd modeli
│   ├── database_manager.py # Verilənlər bazası əməliyyatları
│   └── utils.py            # Köməkçi funksiyalar
├── assets/
│   ├── icons/              # İkonlar
│   ├── themes/             # Tema faylları
│   └── styles.py           # CSS-style konfiqurasiyalar
├── data/
│   └── app.db              # SQLite verilənlər bazası
├── tests/
│   ├── test_tasks.py
│   ├── test_notes.py
│   └── test_database.py
├── requirements.txt        # Python tələbləri
├── README.md
└── setup.py                # Quraşdırma skripti
```

## 🎨 GUI Dizayn Planı

### Əsas Pəncərə (Main Window)
```
┌─────────────────────────────────────────────────────────┐
│  Personal Task Manager & Notes              [_] [□] [×] │
├─────────────────────────────────────────────────────────┤
│  File  Edit  View  Tools  Help                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─── Tasks ──┐  ┌─── Notes ───┐  ┌─── Calendar ───┐   │
│  │             │  │             │  │                │   │
│  │ • Task 1    │  │ • Note 1    │  │   September    │   │
│  │ • Task 2    │  │ • Note 2    │  │  S  M  T  W  T │   │
│  │ • Task 3    │  │ • Note 3    │  │     1  2  3  4 │   │
│  │             │  │             │  │  5  6  7  8  9 │   │
│  │ [Add Task]  │  │ [Add Note]  │  │               │   │
│  └─────────────┘  └─────────────┘  └────────────────┘   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Status: Ready | Tasks: 15 | Completed: 8 | Notes: 23  │
└─────────────────────────────────────────────────────────┘
```

### Tapşırıq Əlavə Etmə Dialog-u
```
┌───────────────────────────────────┐
│  Add New Task              [×]    │
├───────────────────────────────────┤
│                                   │
│  Title:  [____________________]   │
│                                   │
│  Description:                     │
│  ┌─────────────────────────────┐   │
│  │                             │   │
│  │                             │   │
│  └─────────────────────────────┘   │
│                                   │
│  Priority: [High ▼]               │
│  Due Date: [12/09/2025 ▼]         │
│  Category: [Work ▼]               │
│                                   │
│           [Cancel] [Save]         │
└───────────────────────────────────┘
```

## 💾 Verilənlər Bazası Strukturu

### Tasks Table
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    priority TEXT DEFAULT 'medium',
    category TEXT DEFAULT 'general',
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes Table
```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    category TEXT DEFAULT 'general',
    tags TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Categories Table
```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    color TEXT DEFAULT '#0078d4',
    type TEXT DEFAULT 'general'
);
```

## 📱 Funksional Tələblər

### 1. Tapşırıq İdarəetməsi
- **CRUD əməliyyatları**: Create, Read, Update, Delete
- **Status idarəetməsi**: Pending → In Progress → Completed
- **Filtirləmə**: Status, prioritet, kateqoriya, tarix
- **Axtarış**: Başlıq və təsvir üzrə axtarış
- **Sort etmə**: Tarix, prioritet, başlıq

### 2. Qeydlər Sistemi
- **Sadə text editor** ilə qeyd yazma
- **Kategoriyalaşdırma** sistemi
- **Tag sistemi** (#work, #personal)
- **Export/Import** funksiyası

### 3. Sistem Funksiyaları
- **Avtomatik backup** (gündəlik)
- **Tema dəyişikliyi** real-time
- **Keyboard shortcuts**
- **Sistem tray minimization**

## 🎯 İcra Planı

### MƏRHƏLƏ 1: Əsas Struktur (1-2 gün)
1. Layihə qovluqları yaratmaq
2. Əsas faylları və modulları yaratmaq
3. Verilənlər bazası strukturunu hazırlamaq
4. Konfiqurasiya sistemini qurmaq

### MƏRHƏLƏ 2: Core Funksiyalar (2-3 gün)
1. Task model və əməliyyatlarını hazırlamaq
2. Notes model və əməliyyatlarını hazırlamaq
3. Database manager klassını yazmaq
4. Utilities və köməkçi funksiyalar

### MƏRHƏLƏ 3: GUI İnkişafı (3-4 gün)
1. Main window layout-unu hazırlamaq
2. Task management GUI
3. Notes management GUI
4. Dialog pəncərələri və formalar

### MƏRHƏLƏ 4: Əlavə Funksiyalar (2-3 gün)
1. Tema sistemi
2. Export/Import funksiyaları
3. Statistik məlumatlar
4. Settings pəncərəsi

### MƏRHƏLƏ 5: Test və Optimallaşdırma (1-2 gün)
1. Unit testlər yazmaq
2. Bug fixing
3. Performance optimallaşdırması
4. Documentation yazma

## 🔧 Development Environment

### Tələb olunan Python Packages
```txt
tkinter (built-in)
sqlite3 (built-in)
datetime (built-in)
json (built-in)
pillow>=8.0.0         # İmage processing
tkcalendar>=1.6.0     # Calendar widget
```

### Optional Packages
```txt
pyinstaller>=4.0      # Executable yaratmaq üçün
pytest>=6.0.0         # Testing üçün
black>=21.0.0         # Code formatting
flake8>=3.8.0         # Code linting
```

## 📈 Gözlənilən Nəticələr

1. **Tam funksional desktop tətbiqi** tapşırıq və qeydləri idarə etmək üçün
2. **Professional GUI dizayn** modern görünüş ilə
3. **Stabil və performant** kod strukturu
4. **Portfolio layihəsinə** əlavə texniki komponent
5. **Python Tkinter** bacarıqlarının nümayişi

---

**Plan tarixi**: 12 Sentyabr 2025
**Təxmini müddət**: 8-12 gün
**Çətinlik səviyyəsi**: Orta-Yüksək