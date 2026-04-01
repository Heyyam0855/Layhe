# BRO-EN Laboratoriya - Tam Layihə Dokumentasiyası

## 📋 Layihə Haqqında
BRO-EN Laboratoriya veb saytı - Bakıda fəaliyyət göstərən tibbi laboratoriya üçün tam funksional veb sayt.

## 🗂️ Layihə Strukturu

```
medical-lab-website/
│
├── index.html          # Ana səhifə
├── tests.html          # Testlər səhifəsi
├── prices.html         # Qiymətlər səhifəsi
├── about.html          # Haqqımızda səhifəsi
├── contact.html        # Əlaqə səhifəsi
├── my_project.md       # Bu fayl
│
├── css/
│   └── styles.css      # Əsas CSS faylı
│
└── js/
    └── script.js       # Əsas JavaScript faylı
```

---

## 🎨 CSS - Vizual Dizayn və Stillər

### 1. CSS Variables (Dəyişənlər)
```css
:root {
    --primary-color: #2196F3;      /* Əsas mavi rəng */
    --secondary-color: #F44336;     /* Qırmızı-narıncı */
    --accent-color: #03A9F4;        /* Açıq mavi */
    --success-color: #FF5722;       /* Açıq qırmızı-narıncı */
    --text-primary: #2C3E50;        /* Əsas mətn rəngi */
    --text-secondary: #7F8C8D;      /* İkinci mətn rəngi */
    --bg-light: #F8F9FA;            /* Açıq fon */
    --border-radius: 8px;           /* Border radius */
    --transition: all 0.3s ease;    /* Animasiya */
}
```

**İzahat**: Bu dəyişənlər bütün layihədə istifadə olunan rəng və stil parametrlərini saxlayır. Dəyişiklik etdikdə yalnız bir yerdə dəyişdirmək kifayətdir.

### 2. Reset & Base Styles
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

**İzahat**: Bütün elementlərin default margin və padding-lərini sıfırlayır. `box-sizing: border-box` border və padding-in element ölçüsünə daxil olmasını təmin edir.

### 3. Navigation Header (Naviqasiya)
```css
.header {
    position: fixed;           /* Səhifə scroll olarkən yuxarıda qalır */
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;            /* Digər elementlərin üstündə qalır */
    background: var(--bg-white);
    box-shadow: var(--shadow-light);
}
```

**İzahat**: 
- `position: fixed` - Header daim ekranın yuxarısında qalır
- `z-index: 1000` - Header bütün digər elementlərin üstündə görünür
- `box-shadow` - Yumşaq kölgə effekti

### 4. Logo Dizaynı
```css
.logo {
    width: 50px;
    height: 50px;
    border-radius: var(--border-radius);
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    position: relative;
    overflow: hidden;
}

.logo::before {
    content: '';
    position: absolute;
    background: repeating-linear-gradient(
        45deg,
        rgba(255,255,255,0.1) 0px,
        rgba(255,255,255,0.1) 2px,
        transparent 2px,
        transparent 8px
    );
}
```

**İzahat**:
- `linear-gradient` - Rəng keçidi effekti
- `::before` pseudo-element - Diagonal xətlər pattern yaradır
- `repeating-linear-gradient` - Təkrarlanan xətlər pattern

### 5. Mobile Menu (Hamburger)
```css
.nav-toggle {
    display: none;              /* Desktop-də gizlidir */
    flex-direction: column;
    gap: 4px;
}

@media (max-width: 768px) {
    .nav-toggle {
        display: flex;          /* Mobile-də görünür */
    }
    
    .nav-menu {
        display: none;          /* Default olaraq gizli */
        position: absolute;
        top: 100%;
        background: var(--bg-white);
    }
    
    .nav-menu.active {
        display: flex;          /* Click edildikdə görünür */
    }
}
```

**İzahat**:
- Media query ilə ekran ölçüsünə görə dəyişikliklər
- `.active` class-ı JavaScript ilə toggle olunur

### 6. Hero Section Animasiyası
```css
@keyframes float {
    0%, 100% { 
        transform: translateY(20px); 
    }
    50% { 
        transform: translateY(0); 
    }
}

.hero-card {
    animation: float 6s ease-in-out infinite;
}
```

**İzahat**:
- `@keyframes` - Animasiya keyframe-lərini müəyyən edir
- `infinite` - Animasiya daim təkrarlanır
- `ease-in-out` - Yumşaq başlanğıc və son

### 7. Grid Layout Sistemi
```css
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}
```

**İzahat**:
- `display: grid` - CSS Grid istifadə edir
- `auto-fit` - Avtomatik olaraq sütun sayını müəyyən edir
- `minmax(250px, 1fr)` - Minimum 250px, maksimum bərabər bölgü

### 8. Card Hover Effekti
```css
.service-card {
    transition: var(--transition);
}

.service-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-medium);
    border-color: var(--primary-color);
}
```

**İzahat**:
- `transform: translateY(-5px)` - Kartı 5px yuxarı qaldırır
- `:hover` - Mouse üzərinə gəldikdə aktiv olur
- `transition` - Animasiyanı yumşaq edir

### 9. Responsive Typography
```css
h1 {
    font-size: 2.5rem;
}

@media (max-width: 768px) {
    h1 {
        font-size: 2rem;      /* Mobil üçün kiçik */
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: 1.8rem;    /* Çox kiçik ekranlar üçün */
    }
}
```

**İzahat**: Ekran ölçüsünə görə font ölçüləri avtomatik dəyişir.

---

## 💻 JavaScript - İnteraktiv Funksionallıq

### 1. Mobile Menu Toggle
```javascript
const mobileMenu = document.getElementById('mobile-menu');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenu && navMenu) {
    mobileMenu.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');
        navMenu.classList.toggle('active');
    });
}
```

**İzahat**:
- `getElementById` - ID ilə element seçir
- `addEventListener` - Click event dinləyir
- `classList.toggle` - Class-ı əlavə/silir

**İşləmə prinsipi**:
1. İstifadəçi hamburger menüyə klik edir
2. JavaScript `active` class-ını toggle edir
3. CSS `active` class-ı ilə menünu göstərir/gizlədir

### 2. Price Filter Funksionallığı
```javascript
const filterButtons = document.querySelectorAll('.filter-btn');
const priceTables = document.querySelectorAll('.price-table');

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Bütün buttonlardan active class-ını sil
        filterButtons.forEach(btn => btn.classList.remove('active'));
        
        // Click olunan buttona active class əlavə et
        button.classList.add('active');
        
        // Data attribute-u oxu
        const category = button.getAttribute('data-category');
        
        // Cədvəlləri filter et
        priceTables.forEach(table => {
            if (category === 'all') {
                table.style.display = 'block';
            } else if (table.getAttribute('data-category') === category) {
                table.style.display = 'block';
            } else {
                table.style.display = 'none';
            }
        });
    });
});
```

**İzahat**:
- `querySelectorAll` - Bütün uyğun elementləri seçir
- `forEach` - Hər element üçün döngü
- `getAttribute` - HTML data attribute-u oxuyur
- `style.display` - Element-in görünməsini idarə edir

**İşləmə prinsipi**:
1. İstifadəçi filter buttonuna klik edir
2. Button-dan kateqoriyanı oxuyur (`data-category`)
3. Bütün cədvəlləri yoxlayır
4. Uyğun kateqoriyalı cədvəlləri göstərir, digərlərini gizlədir

### 3. FAQ Accordion
```javascript
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    
    question.addEventListener('click', () => {
        // Digər bütün FAQ-ları bağla
        faqItems.forEach(otherItem => {
            if (otherItem !== item) {
                otherItem.classList.remove('active');
            }
        });
        
        // Cari FAQ-ı toggle et
        item.classList.toggle('active');
    });
});
```

**İzahat**:
- Yalnız bir FAQ eyni vaxtda açıq ola bilər
- Click olunan FAQ toggle olunur
- Digərləri avtomatik bağlanır

**CSS ilə əlaqə**:
```css
.faq-answer {
    display: none;              /* Default gizli */
}

.faq-item.active .faq-answer {
    display: block;             /* Active olduqda görünür */
}
```

### 4. Form Validation
```javascript
const contactForm = document.querySelector('#contact-form');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();  // Formun default submit-ini dayandır
    
    // Form data-nı toplayır
    const formData = new FormData(contactForm);
    const formObject = {};
    
    for (let [key, value] of formData.entries()) {
        formObject[key] = value;
    }
    
    // Validasiya
    const requiredFields = contactForm.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.style.borderColor = '#E74C3C';  // Qırmızı border
            
            // 3 saniyədən sonra normal border
            setTimeout(() => {
                field.style.borderColor = '#E9ECEF';
            }, 3000);
        }
    });
    
    // Email validasiyası
    const emailField = contactForm.querySelector('input[type="email"]');
    if (emailField && emailField.value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailField.value)) {
            isValid = false;
            emailField.style.borderColor = '#E74C3C';
        }
    }
    
    if (isValid) {
        showNotification('Mesajınız göndərildi!', 'success');
        contactForm.reset();
    } else {
        showNotification('Xahiş olunur sahələri düzgün doldurun.', 'error');
    }
});
```

**İzahat**:
- `e.preventDefault()` - Səhifənin reload olmasının qarşısını alır
- `FormData` - Form data-sını avtomatik toplayır
- `trim()` - Boşluqları silir
- `setTimeout` - Gec işləyən funksiya
- RegEx pattern - Email formatını yoxlayır

### 5. Notification System
```javascript
function showNotification(message, type = 'info') {
    // Köhnə notification-ı sil
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Yeni notification yarat
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span>${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;
    
    // Stil əlavə et
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: white;
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    // Rəngə görə background
    switch (type) {
        case 'success':
            notification.style.background = '#4CAF50';
            break;
        case 'error':
            notification.style.background = '#E74C3C';
            break;
        default:
            notification.style.background = '#FF6B35';
    }
    
    // DOM-a əlavə et
    document.body.appendChild(notification);
    
    // Animasiya
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Close button
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    });
    
    // 5 saniyədən sonra avtomatik bağlan
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}
```

**İzahat**:
- `createElement` - Yeni HTML elementi yaradır
- `innerHTML` - Element-in içəriğini təyin edir
- `appendChild` - Elementi DOM-a əlavə edir
- `switch` - Şərtlərə görä seçim
- İki `setTimeout` - Animasiya və avtomatik bağlanma üçün

### 6. Counter Animation
```javascript
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);  // 16ms = 60fps
    
    const updateCounter = () => {
        start += increment;
        if (start < target) {
            element.textContent = Math.floor(start).toLocaleString();
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target.toLocaleString();
        }
    };
    
    updateCounter();
}
```

**İzahat**:
- `requestAnimationFrame` - Browser-in refresh rate-inə uyğun animasiya
- `Math.floor` - Aşağı yuvarlaqlaşdırma
- `toLocaleString()` - Nömrələri format edir (50,000)
- Recursion - Funksiya özünü çağırır

### 7. Intersection Observer (Scroll Animasiyası)
```javascript
const observerOptions = {
    threshold: 0.1,              // Element 10% görünəndə
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const element = entry.target;
            
            // Counter animasiyası
            if (element.classList.contains('stat-number')) {
                const target = parseInt(element.textContent.replace(/[^\d]/g, ''));
                if (target && !element.classList.contains('animated')) {
                    element.classList.add('animated');
                    animateCounter(element, target);
                }
            }
            
            // Fade in animasiyası
            if (element.classList.contains('fade-in')) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        }
    });
}, observerOptions);

// Elementləri observe et
document.addEventListener('DOMContentLoaded', () => {
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        observer.observe(stat);
    });
});
```

**İzahat**:
- `IntersectionObserver` - Element-in görünməsini izləyir
- `threshold: 0.1` - Element 10% görünəndə trigger olur
- `isIntersecting` - Element viewport-da görünürsə true
- `DOMContentLoaded` - HTML tam yüklənəndə işə düşür

### 8. Back to Top Button
```javascript
const backToTopButton = document.createElement('button');
backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
backToTopButton.className = 'back-to-top';
backToTopButton.style.cssText = `
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    transform: translateY(100px);
    transition: all 0.3s ease;
`;

document.body.appendChild(backToTopButton);

// Scroll event
window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTopButton.style.transform = 'translateY(0)';
    } else {
        backToTopButton.style.transform = 'translateY(100px)';
    }
});

// Click event
backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
```

**İzahat**:
- `window.pageYOffset` - Scroll məsafəsini verir
- `scrollTo` - Səhifəni scroll edir
- `behavior: 'smooth'` - Yumşaq scroll animasiyası

### 9. Smooth Scrolling
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});
```

**İzahat**:
- `a[href^="#"]` - # ilə başlayan linklər
- `substring(1)` - # işarəsini silir
- `offsetTop` - Element-in top mövqeyini verir
- Header hündürlüyü çıxılır ki, element header altında qalmasın

---

## 📄 HTML Struktur İzahları

### 1. index.html - Ana Səhifə

#### Header (Naviqasiya)
```html
<header class="header">
    <nav class="navbar">
        <div class="nav-container">
            <!-- Logo -->
            <div class="nav-logo">
                <div class="logo">BRO</div>
                <h2>BRO-EN</h2>
            </div>
            
            <!-- Navigation Links -->
            <ul class="nav-menu">
                <li class="nav-item">
                    <a href="index.html" class="nav-link active">Ana Səhifə</a>
                </li>
                <!-- Digər linklər -->
            </ul>
            
            <!-- Mobile Hamburger Menu -->
            <div class="nav-toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>
</header>
```

**İzahat**:
- `header.header` - Sabit naviqasiya
- `.nav-logo` - Logo və şirkət adı
- `.nav-menu` - Desktop naviqasiya
- `.nav-toggle` - Mobile hamburger menu
- `active` class - Cari səhifəni işarələyir

#### Hero Section
```html
<section class="hero">
    <div class="hero-container">
        <!-- Sol tərəf: Mətn və buttonlar -->
        <div class="hero-content">
            <h1>Bakının Ən Etibarlı Tibbi Laboratoriyası</h1>
            <p>Yüksək keyfiyyətli analiz xidmətləri...</p>
            <div class="hero-buttons">
                <a href="tests.html" class="btn-primary">Testlərimiz</a>
                <a href="contact.html" class="btn-secondary">Əlaqə</a>
            </div>
        </div>
        
        <!-- Sağ tərəf: Animasiyalı kart -->
        <div class="hero-image">
            <div class="hero-card">
                <i class="fas fa-microscope"></i>
                <h3>Dəqiq Nəticələr</h3>
            </div>
        </div>
    </div>
</section>
```

**İzahat**:
- Grid layout - İki sütunlu düzüm
- `.hero-card` - Float animasiyası ilə
- CTA buttonları - İstifadəçini hərəkətə keçirir

#### Features Grid
```html
<section class="features">
    <div class="container">
        <h2 class="section-title">Nə üçün Bizə Güvənmək Lazımdır?</h2>
        <div class="features-grid">
            <!-- Feature Card -->
            <div class="feature-card">
                <div class="feature-icon">
                    <i class="fas fa-clock"></i>
                </div>
                <h3>Sürətli Nəticə</h3>
                <p>Testlərin nəticələri 1-3 iş günü ərzində hazır olur</p>
            </div>
            <!-- Digər kartlar... -->
        </div>
    </div>
</section>
```

**İzahat**:
- Auto-fit grid - Responsiv bölgü
- Font Awesome ikonlar
- Hover effektləri ilə kartlar

### 2. tests.html - Testlər Səhifəsi

#### Test Category Structure
```html
<div id="blood-tests" class="test-category">
    <!-- Kateqoriya başlığı -->
    <div class="category-header">
        <div class="category-icon">
            <i class="fas fa-tint"></i>
        </div>
        <div class="category-info">
            <h2>Qan Analizləri</h2>
            <p>Ümumi və xüsusi qan analizləri...</p>
        </div>
    </div>
    
    <!-- Test kartları -->
    <div class="tests-grid">
        <div class="test-card">
            <div class="test-header">
                <h3>Ümumi Qan Analizi</h3>
                <span class="test-price">15 AZN</span>
            </div>
            
            <!-- Test parametrləri -->
            <ul class="test-parameters">
                <li>Hemoglobin</li>
                <li>Eritrositlər</li>
                <li>Leykotsitlər</li>
            </ul>
            
            <!-- Test məlumatları -->
            <div class="test-info">
                <span class="test-time">
                    <i class="fas fa-clock"></i> 1 gün
                </span>
                <span class="test-prep">
                    <i class="fas fa-info-circle"></i> Hazırlıq tələb olunmur
                </span>
            </div>
        </div>
    </div>
</div>
```

**İzahat**:
- `id="blood-tests"` - Anchor link üçün
- Qiymət, müddət və hazırlıq məlumatları
- Grid layout ilə responsive dizayn

### 3. prices.html - Qiymətlər Səhifəsi

#### Filter System
```html
<section class="price-filter">
    <div class="container">
        <div class="filter-buttons">
            <button class="filter-btn active" data-category="all">
                Hamısı
            </button>
            <button class="filter-btn" data-category="blood">
                Qan Analizləri
            </button>
            <!-- Digər filterlər... -->
        </div>
    </div>
</section>
```

**İzahat**:
- `data-category` - JavaScript üçün identifier
- `active` class - Seçilmiş filter
- Click event ilə cədvəllər filter olunur

#### Price Table
```html
<div class="price-table blood" data-category="blood">
    <div class="table-header">
        <h2><i class="fas fa-tint"></i> Qan Analizləri</h2>
    </div>
    
    <div class="price-list">
        <div class="price-item">
            <div class="test-info">
                <h4>Ümumi Qan Analizi</h4>
                <p>Hemoglobin, Eritrositlər...</p>
            </div>
            <div class="price-details">
                <span class="price">15 AZN</span>
                <span class="duration">1 gün</span>
            </div>
        </div>
    </div>
</div>
```

**İzahat**:
- `data-category` - Filter üçün
- Flexbox layout - Test adı və qiymət yan-yana
- JavaScript ilə show/hide

#### Package Cards
```html
<div class="package-card popular">
    <div class="popular-badge">Populyar</div>
    
    <div class="package-header">
        <h3>Diabet Yoxlama Paketi</h3>
        <div class="package-price">
            <span class="old-price">180 AZN</span>
            <span class="new-price">140 AZN</span>
        </div>
    </div>
    
    <ul class="package-tests">
        <li><i class="fas fa-check"></i> Qlükoza</li>
        <li><i class="fas fa-check"></i> HbA1c</li>
        <!-- Digər testlər... -->
    </ul>
    
    <div class="package-discount">
        <span class="discount-badge">22% endim</span>
    </div>
</div>
```

**İzahat**:
- `.popular` - Xüsusi stil üçün
- Köhnə və yeni qiymət - Endirim göstərmək üçün
- Check ikonları ilə test list

### 4. about.html - Haqqımızda Səhifəsi

#### Team Members
```html
<div class="team-member">
    <div class="member-photo">
        <div class="photo-placeholder">
            <i class="fas fa-user-md"></i>
        </div>
    </div>
    
    <div class="member-info">
        <h4>Dr. Aynur Əliyeva</h4>
        <p class="position">Baş Həkim</p>
        <p class="experience">20 illik təcrübə</p>
        
        <div class="member-qualifications">
            <span class="qualification">PhD</span>
            <span class="qualification">ISO Sertifikat</span>
        </div>
    </div>
</div>
```

**İzahat**:
- Placeholder ikon - Şəkil əvəzinə
- Qualification badge-ləri
- Grid layout ilə responsive

#### Mission & Vision Cards
```html
<div class="mv-item">
    <div class="mv-icon">
        <i class="fas fa-bullseye"></i>
    </div>
    <h3>Missiyamız</h3>
    <p>Ən yüksək keyfiyyətli...</p>
</div>
```

**İzahat**:
- Gradient background ikonlar
- Center alignment
- Box shadow ilə kart effekti

### 5. contact.html - Əlaqə Səhifəsi

#### Contact Cards
```html
<div class="contact-card">
    <div class="contact-icon">
        <i class="fas fa-phone"></i>
    </div>
    <h3>Telefon</h3>
    <div class="contact-details">
        <p><a href="tel:+994125555555">+994 12 555 55 55</a></p>
        <p class="note">24/7 dəstək xətti</p>
    </div>
</div>
```

**İzahat**:
- `tel:` - Telefon linki
- `mailto:` - Email linki
- Hover effekti ilə interaktiv

#### Contact Form
```html
<form class="contact-form" id="main-contact-form">
    <!-- İki sütunlu input -->
    <div class="form-row">
        <div class="form-field">
            <label for="firstName">Ad</label>
            <input type="text" id="firstName" name="firstName" required>
        </div>
        <div class="form-field">
            <label for="lastName">Soyad</label>
            <input type="text" id="lastName" name="lastName" required>
        </div>
    </div>
    
    <!-- Select dropdown -->
    <div class="form-group">
        <label for="subject">Mövzu</label>
        <select id="subject" name="subject" required>
            <option value="">Mövzu seçin</option>
            <option value="appointment">Randevu alma</option>
            <!-- Digər optionlar... -->
        </select>
    </div>
    
    <!-- Checkbox -->
    <div class="checkbox-group">
        <input type="checkbox" id="privacy" name="privacy" required>
        <label for="privacy">
            Məxfilik siyasətini qəbul edirəm
        </label>
    </div>
    
    <button type="submit" class="btn-primary submit-btn">
        <i class="fas fa-paper-plane"></i>
        Mesaj Göndər
    </button>
</form>
```

**İzahat**:
- `required` attribute - HTML5 validasiya
- Grid layout - Responsive form
- JavaScript ilə əlavə validasiya

#### FAQ Accordion
```html
<div class="faq-item">
    <div class="faq-question">
        <h4>Test üçün necə hazırlaşmalıyam?</h4>
        <i class="fas fa-plus"></i>
    </div>
    <div class="faq-answer">
        <p>Qan analizləri üçün 8-12 saat acqarına...</p>
    </div>
</div>
```

**İzahat**:
- Click event ilə toggle
- CSS-də `.active` class ilə göstər/gizlə
- Plus ikonu rotate olur

---

## 🎯 Əsas Konseptlər və Texnikalar

### 1. BEM Naming Convention (İstifadə olunmur, lakin faydalıdır)
```
Block__Element--Modifier

Nümunə:
.card__title--large
.button--primary
```

### 2. CSS Grid vs Flexbox

**Grid - İki ölçülü layout**
```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```

**Flexbox - Bir ölçülü layout**
```css
.flex-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

### 3. JavaScript Event Delegation
```javascript
// Pis üsul - Hər elementə event
buttons.forEach(btn => {
    btn.addEventListener('click', handler);
});

// Yaxşı üsul - Parent-ə bir event
parent.addEventListener('click', (e) => {
    if (e.target.classList.contains('button')) {
        handler(e);
    }
});
```

### 4. CSS Custom Properties (Variables) Avantajları
```css
/* Bir yerdə dəyişiklik */
:root {
    --primary: #2196F3;
}

/* JavaScript ilə dəyişdirmək mümkündür */
document.documentElement.style.setProperty('--primary', '#FF0000');
```

### 5. Responsive Design Strategyası
```
Mobile First Approach:
1. Əvvəlcə mobil dizayn
2. Sonra tablet (768px+)
3. Sonra desktop (1024px+)

@media (min-width: 768px) {
    /* Tablet və yuxarı */
}
```

---

## 🚀 Performance Optimizasiyası

### 1. CSS Optimization
```css
/* Pis */
.element {
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
}

/* Yaxşı - Dəyişənlə */
.element {
    box-shadow: var(--shadow-light);
}
```

### 2. JavaScript Performance
```javascript
// Pis - DOM query hər dəfə
for (let i = 0; i < 100; i++) {
    document.querySelector('.item').innerHTML = i;
}

// Yaxşı - Cache edilmiş
const item = document.querySelector('.item');
for (let i = 0; i < 100; i++) {
    item.innerHTML = i;
}
```

### 3. Image Optimization
```html
<!-- Lazy loading -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Responsive images -->
<img srcset="small.jpg 300w, medium.jpg 600w, large.jpg 900w"
     sizes="(max-width: 600px) 300px, (max-width: 900px) 600px, 900px"
     src="medium.jpg" alt="Description">
```

---

## 📱 Responsive Breakpoints

```css
/* Mobile: 0-767px (default) */

/* Tablet: 768px+ */
@media (min-width: 768px) {
    .container {
        max-width: 720px;
    }
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
    .container {
        max-width: 960px;
    }
}

/* Large Desktop: 1200px+ */
@media (min-width: 1200px) {
    .container {
        max-width: 1140px;
    }
}
```

---

## 🔧 Debugging Tips

### 1. Console Logging
```javascript
// Dəyərləri yoxla
console.log('Variable:', myVariable);

// Obyekti yoxla
console.table(myObject);

// Performans ölçümü
console.time('Operation');
// ... kod ...
console.timeEnd('Operation');
```

### 2. CSS Debugging
```css
/* Border ilə layout-u gör */
* {
    border: 1px solid red;
}

/* Grid lines-ı gör */
.grid {
    display: grid;
    gap: 1rem;
    /* DevTools-da grid overlay aktivləşdir */
}
```

---

## 📚 Əlavə Resurslar

### Faydalı Linklər:
- MDN Web Docs: https://developer.mozilla.org
- CSS Tricks: https://css-tricks.com
- Can I Use: https://caniuse.com
- Font Awesome: https://fontawesome.com

### Tövsiyə olunan kitablar:
- "You Don't Know JS" - Kyle Simpson
- "CSS Secrets" - Lea Verou
- "JavaScript: The Good Parts" - Douglas Crockford

---

## ✅ Checklist - Yeni Feature Əlavə edərkən

1. ☐ HTML struktur düzgündür
2. ☐ CSS responsive dizayn
3. ☐ JavaScript event-lər təmiz
4. ☐ Form validasiya işləyir
5. ☐ Mobile-də test edilib
6. ☐ Browser compatibility yoxlanılıb
7. ☐ Performance optimize edilib
8. ☐ Accessibility (a11y) nəzərə alınıb
9. ☐ SEO friendly
10. ☐ Kod comment-ləri əlavə edilib

---

## 🎓 Layihədən Öyrənilənlər

### HTML:
- Semantic HTML5 elementləri
- Form structure və validasiya
- Accessibility attributes
- SEO best practices

### CSS:
- Modern layout (Grid, Flexbox)
- CSS Variables
- Animations və Transitions
- Responsive design
- Mobile-first approach

### JavaScript:
- DOM manipulation
- Event handling
- Form validation
- API concepts (hazırda mock)
- Modern ES6+ syntax
- Async operations

---

## 📝 Gələcək Təkmilləşdirmələr

### Backend Integration:
```javascript
// Form submit - Backend API-yə göndər
async function submitForm(formData) {
    try {
        const response = await fetch('https://api.broen.az/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}
```

### Database Structure:
```sql
-- Tests cədvəli
CREATE TABLE tests (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10,2),
    duration VARCHAR(50),
    parameters JSON,
    created_at TIMESTAMP
);

-- Appointments cədvəli
CREATE TABLE appointments (
    id INT PRIMARY KEY,
    patient_name VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255),
    test_id INT,
    date DATE,
    time TIME,
    status VARCHAR(50),
    FOREIGN KEY (test_id) REFERENCES tests(id)
);
```

### React/Vue Integration:
```javascript
// Vue.js komponent nümunəsi
export default {
    name: 'TestCard',
    props: {
        test: Object
    },
    template: `
        <div class="test-card">
            <h3>{{ test.name }}</h3>
            <p>{{ test.description }}</p>
            <span class="price">{{ test.price }} AZN</span>
        </div>
    `
}
```

---

## 🏁 Nəticə

Bu layihə tam funksional, responsive və modern bir tibbi laboratoriya veb saytıdır. Bütün əsas web development konseptlərini əhatə edir və real dünya proyektlərində istifadə üçün hazırdır.

**Əsas Xüsusiyyətlər:**
✅ Tam responsive dizayn
✅ Modern CSS (Grid, Flexbox, Animations)
✅ Interactive JavaScript funksionallıq
✅ Form validation
✅ Accessibility friendly
✅ SEO optimized
✅ Clean və maintainable kod

**Təkmilləşdirmə imkanları:**
🔄 Backend integration
🔄 Database əlaqəsi
🔄 User authentication
🔄 Online ödəniş sistemi
🔄 Test nəticələri paneli
🔄 Admin panel

Bu dokumentasiya layihəni başa düşmək və genişləndirmək üçün tam bələdçidir.
