# Personal Task Manager & Notes

Personal tapşırıq idarəetməsi və qeydlər sistemi - Python Tkinter ilə hazırlanmış desktop tətbiqi.

## 🎯 Məqsəd

Bu tətbiq portfolio layihəsinin bir hissəsidir və Python GUI proqramlaşdırma bacarıqlarını nümayiş etdirmək məqsədini güdür.

## ✨ Xüsusiyyətlər

### 📋 Tapşırıq İdarəetməsi
- ✅ Yeni tapşırıq əlavə etmək
- ✅ Tapşırıqları redaktə etmək və silmək
- ✅ Status idarəetməsi (Pending, In Progress, Completed)
- ✅ Prioritet sistemi (High, Medium, Low)
- ✅ Kateqoriya sistemi
- ✅ Tarix və deadline idarəetməsi

### 📝 Qeydlər Sistemi
- 📝 Qısa qeydlər yazmaq və idarə etmək
- 📝 Qeydləri kateqoriyalara ayırmaq
- 📝 Tag sistemi (#work, #personal)
- 📝 Axtarış və filtirləmə

### 🎨 Əlavə Funksiyalar
- 🌓 Light/Dark tema dəstəyi
- 💾 SQLite verilənlər bazası
- 📊 Statistik məlumatlar
- 📤 Backup və Export sistemi
- ⌨️ Keyboard shortcuts

## 🛠️ Texnologiyalar

- **Python 3.8+**
- **Tkinter** (GUI Framework)
- **SQLite3** (Verilənlər bazası)
- **tkcalendar** (Təqvim widget-i)
- **Pillow** (Şəkil emalı)

## 📦 Quraşdırma

### Tələblər
- Python 3.8 və ya daha yüksək versiya
- pip package manager

### Addım-addım quraşdırma

1. **Repository-ni klonlamaq:**
```bash
git clone [repository-url]
cd tkinter-app
```

2. **Virtual environment yaratmaq (tövsiyə edilir):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# və ya
venv\\Scripts\\activate  # Windows
```

3. **Paketləri quraşdırmaq:**
```bash
pip install -r requirements.txt
```

4. **Tətbiqi işə salmaq:**
```bash
python main.py
```

## 🏗️ Layihə Strukturu

```
tkinter-app/
├── main.py                 # Ana başlanğıc faylı
├── config/                 # Konfiqurasiya modulları
│   ├── __init__.py
│   ├── settings.py         # Tətbiq parametrləri
│   └── database.py         # Verilənlər bazası idarəetməsi
├── gui/                    # GUI komponentləri
│   ├── __init__.py
│   ├── main_window.py      # Ana pəncərə
│   ├── task_manager.py     # Tapşırıq idarəetməsi GUI
│   ├── notes_manager.py    # Qeydlər GUI
│   └── dialogs.py          # Dialog pəncərələri
├── core/                   # Əsas biznes məntiqi
│   ├── __init__.py
│   ├── task_model.py       # Tapşırıq modeli
│   ├── notes_model.py      # Qeyd modeli
│   └── utils.py            # Köməkçi funksiyalar
├── assets/                 # Statik fayllar
│   ├── icons/              # İkonlar
│   └── themes/             # Tema faylları
├── data/                   # Verilənlər qovluğu
│   └── app.db              # SQLite bazası
├── tests/                  # Test faylları
├── requirements.txt        # Python tələbləri
└── README.md              # Bu fayl
```

## 📱 İstifadə

### İlk İşə Salma
1. Tətbiqi başladın: `python main.py`
2. Ana pəncərə açılacaq
3. Sol paneldə tapşırıqları, sağ paneldə qeydləri görsünüz

### Tapşırıq Əlavə Etmə
1. "Add Task" düyməsinə basın
2. Forma doldurún (başlıq, təsvir, prioritet, tarix)
3. "Save" düyməsi ilə yadda saxlayın

### Qeyd Yaratma
1. "Add Note" düyməsinə basın
2. Başlıq və məzmun yazın
3. Kateqoriya və tag-lar əlavə edin

### Klaviatura Qısayolları
- `Ctrl+T` - Yeni tapşırıq
- `Ctrl+N` - Yeni qeyd
- `Ctrl+S` - Yadda saxla
- `Ctrl+F` - Axtarış
- `Ctrl+Q` - Proqramdan çıx

## 🔧 İnkişaf

### Test etmək
```bash
pytest tests/
```

### Kod formatlamaq
```bash
black .
flake8 .
```

### Executable yaratmaq
```bash
pyinstaller --onefile --windowed main.py
```

## 📊 Verilənlər Bazası

Tətbiq SQLite verilənlər bazası istifadə edir. Əsas cədvəllər:
- `tasks` - Tapşırıq məlumatları
- `notes` - Qeyd məlumatları
- `categories` - Kateqoriya sistemi
- `settings` - Tətbiq parametrləri

## 🎨 Temalar

Tətbiq iki tema dəstəkləyir:
- **Light Theme** - Açıq rəngli interfeys
- **Dark Theme** - Qaranlıq rəngli interfeys

Tema dəyişikliyi real-time həyata keçirilir.

## 📸 Ekran Görüntüləri

*(Bu hissəyə tətbiqin ekran görüntüləri əlavə ediləcək)*

## 🐛 Problemlər və Dəstək

Əgər problem taparsan və ya sual yararsa:
1. GitHub Issues bölməsinə bax
2. Yeni issue yarat
3. Detallı təsvir ver

## 📄 Lisenziya

Bu layihə portfolio məqsədilə hazırlanıb və təlim məqsədilə açıq kodludur.

## 👨‍💻 Müəllif

Portfolio Layihəsi - Python Tkinter Desktop Tətbiqi

---

**Qeyd**: Bu tətbiq portfolio layihəsinin bir hissəsidir və Python GUI proqramlaşdırma bacarıqlarını nümayiş etdirmək məqsədini güdür.