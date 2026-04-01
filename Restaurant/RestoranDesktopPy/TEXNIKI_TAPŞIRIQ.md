# Restoran İdarə Etmə Sistemi - Texniki Tapşırıq

## Layihənin Ümumi Məlumatları
- **Layihə adı:** Restoran İdarə Etmə Sistemi (RIES)
- **Texnologiya:** Python + tkinter
- **Məqsəd:** Restoranın gündəlik fəaliyyətlərinin idarə edilməsi
- **Versiya:** 1.0 (Minimal)

## Minimal Funksional Tələblər

### 1. İSTİFADƏÇİ İDARƏSİ
- **1.1** Sistem giriş ekranı (istifadəçi adı və parol)
- **1.2** İki tip istifadəçi: 
  - Admin (bütün hüquqlar)
  - Ofisiant (məhdud hüquqlar)

### 2. MUSTERILER
- **2.1** Müştəri əlavə etmə (ad, telefon, email)
- **2.2** Müştəri siyahısını görüntüləmə
- **2.3** Müştəri məlumatlarını yeniləmə
- **2.4** Müştəri silmə

### 3. MASALAR
- **3.1** Masa məlumatları (masa nömrəsi, tutum, status)
- **3.2** Masa statusları:
  - Boş
  - Məşğul
  - Rezervə olunmuş
  - Təmizlənir
- **3.3** Masa statusunu dəyişdirmə

### 4. SİFARİŞLƏR
- **4.1** Yeni sifariş yaratma
- **4.2** Sifarişə məhsul əlavə etmə/çıxarma
- **4.3** Sifariş statusları:
  - Yeni
  - Hazırlanır
  - Hazır
  - Təhvil verildi
  - Ləğv edildi
- **4.4** Sifariş siyahısını görüntüləmə
- **4.5** Ümumi sifariş məbləğinin hesablanması

### 5. MENYU İDARƏSİ
- **5.1** Məhsul əlavə etmə (ad, qiymət, kateqoriya)
- **5.2** Məhsul siyahısını görüntüləmə
- **5.3** Məhsul məlumatlarını yeniləmə
- **5.4** Məhsul silmə
- **5.5** Kateqoriya üzrə qruplaşdırma

### 6. REZERVASIYALAR
- **6.1** Yeni rezervasiya yaratma (müştəri, masa, tarix, saat)
- **6.2** Rezervasiya siyahısını görüntüləmə
- **6.3** Rezervasiya statusları:
  - Aktiv
  - Tamamlandı
  - Ləğv edildi
- **6.4** Rezervasiya yeniləmə/ləğv etmə

### 7. ÖDƏMƏLƏR
- **7.1** Sifariş üçün ödəmə hesablama
- **7.2** Ödəmə növləri:
  - Nəqd
  - Kart
- **7.3** Ödəmə tarixçəsi
- **7.4** Gündəlik satış hesabatı

### 8. HESABATLAR (Minimal)
- **8.1** Gündəlik satış hesabatı
- **8.2** Populyar məhsullar siyahısı
- **8.3** Masa doluluk statistikası

## Texniki Tələblər

### Verilənlər Bazası
- **DB növü:** SQLite (lokal fayl)
- **Cədvəllər:**
  - users (id, username, password, role)
  - customers (id, name, phone, email)
  - tables (id, number, capacity, status)
  - menu_items (id, name, price, category)
  - orders (id, table_id, customer_id, date, status, total)
  - order_items (id, order_id, menu_item_id, quantity, price)
  - reservations (id, customer_id, table_id, date, time, status)
  - payments (id, order_id, amount, payment_type, date)

### İstifadəçi İnterfeysi
- **Ana pəncərə:** Menyu paneli ilə
- **Modullar:** Ayrı pəncərələr və ya tablar
- **Dizayn:** Sadə və funksional
- **Ölçü:** 1024x768 minimal

### Faylların Strukturu
```
RestaurantManagement/
├── main.py              # Ana proqram
├── database/
│   ├── __init__.py
│   ├── db_manager.py    # Verilənlər bazası əməliyyatları
│   └── models.py        # Verilənlər modelləri
├── gui/
│   ├── __init__.py
│   ├── main_window.py   # Ana pəncərə
│   ├── login.py         # Giriş ekranı
│   ├── customers.py     # Müştərilər modulu
│   ├── tables.py        # Masalar modulu
│   ├── orders.py        # Sifarişlər modulu
│   ├── menu.py          # Menyu modulu
│   ├── reservations.py  # Rezervasiyalar modulu
│   └── reports.py       # Hesabatlar modulu
├── utils/
│   ├── __init__.py
│   └── helpers.py       # Yardımçı funksiyalar
└── restaurant.db        # SQLite verilənlər bazası
```

## Layihənin Mərhələləri

### Mərhələ 1: Əsas Struktur (1 həftə)
- Verilənlər bazası yaratma
- Ana pəncərə və giriş sistemi
- Əsas navigasiya

### Mərhələ 2: Əsas Modullər (2 həftə)
- Müştərilər idarəsi
- Masalar idarəsi
- Menyu idarəsi

### Mərhələ 3: Sifarişlər (1 həftə)
- Sifariş yaratma və idarəsi
- Ödəmə sistemi

### Mərhələ 4: Rezervasiyalar və Hesabatlar (1 həftə)
- Rezervasiya sistemi
- Əsas hesabatlar

## Qeydlər
- Bu minimal versiyadır, sonradan genişləndirilə bilər
- Sadə və anlaşılan interfeys üstünlük təşkil edir
- Performans üçün optimallaşdırma sonrakı versiyalarda
- Backup və restore funksiyaları əlavə edilə bilər
