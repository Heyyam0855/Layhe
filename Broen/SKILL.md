# SKILL — Broen Lab (Tibbi Laboratoriya Platforması)

## Öyrənilən Texnologiyalar və Bacarıqlar

### Python / Django
- Django layihə strukturu (`startproject`, `startapp`)
- Çoxlu model yaratma (Company, Service, TeamMember, FAQ, ContactMessage...)
- Model sahə tipləri: `CharField`, `TextField`, `ImageField`, `BooleanField`, `IntegerField`, `DateTimeField`, `URLField`, `EmailField`
- Model `choices` istifadəsi (status, platform, position)
- `ordering`, `verbose_name`, `__str__` meta konfiqurasiya
- Management commands (`seed_data.py`)
- Static və media faylların konfiqurasiyası

### Django REST Framework (DRF)
- `ModelSerializer` ilə serializer yaratma
- `ListAPIView`, `CreateAPIView` ilə API view-lar
- `@api_view` dekoratoru ilə function-based API
- `django-filter` ilə queryset filterləmə
- CORS konfiqurasiya (`django-cors-headers`)
- API response formatlaşdırma (`Response`, `status`)

### HTML5 / Template
- Django template inheritance (`{% extends "base.html" %}`)
- Template tag-lar: `{% block %}`, `{% load static %}`, `{% url %}`
- Responsive navigation (hamburger menu)
- Semantic HTML: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- Font Awesome ikon inteqrasiyası
- Google Fonts yükləmə

### CSS3
- CSS Custom Properties (dəyişənlər): `--primary-color`, `--shadow-md`
- Flexbox və CSS Grid layout
- Media queries ilə responsive design
- Keyframe animasiyalar (`@keyframes fadeInUp`)
- Transition effektləri
- Gradient backgrounds
- Box-shadow, border-radius dizayn
- Hover və active state-lər

### JavaScript (ES6+)
- DOM manipulation: `querySelector`, `querySelectorAll`, `addEventListener`
- Fetch API ilə REST API çağırışları
- `async/await` pattern
- Intersection Observer API (scroll animasiyalar)
- Form validation (real-time)
- Dynamic HTML injection (`innerHTML`)
- Event delegation
- Error handling (`try/catch`)
- `setTimeout`, `setInterval` istifadəsi

### Layihə İdarəetmə
- `requirements.txt` ilə asılılıq idarəetmə
- Django admin paneli konfiqurasiya
- Test yazma əsasları
- URL namespace və routing
- Statik fayl versiyalaşdırma (`?v=2.1`)
