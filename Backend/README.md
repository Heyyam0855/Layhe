# Backend — Django İstifadəçi İdarəetmə Sistemi

## Layihə Haqqında
Django framework ilə yazılmış **e-ticarət platforması üçün istifadəçi autentifikasiya sistemi** ("Mağaza").
Qeydiyyat, giriş, profil idarəetmə və admin panel funksiyalarını ehtiva edir.

## Texnologiyalar
| Texnologiya | İstifadə |
|-------------|----------|
| **Python 3.13** | Backend proqramlaşdırma dili |
| **Django** | Veb framework |
| **SQLite3** | Verilənlər bazası |
| **HTML5** | Şablon (template) faylları |
| **CSS3** | Səhifə dizaynı (inline styles) |

## Layihə Strukturu
```
Backend/
├── accounts/              # İstifadəçi tətbiqi
│   ├── views.py           # 8 view funksiyası
│   ├── models.py          # UserProfile modeli
│   ├── forms.py           # 4 Django form
│   ├── urls.py            # URL routing (8 endpoint)
│   ├── admin.py           # Admin paneli qeydiyyatı
│   └── templates/accounts/
│       ├── index.html         # Ana səhifə (e-ticarət)
│       ├── login.html         # Giriş səhifəsi
│       ├── register.html      # Qeydiyyat səhifəsi
│       ├── admin_panel.html   # Admin panel
│       └── forgot_password.html # Şifrə sıfırlama
├── config/                # Django konfiqurasiya
│   ├── settings.py        # Layihə parametrləri
│   ├── urls.py            # Əsas URL routing
│   ├── wsgi.py            # WSGI server
│   └── asgi.py            # ASGI server
└── static/                # Statik fayllar
```

## Əsas Funksiyalar
1. **Qeydiyyat** — E-poçt, ad, soyad ilə yeni hesab yaratma
2. **Giriş/Çıxış** — E-poçt əsaslı autentifikasiya
3. **Profil** — İstifadəçi məlumatlarını redaktə etmə (telefon, ünvan, doğum tarixi)
4. **Admin Panel** — İstifadəçi axtarışı və idarəetmə
5. **Şifrə Sıfırlama** — Unudulmuş şifrəni bərpa etmə
6. **Data Fayl** — İstifadəçi məlumatlarının data.txt faylına yazılması

## Kodlar İzahı

### models.py - UserProfile Modeli
- Django `User` modeli ilə `OneToOneField` əlaqəsi
- Sahələr: ad, soyad, telefon, ünvan, doğum tarixi
- `save()` zamanı avtomatik data.txt-ə yazılır
- Signal ilə yeni istifadəçi yarandıqda profil avtomatik yaranır

### views.py - View Funksiyaları
- `register_view()` — Form validation + hesab yaratma
- `login_view()` — E-poçta görə istifadəçi tapıb authenticate etmə
- `profile_view()` — `@login_required` dekoratorlu profil idarəetmə
- `admin_panel_view()` — `@staff_member_required` ilə admin girişi

### forms.py - Django Formları
- `UserRegistrationForm` — Şifrə təsdiqləməli qeydiyyat formu
- `UserLoginForm` — E-poçt sahəli giriş formu

## Necə İşə Salmaq
```bash
cd Backend
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Brauzer: `http://127.0.0.1:8000/`

## Ölçü
~150 KB (venv qovluğu olmadan)

## Dil
- Kod və interfeys: **Azərbaycan dili**
- Timezone: Asia/Baku
