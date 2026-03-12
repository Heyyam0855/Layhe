# BRO-EN Laboratoriya - Django Backend

BRO-EN Laboratoriyası üçün Django REST Framework ilə hazırlanmış tam funksional backend sistem.

## 🚀 Xüsusiyyətlər

### ✅ Hazır Funksionallıqlar

- **Tam funksional REST API**
  - Test kateqoriyaları və testlər
  - Qiymət idarəetməsi
  - Əlaqə formu və mesaj idarəetməsi
  - Newsletter abunəliyi
  - Şirkət məlumatları
  - Komanda üzvləri
  - FAQ sistemi

- **Güclü Admin Panel**
  - Django admin paneli tam konfiqurasiya edilib
  - Bütün modellər üçün custom admin interface
  - Axtarış, filtrlənmə və sıralama funksiyaları
  - Bulk actions və inline editing

- **Məlumat Bazası Modelləri**
  - Company (Şirkət məlumatları)
  - Service (Xidmətlər)
  - TeamMember (Komanda üzvləri)
  - FAQ (Suallar)
  - TestCategory (Test kateqoriyaları)
  - Test (Laboratoriya testləri)
  - TestPackage (Test paketləri)
  - ContactMessage (Əlaqə mesajları)
  - NewsletterSubscription (Newsletter)
  - ContactInfo (Əlaqə məlumatları)
  - SocialMedia (Sosial media hesabları)

## 📋 Tələblər

- Python 3.8+
- Django 5.2.7
- Django REST Framework 3.16.1
- PostgreSQL (istəyə bağlı, default SQLite)

## 🛠️ Quraşdırma

### 1. Repo-nu klonlayın

```bash
git clone <repo-url>
cd broen_lab_backend
```

### 2. Virtual environment yaradın

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# və ya
source venv/bin/activate  # Linux/Mac
```

### 3. Paketləri quraşdırın

```bash
pip install -r requirements.txt
```

### 4. Environment dəyişənləri

`.env` faylı yaradın (istəyə bağlı):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Migration-ları tətbiq edin

```bash
python manage.py migrate
```

### 6. Admin istifadəçisi yaradın

```bash
python manage.py createsuperuser
```

### 7. Başlanğıc məlumatları yükləyin

```bash
python manage.py seed_data
```

### 8. Serveri başladın

```bash
python manage.py runserver
```

Server `http://127.0.0.1:8000/` ünvanında işə düşəcək.

## 📚 API Endpoints

### Core (Əsas məlumatlar)

- `GET /api/core/company/` - Şirkət məlumatları
- `GET /api/core/services/` - Xidmətlər
- `GET /api/core/team/` - Komanda üzvləri
- `GET /api/core/faq/` - FAQ-lar
- `GET /api/core/company-info/` - Ana səhifə məlumatları

### Tests (Testlər)

- `GET /api/tests/` - Bütün testlər (filtrlənə bilər)
- `GET /api/tests/{id}/` - Test təfərrüatları
- `GET /api/tests/categories/` - Test kateqoriyaları
- `GET /api/tests/packages/` - Test paketləri
- `GET /api/tests/popular/` - Məşhur testlər
- `GET /api/tests/category/{category_type}/` - Kateqoriyaya görə testlər
- `GET /api/tests/prices/` - Qiymət cədvəli

**Filtrlənmə parametrləri:**
- `?category__category_type=blood` - Kateqoriyaya görə
- `?is_popular=true` - Məşhur testlər
- `?search=hemoglobin` - Axtarış
- `?ordering=price` - Sıralama

### Contact (Əlaqə)

- `POST /api/contact/message/` - Əlaqə mesajı göndər
- `POST /api/contact/newsletter/` - Newsletter abunəliyi
- `GET /api/contact/info/` - Əlaqə məlumatları
- `GET /api/contact/social/` - Sosial media hesabları
- `POST /api/contact/form-submit/` - Form göndərmə (frontend üçün)
- `POST /api/contact/newsletter-subscribe/` - Newsletter (frontend üçün)
- `GET /api/contact/page-data/` - Əlaqə səhifəsi məlumatları

## 🔐 Admin Panel

Admin panelə giriş: `http://127.0.0.1:8000/admin/`

Admin paneldə:
- Bütün məlumatları idarə edə bilərsiniz
- Testlər, qiymətlər, kateqoriyalar əlavə edə bilərsiniz
- Mesajları oxuyub cavablandıra bilərsiniz
- Newsletter abunəliklərini idarə edə bilərsiniz

## 📊 Məlumat Strukturu

### Test Modelində

```python
{
  "id": 1,
  "name": "Ümumi Qan Analizi",
  "code": "QAN001",
  "category": {...},
  "price": "15.00",
  "discount_price": null,
  "effective_price": "15.00",
  "has_discount": false,
  "is_popular": true,
  "description": "...",
  "sample_type": "Kapillyar və ya venoz qan",
  "result_time": "1 iş günü"
}
```

### Contact Message

```python
{
  "first_name": "Ad",
  "last_name": "Soyad",
  "phone": "+994501234567",
  "email": "email@example.com",
  "subject": "Mövzu",
  "test_type": "Qan analizi",
  "message": "Mesaj mətni"
}
```

## 🔧 Əlavə Əmrlər

### Static faylları yığmaq

```bash
python manage.py collectstatic
```

### Yeni migration yaratmaq

```bash
python manage.py makemigrations
```

### Database backup (SQLite)

```bash
cp db.sqlite3 db_backup_$(date +%Y%m%d).sqlite3
```

## 🌐 CORS Konfiqurasiyası

Frontend ilə işləmək üçün CORS artıq konfiqurasiya olunub:
- `http://localhost:3000`
- `http://127.0.0.1:3000`
- `http://localhost:8080`
- `http://127.0.0.1:8080`

## 📧 Email Konfiqurasiyası

Email göndərmə Gmail SMTP vasitəsilə konfiqurasiya olunub.

`settings.py`-də dəyişdirin:

```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

**Qeyd:** Gmail üçün 2-faktorlu autentifikasiya aktivdirsə, App Password istifadə edin.

## 🚀 Production üçün

### 1. Debug modunu söndürün

```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
```

### 2. SECRET_KEY-i dəyişin

```python
SECRET_KEY = 'your-secure-secret-key'
```

### 3. PostgreSQL istifadə edin

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'broen_lab',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Static faylları yığın

```bash
python manage.py collectstatic --noinput
```

### 5. Gunicorn quraşdırın

```bash
pip install gunicorn
gunicorn broen_lab.wsgi:application --bind 0.0.0.0:8000
```

## 📂 Layihə Strukturu

```
broen_lab_backend/
├── broen_lab/           # Əsas layihə qovluğu
│   ├── settings.py      # Konfiqurasiya
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI konfiqurasiyası
├── core/                # Core app (şirkət, xidmətlər, FAQ)
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── seed_data.py
├── tests/               # Tests app (testlər, paketlər)
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── contact/             # Contact app (mesajlar, newsletter)
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── static/              # Static fayllar (CSS, JS, images)
├── media/               # Upload olunan fayllar
├── templates/           # HTML template-lər
└── manage.py            # Django management script
```

## 🤝 Töhfə vermək

1. Fork edin
2. Feature branch yaradın (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add some amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📝 Lisenziya

Bu layihə [MIT License](LICENSE) altında paylanır.

## 👥 Müəlliflər

**BRO-EN Laboratoriya Development Team**

## 📞 Əlaqə

- Website: https://broen.az
- Email: info@broen.az
- Phone: +994 12 555-55-55

---

**Qeyd:** Bu backend sistem BRO-EN Laboratoriyası frontend layihəsi ilə inteqrasiya olunmaq üçün hazırlanıb.