# Restoran İdarə Etmə Sistemi

Bu layihə Python və tkinter istifadə edərək restoran idarəsini həyata keçirən desktop proqramıdır.

## Xüsusiyyətlər

- **Müştəri İdarəsi**: Müştəri məlumatlarının saxlanması və idarəsi
- **Masa İdarəsi**: Masa statuslarının izlənməsi
- **Sifariş İdarəsi**: Sifarişlərin qəbulu və izlənməsi
- **Menyu İdarəsi**: Məhsul və qiymətlərin idarəsi
- **Rezervasiya Sistemi**: Masa rezervasiyalarının idarəsi
- **Ödəmə Sistemi**: Nəqd və kart ödəmələrinin işlənməsi
- **Hesabat Sistemi**: Satış və statistika hesabatları

## Quraşdırma

1. Python 3.7+ yükləyin
2. Lazımi kitabxanaları yükləyin:
```bash
pip install -r requirements.txt
```

3. Proqramı işə salın:
```bash
python main.py
```

## İstifadə

### İlk Giriş
- İstifadəçi adı: `admin`
- Parol: `admin123`

### Sistem Tələbləri
- Python 3.7+
- tkinter (Python ilə birlikdə gəlir)
- SQLite3 (Python ilə birlikdə gəlir)

## Faylların Strukturu

```
RestaurantManagement/
├── main.py                    # Ana proqram
├── TEXNIKI_TAPŞIRIQ.md       # Texniki tapşırıq
├── README.md                  # Bu fayl
├── requirements.txt           # Lazımi kitabxanalar
├── database/
│   ├── __init__.py
│   ├── db_manager.py         # Verilənlər bazası idarəsi
│   └── models.py             # Verilənlər modelləri
└── gui/
    ├── __init__.py
    ├── main_window.py        # Ana pəncərə
    ├── login.py              # Giriş ekranı
    ├── customers.py          # Müştərilər modulu
    ├── tables.py             # Masalar modulu
    ├── orders.py             # Sifarişlər modulu
    ├── menu.py               # Menyu modulu
    ├── reservations.py       # Rezervasiyalar modulu
    └── reports.py            # Hesabatlar modulu
```

## Əlaqə

Layihə haqqında suallar üçün development team ilə əlaqə saxlayın.
