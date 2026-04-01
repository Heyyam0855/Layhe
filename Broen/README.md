# Broen Lab — Tibbi Laboratoriya Veb Platforması

## Layihə Haqqında
**Broen Lab** — Django + Django REST Framework ilə yazılmış tam funksional **tibbi laboratoriya xidməti veb saytıdır**.
Şirkət məlumatları, xidmətlər kataloqu, komanda üzvləri, FAQ, əlaqə formu və newsletter abunəliyi funksiyalarını ehtiva edir.

## Texnologiyalar
| Texnologiya | İstifadə |
|-------------|----------|
| **Python 3** | Backend proqramlaşdırma dili |
| **Django 5.2.7** | Veb framework |
| **Django REST Framework 3.16** | REST API yaratma |
| **django-cors-headers** | CORS konfiqurasiya |
| **django-filter** | API filterləmə |
| **Pillow** | Şəkil emalı |
| **SQLite3** | Verilənlər bazası |
| **HTML5** | Frontend şablonlar |
| **CSS3** | Responsive dizayn (1000+ sətir) |
| **JavaScript (ES6+)** | Dinamik frontend (600+ sətir) |
| **Font Awesome** | İkon kitabxanası |
| **Google Fonts (Poppins)** | Tipografiya |

## Layihə Strukturu
```
Broen/
├── broen_lab_backend/
│   ├── broen_lab/          # Django konfiqurasiya
│   │   ├── settings.py     # Layihə parametrləri
│   │   ├── urls.py         # Əsas URL routing + API
│   │   └── wsgi.py / asgi.py
│   ├── core/               # Əsas tətbiq
│   │   ├── models.py       # Company, Service, TeamMember, FAQ
│   │   ├── views.py        # REST API views + HTML view
│   │   ├── serializers.py  # DRF serializers
│   │   └── urls.py         # API endpoint-ləri
│   ├── contact/            # Əlaqə tətbiqi
│   │   ├── models.py       # ContactMessage, Newsletter, SocialMedia
│   │   ├── views.py        # Contact API + form handling
│   │   ├── serializers.py  # DRF serializers
│   │   └── urls.py         # Contact API endpoint-ləri
│   ├── tests/              # Test tətbiqi
│   ├── templates/
│   │   ├── base.html       # Əsas layout (header, footer, nav)
│   │   ├── home.html       # Ana səhifə (hero, services, team, FAQ)
│   │   └── test.html       # Test səhifəsi
│   ├── static/
│   │   ├── css/styles.css  # Tam responsive CSS (1000+ sətir)
│   │   └── js/script.js    # Frontend JS (600+ sətir)
│   ├── manage.py
│   └── requirements.txt
├── medical-lab-website/    # Alt layihə
├── Bosluq.md
├── my_project.md
└── unnamed.jpg
```

## API Endpoint-ləri
| Metod | URL | Təsvir |
|-------|-----|--------|
| GET | `/api/core/company/` | Şirkət məlumatları |
| GET | `/api/core/services/` | Xidmətlər siyahısı |
| GET | `/api/core/team/` | Komanda üzvləri |
| GET | `/api/core/faq/` | Tez-tez verilən suallar |
| GET | `/api/core/company-info/` | Birləşdirilmiş məlumat |
| POST | `/api/contact/messages/` | Əlaqə mesajı göndərmə |
| POST | `/api/contact/newsletter/` | Newsletter abunəlik |
| GET | `/api/contact/info/` | Əlaqə məlumatları |
| GET | `/api/contact/social/` | Sosial media linkləri |

## Django Modelləri

### Core App
- **Company** — Ad, təsvir, missiya, vizyon, ünvan, telefon, e-poçt, iş saatları, logo
- **Service** — Başlıq, təsvir, ikon, aktiv status, sıralama
- **TeamMember** — Ad, vəzifə (həkim/laborant/menecer/tibb bacısı), foto, təcrübə ili
- **FAQ** — Sual, cavab, aktiv status, sıralama

### Contact App
- **ContactMessage** — Ad, telefon, e-poçt, mövzu, test tipi, tarix, status (yeni/davam edir/həll edildi/bağlandı)
- **NewsletterSubscription** — E-poçt, aktiv status
- **ContactInfo** — Ad, dəyər, ikon
- **SocialMedia** — Platform (Facebook, Instagram, WhatsApp, LinkedIn, YouTube, Twitter, Telegram)

## Frontend Xüsusiyyətləri (JavaScript)
- Mobil menyu toggle
- FAQ accordion
- Əlaqə formu validation və göndərmə
- Bildiriş sistemi (notification)
- Smooth scrolling
- Sayğac animasiyaları (counter animation)
- Intersection Observer ilə görünüş animasiyaları
- "Yuxarı qayıt" düyməsi
- WhatsApp əlaqə inteqrasiyası
- Real-time form validation

## Necə İşə Salmaq
```bash
cd Broen/broen_lab_backend
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data    # Test məlumatları yüklə
python manage.py runserver
```
Brauzer: `http://127.0.0.1:8000/`

## Ölçü
~1.5 MB (venv qovluğu olmadan)
