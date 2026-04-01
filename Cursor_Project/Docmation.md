# 📋 E-Ticarət Platforması - Layihə Dokumentasiyası və Plan

## 📅 Layihə Məlumatları
- **Layihə Adı:** E-Ticarət Platforması
- **Versiya:** 1.0
- **Son Yeniləmə:** 28 Dekabr 2025
- **Dil:** Azərbaycan dili

---

## 🎯 Layihənin Məqsədi
Müasir, istifadəçi dostu və tam funksional e-ticarət platforması yaratmaq. Platform həm alıcılar, həm də satıcılar üçün ayrı-ayrı interfeyslərə malik olacaq.

---

## 🏗️ Mövcud Arxitektura

### 📁 Layihə Strukturu
```
Cursor_procekt.code/
│
├── index.html              # Əsas səhifə (Alıcı interfeysi)
├── seller-dashboard.html   # Satıcı paneli
│
├── styles.css              # Əsas səhifə üçün stiller
├── seller-styles.css       # Satıcı paneli stilləri
│
├── script.js               # Əsas səhifə funksiyaları
├── seller-script.js        # Satıcı paneli funksiyaları
│
└── Docmation.md           # Bu fayl - Dokumentasiya
```

---

## 🎨 FRONTEND - Hazırda Mövcud Funksiyalar

### 1️⃣ **Əsas Səhifə (index.html)**

#### ✅ Mövcud Komponentlər:
- **Header (Başlıq)**
  - Logo və navigasiya menyusu
  - Axtarış qutusu
  - İstifadəçi, səbət və istək siyahısı ikonları
  
- **Hero Bölməsi**
  - Əsas banner
  - CTA (Call-to-Action) düyməsi
  
- **Məhsullar Şəbəkəsi**
  - 4 məhsul kartı
  - Hover effektləri
  - Klik edildikdə səbətə əlavə
  
- **Kateqoriyalar**
  - 4 kateqoriya kartı
  - İkonlar və adlar
  
- **Newsletter**
  - E-poçt abunəliyi forması
  - Email validasiyası
  
- **Footer**
  - Sosial media linkləri
  - Ödəniş metodları ikonları
  - Navigasiya linkləri

#### ✅ JavaScript Funksiyaları:
- ✔️ Axtarış funksiyası
- ✔️ Səbət əlavə etmə
- ✔️ Bildiriş sistemi (notifications)
- ✔️ İstək siyahısı
- ✔️ Email validasiyası
- ✔️ Smooth scroll
- ✔️ Header scroll effekti
- ✔️ Səbət badge sayğacı

---

### 2️⃣ **Satıcı Paneli (seller-dashboard.html)**

#### ✅ Mövcud Komponentlər:
- **Sidebar (Yan panel)**
  - İstifadəçi profili
  - Navigasiya menyusu
  - "Mağazaya Bax" düyməsi
  - Ayarlar və çıxış
  
- **Məhsul Yaratma Forması**
  - Məhsul adı
  - Təsvir
  - Kateqoriya seçimi
  - Şəkil yükləmə (Drag & Drop)
  - Qiymət (+/- düymələri ilə)
  - Çatdırılma müddəti
  
#### ✅ JavaScript Funksiyaları:
- ✔️ Drag & Drop şəkil yükləmə
- ✔️ Şəkil önizləmə
- ✔️ Forma validasiyası
- ✔️ Qiymət artırma/azaltma
- ✔️ "Yadda Saxla" və "Dərc Et" funksiyaları
- ✔️ Bildiriş sistemi

---

## 🚀 FRONTEND - Gələcək Təkmilləşdirmələr

### 📋 Prioritet 1 (Yüksək)

#### 🛒 Alıcı İnterfeysi Təkmilləşdirmələri:

1. **Məhsul Detay Səhifəsi**
   - [ ] Ayrı məhsul səhifəsi yaratmaq
   - [ ] Böyük şəkil qalereyası
   - [ ] Rəylər və reytinq sistemi
   - [ ] Oxşar məhsullar bölməsi
   - [ ] "Səbətə Əlavə Et" funksiyası

2. **Səbət Səhifəsi**
   - [ ] Səbət modalı və ya ayrı səhifə
   - [ ] Məhsul sayını dəyişdirmə
   - [ ] Məhsul silmə
   - [ ] Ümumi qiymət hesablanması
   - [ ] Kupon/Endirim kodu

3. **İstifadəçi Autentifikasiyası**
   - [ ] Qeydiyyat forması
   - [ ] Giriş forması
   - [ ] Şifrəni unutdum
   - [ ] İstifadəçi profili səhifəsi

4. **Ödəniş Prosesi (Checkout)**
   - [ ] Çatdırılma ünvanı forması
   - [ ] Ödəniş metodu seçimi
   - [ ] Sifariş xülasəsi
   - [ ] Təsdiq səhifəsi

5. **Axtarış və Filtrlər**
   - [ ] Axtarış nəticələri səhifəsi
   - [ ] Qiymət aralığı filtri
   - [ ] Kateqoriya filtri
   - [ ] Çeşidləmə (ucuzdan bahaya, yenidən köhnəyə)
   - [ ] Brend filtri

---

### 📋 Prioritet 2 (Orta)

#### 👤 İstifadəçi Xüsusiyyətləri:

6. **İstifadəçi Profili**
   - [ ] Profil məlumatlarını redaktə
   - [ ] Sifariş tarixçəsi
   - [ ] İstək siyahısı
   - [ ] Ünvan dəftərçəsi
   - [ ] Ödəniş metodları

7. **Sifariş İzləmə**
   - [ ] Sifariş statusu
   - [ ] Çatdırılma izləmə
   - [ ] Bildirişlər

8. **Rəy və Reytinq**
   - [ ] Məhsullara rəy yazma
   - [ ] Ulduz reytinqi
   - [ ] Rəy şəkilləri
   - [ ] Rəylərə cavab

---

### 📋 Prioritet 3 (Aşağı)

#### ⚡ Əlavə Xüsusiyyətlər:

9. **Chat Dəstəyi**
   - [ ] Canlı chat widget
   - [ ] Satıcı ilə mesajlaşma

10. **Responsive Dizayn Təkmilləşdirmələri**
    - [ ] Mobil menyu
    - [ ] Tablet optimizasiyası
    - [ ] Touch jestləri

11. **Performans Optimizasiyası**
    - [ ] Lazy loading şəkillər
    - [ ] Code splitting
    - [ ] Caching strategiyası

---

## 🖥️ BACKEND - Plan və Arxitektura

### 🎯 Backend Texnologiya Seçimi

#### Tövsiyə olunan Stack:

**Variant 1: Node.js (JavaScript/TypeScript)**
```
- Runtime: Node.js
- Framework: Express.js və ya NestJS
- Database: PostgreSQL və ya MongoDB
- ORM: Prisma və ya TypeORM
- Authentication: JWT + bcrypt
```

**Variant 2: Python**
```
- Framework: Django və ya FastAPI
- Database: PostgreSQL
- ORM: Django ORM və ya SQLAlchemy
- Authentication: JWT + Django Rest Framework
```

**Variant 3: PHP**
```
- Framework: Laravel
- Database: MySQL və ya PostgreSQL
- ORM: Eloquent
- Authentication: Laravel Sanctum
```

---

### 📊 Verilənlər Bazası Strukturu

#### **1. Users (İstifadəçilər) Cədvəli**
```sql
- id (Primary Key)
- email (Unique)
- password (Hashed)
- first_name
- last_name
- phone
- role (buyer/seller/admin)
- avatar
- is_verified
- created_at
- updated_at
```

#### **2. Products (Məhsullar) Cədvəli**
```sql
- id (Primary Key)
- seller_id (Foreign Key -> Users)
- name
- description
- category_id (Foreign Key -> Categories)
- price
- stock_quantity
- images (JSON array və ya ayrı cədvəl)
- delivery_time
- is_active
- created_at
- updated_at
```

#### **3. Categories (Kateqoriyalar) Cədvəli**
```sql
- id (Primary Key)
- name
- slug
- icon
- parent_id (Self reference - alt kateqoriyalar üçün)
- created_at
```

#### **4. Orders (Sifarişlər) Cədvəli**
```sql
- id (Primary Key)
- user_id (Foreign Key -> Users)
- total_amount
- status (pending/processing/shipped/delivered/cancelled)
- payment_method
- payment_status
- delivery_address
- created_at
- updated_at
```

#### **5. Order_Items (Sifariş Məhsulları) Cədvəli**
```sql
- id (Primary Key)
- order_id (Foreign Key -> Orders)
- product_id (Foreign Key -> Products)
- quantity
- price_at_purchase
- created_at
```

#### **6. Reviews (Rəylər) Cədvəli**
```sql
- id (Primary Key)
- user_id (Foreign Key -> Users)
- product_id (Foreign Key -> Products)
- rating (1-5)
- comment
- images (JSON)
- created_at
- updated_at
```

#### **7. Cart (Səbət) Cədvəli**
```sql
- id (Primary Key)
- user_id (Foreign Key -> Users)
- product_id (Foreign Key -> Products)
- quantity
- created_at
- updated_at
```

#### **8. Wishlist (İstək Siyahısı) Cədvəli**
```sql
- id (Primary Key)
- user_id (Foreign Key -> Users)
- product_id (Foreign Key -> Products)
- created_at
```

---

### 🔌 Backend API Endpoint Planı

#### **Auth Endpoints (Autentifikasiya)**
```
POST   /api/auth/register        - Qeydiyyat
POST   /api/auth/login           - Giriş
POST   /api/auth/logout          - Çıxış
POST   /api/auth/refresh-token   - Token yeniləmə
POST   /api/auth/forgot-password - Şifrəni unutdum
POST   /api/auth/reset-password  - Şifrəni sıfırla
```

#### **User Endpoints (İstifadəçi)**
```
GET    /api/users/profile        - Profil məlumatları
PUT    /api/users/profile        - Profili yenilə
GET    /api/users/orders         - İstifadəçi sifarişləri
GET    /api/users/wishlist       - İstək siyahısı
POST   /api/users/wishlist       - İstək siyahısına əlavə et
DELETE /api/users/wishlist/:id   - İstək siyahısından sil
```

#### **Product Endpoints (Məhsul)**
```
GET    /api/products              - Bütün məhsullar (pagination, filter)
GET    /api/products/:id          - Tək məhsul
POST   /api/products              - Yeni məhsul (satıcı)
PUT    /api/products/:id          - Məhsulu yenilə (satıcı)
DELETE /api/products/:id          - Məhsulu sil (satıcı)
GET    /api/products/search       - Məhsul axtarışı
GET    /api/products/category/:id - Kateqoriyaya görə
```

#### **Category Endpoints (Kateqoriya)**
```
GET    /api/categories            - Bütün kateqoriyalar
GET    /api/categories/:id        - Tək kateqoriya
POST   /api/categories            - Yeni kateqoriya (admin)
PUT    /api/categories/:id        - Kateqoriyanı yenilə (admin)
DELETE /api/categories/:id        - Kateqoriyanı sil (admin)
```

#### **Cart Endpoints (Səbət)**
```
GET    /api/cart                  - Səbəti gətir
POST   /api/cart                  - Səbətə əlavə et
PUT    /api/cart/:id              - Səbət elementini yenilə
DELETE /api/cart/:id              - Səbətdən sil
DELETE /api/cart                  - Səbəti təmizlə
```

#### **Order Endpoints (Sifariş)**
```
GET    /api/orders                - Bütün sifarişlər
GET    /api/orders/:id            - Tək sifariş
POST   /api/orders                - Yeni sifariş yarat
PUT    /api/orders/:id/status     - Sifariş statusunu yenilə
GET    /api/orders/track/:id      - Sifarişi izlə
```

#### **Review Endpoints (Rəy)**
```
GET    /api/reviews/product/:id   - Məhsul rəyləri
POST   /api/reviews               - Rəy yaz
PUT    /api/reviews/:id           - Rəyi yenilə
DELETE /api/reviews/:id           - Rəyi sil
```

#### **Seller Endpoints (Satıcı)**
```
GET    /api/seller/dashboard      - Satıcı statistikası
GET    /api/seller/products       - Satıcının məhsulları
GET    /api/seller/orders         - Satıcının sifarişləri
GET    /api/seller/analytics      - Analitika
```

---

### 🔐 Təhlükəsizlik Tədbirləri

#### Backend Təhlükəsizlik:
- [ ] **JWT Authentication** - Token əsaslı autentifikasiya
- [ ] **Password Hashing** - bcrypt istifadə edərək
- [ ] **CORS Configuration** - Cross-origin resource sharing
- [ ] **Rate Limiting** - API rate limiting
- [ ] **Input Validation** - Joi və ya yup ilə
- [ ] **SQL Injection Prevention** - ORM istifadəsi
- [ ] **XSS Protection** - Sanitization
- [ ] **HTTPS** - SSL sertifikatı
- [ ] **Environment Variables** - .env faylı

---

### 📦 Fayl Yükləmə və Saxlama

#### Şəkil Yükləmə:
```
Variant 1: Lokal Saxlama
- /uploads/products/
- /uploads/users/
- /uploads/reviews/

Variant 2: Cloud Storage
- AWS S3
- Cloudinary
- Google Cloud Storage
```

#### Şəkil Optimizasiyası:
- [ ] Şəkil ölçüsünü avtomatik kiçiltmə
- [ ] WebP formatına çevirmə
- [ ] Thumbnail yaratma
- [ ] Lazy loading dəstəyi

---

### 🔔 Bildiriş Sistemi

#### Email Bildirişləri:
- [ ] Qeydiyyat təsdiqi
- [ ] Şifrə sıfırlama
- [ ] Sifariş təsdiqi
- [ ] Sifariş statusu dəyişikliyi
- [ ] Newsletter

#### Push Bildirişləri:
- [ ] Yeni sifariş (satıcı üçün)
- [ ] Sifariş statusu (alıcı üçün)
- [ ] Kampaniya bildirişləri

---

## 🗓️ İcra Planı və Timeline

### **Faza 1: Backend Əsasları (2-3 həftə)**
- [ ] Backend stack seçimi və qurulması
- [ ] Verilənlər bazası dizaynı
- [ ] Auth sisteminin qurulması
- [ ] Əsas API endpointlərin yaradılması
- [ ] User və Product CRUD əməliyyatları

### **Faza 2: Frontend İnteqrasiyası (2 həftə)**
- [ ] API ilə əlaqə qurulması
- [ ] Qeydiyyat və giriş səhifələri
- [ ] Məhsul detay səhifəsi
- [ ] Səbət funksionallığı
- [ ] Real məlumatlarla test

### **Faza 3: Satıcı Paneli Backend (1-2 həftə)**
- [ ] Satıcı API endpointləri
- [ ] Məhsul CRUD əməliyyatları
- [ ] Sifariş idarəetməsi
- [ ] Analitika API

### **Faza 4: Ödəniş və Sifariş (2 həftə)**
- [ ] Ödəniş inteqrasiyası (Stripe, PayPal)
- [ ] Checkout prosesi
- [ ] Sifariş idarəetməsi
- [ ] Email bildirişləri

### **Faza 5: Əlavə Xüsusiyyətlər (2 həftə)**
- [ ] Rəy sistemi
- [ ] Axtarış və filtrlər
- [ ] İstifadəçi profili
- [ ] Admin panel

### **Faza 6: Test və Deploy (1-2 həftə)**
- [ ] Unit testlər
- [ ] İnteqrasiya testləri
- [ ] Performans testləri
- [ ] Production deploy
- [ ] Monitoring qurulması

---

## 🛠️ Texniki Tələblər

### Frontend Tələblər:
- Modern brauzer dəstəyi (Chrome, Firefox, Safari, Edge)
- Responsive dizayn (mobil, tablet, desktop)
- SEO optimizasiyası
- Accessibility (WCAG 2.1)
- PWA xüsusiyyətləri (optional)

### Backend Tələblər:
- RESTful API dizaynı
- API dokumentasiyası (Swagger/OpenAPI)
- Verilənlər bazası backup
- Error logging
- Monitoring və analytics

---

## 📈 Performans Hədəfləri

- **Page Load Time:** < 3 saniyə
- **API Response Time:** < 200ms
- **Database Query Time:** < 50ms
- **Uptime:** 99.9%
- **Concurrent Users:** 1000+

---

## 🚀 Deployment Strategiyası

### Hosting Variantları:

**Frontend:**
- Vercel
- Netlify
- AWS S3 + CloudFront
- GitHub Pages

**Backend:**
- Heroku
- AWS EC2
- DigitalOcean
- Railway
- Render

**Database:**
- AWS RDS
- MongoDB Atlas
- Supabase
- PlanetScale

---

## 📚 Əlavə Resurslar

### Lazım olan Toolkit:
- Git & GitHub
- Postman (API test)
- VS Code
- Browser DevTools
- Database Management Tool

### Öyrənilməli Texnologiyalar:
- REST API dizaynı
- JWT authentication
- SQL/NoSQL verilənlər bazaları
- File upload və storage
- Email göndərmə xidmətləri

---

## 📝 Qeydlər

### Hal-hazırda:
✅ Frontend əsas strukturu hazırdır
✅ Satıcı paneli UI tamamdır
✅ Əsas JavaScript funksiyaları işləyir

### Növbəti Addımlar:
1. Backend texnologiya seçimi
2. Database dizaynı
3. API development başlanğıcı
4. Frontend-Backend inteqrasiyası

---

## 👥 Komanda və Məsuliyyətlər

### Roller:
- **Frontend Developer:** UI/UX implementasiya
- **Backend Developer:** API və database
- **Full-Stack Developer:** Hər iki tərəf
- **Designer:** UI/UX dizayn
- **Tester:** Keyfiyyət nəzarəti

---

## 📞 Əlaqə və Dəstək

Bu dokumentasiya layihənin texniki blueprint-dir. Hər bir fazada yeniləmələr ediləcək.

**Versiya Tarixçəsi:**
- v1.0 - 28 Dekabr 2025 - İlkin dokumentasiya

---

**Son Yeniləmə:** 28 Dekabr 2025
**Status:** 🟢 Aktiv İnkişaf
