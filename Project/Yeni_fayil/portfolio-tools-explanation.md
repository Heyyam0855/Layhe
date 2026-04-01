# Portfolio Veb Saytı JavaScript Alətləri

Bu JavaScript faylları portfolio veb saytı üçün əsas funksionallığı təmin edən alətlərdir. Hər birinin funksiyasını izah edim:

## **utils.js** - Köməkçi Funksiyalar
Bu fayl ümumi istifadə olunan yardımçı funksiyaları saxlayır:

### DOM Əməliyyatları:
- Elementləri seçmək və yaratmaq
- Hadisə dinləyiciləri əlavə etmək
- Elementlərin görünən sahədə olub-olmadığını yoxlamaq

### Storage (Yaddaş):
- LocalStorage ilə məlumat saxlamaq və oxumaq
- Xəta hallarını idarə etmək

### Utility Funksiyaları:
- **debounce/throttle** - Funksiya çağırışlarını məhdudlaşdırır (performans üçün)
- **formatDate** - Tarix formatlaması
- **truncateText** - Uzun mətni qısaldır
- **isValidEmail** - Email doğrulaması
- **copyToClipboard** - Mətni buferə kopyalayır

### Animasiyalar:
- **countUp** - Rəqəmlərin animasiyalı sayılması
- **fadeIn/fadeOut** - Elementlərin yumşaq görünməsi/itməsi

### Tema İdarəsi:
- Qaranlıq/işıqlı tema arasında keçid
- Sistem temasına uyğunlaşma

## **api.js** - API Əlaqə Təbəqəsi
Backend ilə əlaqəni idarə edir:

### Əsas API Funksiyaları:
- GET, POST, PUT, DELETE sorğuları
- Avtorizasiya token idarəsi
- Fayl yükləmə

### Portfolio API:
- Layihələri əldə etmək
- Bacarıqları almaq
- İş təcrübəsini almaq
- Əlaqə formu göndərmək
- Axtarış funksiyası

### Admin API:
- Admin girişi/çıxışı
- CRUD əməliyyatları (Create, Read, Update, Delete)
- Statistika məlumatları

### Cache İdarəsi:
- Tez-tez istifadə olunan məlumatları müvəqqəti yadda saxlayır
- Performansı artırır və server yükünü azaldır

## **components.js** - UI Komponentləri
Təkrar istifadə oluna bilən vizual komponentlər:

### Modal:
- Pop-up pəncərələr yaradır
- Layihə detallarını göstərmək üçün

### Notification:
- Bildirişlər göstərir (uğur, xəta, xəbərdarlıq)
- Avtomatik itən mesajlar

### LoadingSpinner:
- Yükləmə göstəricisi
- Məlumat yüklənərkən istifadə olunur

### ProjectCard:
- Layihə kartlarını yaradır
- Şəkil, başlıq, təsvir və texnologiyaları göstərir

### SkillBadge:
- Bacarıq nişanları
- Faiz göstəricili səviyyə çubuqları

### ContactForm:
- Əlaqə formu komponenti
- Sahə doğrulaması
- Form göndərilməsi

### SearchComponent:
- Axtarış qutusu
- Real-vaxt axtarış nəticələri

## **main.js** - Əsas Tətbiq
Bütün komponentləri birləşdirir:

### Səhifə Yükləməsi:
- Səhifə tipini müəyyənləşdirir (Ana səhifə, Layihələr, Haqqında və s.)
- Müvafiq məzmunu yükləyir

### Komponent İnisializasiyası:
- Naviqasiya paneli
- Tema dəyişdiricisi
- Mobil menyu
- Yuxarı qayıtma düyməsi

### Səhifə Məzmunu:
- Ana səhifə: Seçilmiş layihələr, bacarıqlar, yazı animasiyası
- Layihələr: Filtrləmə funksiyası ilə layihə grid-i
- Bacarıqlar: Kateqoriyalara bölünmüş bacarıqlar
- Təcrübə: Zaman xətti komponenti

### Hadisə İdarəsi:
- Səhifə daxili keçidlər
- Form göndərilmələri
- Scroll hadisələri

### Animasiya:
- Intersection Observer ilə elementlərin görünəndə animasiyası
- Rəqəmlərin sayılması effekti

Bu fayllar birlikdə işləyərək:
1. **Performanslı** - Cache və optimizasiya
2. **İstifadəçi dostu** - Animasiyalar və bildirişlər
3. **Responsive** - Mobil uyğunluq
4. **Modular** - Təkrar istifadə oluna bilən komponentlər

yaradır və müasir bir portfolio veb saytı üçün tam funksional frontend təmin edir.
