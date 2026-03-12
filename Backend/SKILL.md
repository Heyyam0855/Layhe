# SKILL — Backend (Django Autentifikasiya)

## Öyrənilən Texnologiyalar və Bacarıqlar

### Python / Django
- Django proyekt yaratma (`startproject`, `startapp`)
- Model yaratma (`models.Model`, `OneToOneField`, `signals`)
- Form yaratma (`forms.Form`, `forms.ModelForm`)
- View funksiyaları (`render`, `redirect`, `authenticate`, `login`)
- URL routing (`path`, `include`)
- Template sistemi (`{% extends %}`, `{% block %}`, `{% csrf_token %}`)
- Django admin paneli qeydiyyatı
- Dekoratorlar: `@login_required`, `@staff_member_required`
- Migration sistemi (`makemigrations`, `migrate`)

### HTML/CSS
- Django template dili ilə dinamik HTML
- Form rendering (`{{ form.as_p }}`)
- Responsive dizayn (inline CSS)
- Şərti göstərmə (`{% if user.is_authenticated %}`)

### Verilənlər Bazası
- SQLite3 ile işləmə
- Django ORM: `filter()`, `get()`, `create()`, `save()`
- Migration ilə sxem idarəetmə

### Autentifikasiya
- `django.contrib.auth` sistemi
- E-poçt əsaslı giriş (standart username əvəzinə)
- Şifrə hash-ləmə
- Session idarəetmə
- Login/Logout redirect konfiqurasiya

### Fayl Sistemi
- Python ilə fayl oxuma/yazma (`open()`, `read()`, `write()`)
- UserProfile `save()` override ilə avtomatik data export
