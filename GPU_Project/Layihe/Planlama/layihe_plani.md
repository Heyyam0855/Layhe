# Personal Portfolio Layihəsi - İcra Planı

## Ümumi Məlumat
Bu plan GitHub Copilot və Sonnet 4 tərəfindən icra olunacaq personal portfolio layihəsinin ətraflı addımlarını təsvir edir.

## Mərhələlər və İcra Addımları

### MƏRHƏLƏ 1: LAYİHƏ QURULUŞU VƏ ÇEVRƏNİN HAZIRLANMASI (1-2 gün)

#### 1.1 Layihə Strukturunun Yaradılması
```
portfolio-project/
├── frontend/
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── skills.html
│   ├── experience.html
│   ├── contact.html
│   ├── css/
│   │   ├── main.css
│   │   ├── components.css
│   │   └── responsive.css
│   ├── js/
│   │   ├── main.js
│   │   ├── api.js
│   │   ├── components.js
│   │   └── utils.js
│   └── assets/
│       ├── images/
│       ├── icons/
│       └── fonts/
├── admin/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── projects.html
│   ├── skills.html
│   ├── experience.html
│   ├── messages.html
│   ├── settings.html
│   ├── css/
│   │   ├── admin.css
│   │   ├── dashboard.css
│   │   └── forms.css
│   ├── js/
│   │   ├── admin.js
│   │   ├── auth.js
│   │   ├── dashboard.js
│   │   ├── crud.js
│   │   └── utils.js
│   └── assets/
│       ├── images/
│       └── icons/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── admin_routes.py
│   ├── auth.py
│   ├── config.py
│   ├── requirements.txt
│   └── static/
├── docs/
└── README.md
```

**Copilot/Sonnet tapşırıqları:**
- [ ] Layihə qovluğu strukturunu yaradın
- [ ] Git repository başlatın və `.gitignore` faylını konfiqurasiya edin
- [ ] `README.md` faylını layihə təsviri ilə yaradın
- [ ] Frontend üçün boş HTML fayllarını yaradın (semantic structure ilə)
- [ ] Admin panel üçün HTML fayllarını yaradın (dashboard structure ilə)
- [ ] CSS fayllarını əsas strukturla yaradın (CSS Grid və Flexbox əsaslı)
- [ ] JavaScript modullarını boş template ilə yaradın
- [ ] Admin panel üçün ayrıca CSS və JS faylları yaradın

#### 1.2 Backend Mühitinin Qurulması
**Copilot/Sonnet tapşırıqları:**
- [ ] Python virtual environment yaradın və aktivləşdirin
- [ ] `requirements.txt` faylını Flask və lazım olan kitabxanalarla yaradın:
  ```txt
  Flask==2.3.3
  Flask-SQLAlchemy==3.0.5
  Flask-Mail==0.9.1
  Flask-WTF==1.1.1
  Flask-CORS==4.0.0
  Flask-Login==0.6.3
  Flask-Bcrypt==1.0.1
  Flask-JWT-Extended==4.5.2
  python-dotenv==1.0.0
  Pillow==10.0.0
  ```
- [ ] Flask application strukturunu qurduçu əsas `app.py` faylını yaradın
- [ ] Database modelləri üçün `models.py` yaradın
- [ ] API routes üçün `routes.py` yaradın
- [ ] Admin panel routes üçün `admin_routes.py` yaradın
- [ ] Authentication sistemi üçün `auth.py` yaradın
- [ ] Configuration üçün `config.py` yaradın

#### 1.3 İnkişaf Alətlərinin Konfiqurasiyası
**Copilot/Sonnet tapşırıqları:**
- [ ] VS Code workspace settings yaradın
- [ ] ESLint və Prettier konfiqurasiya fayllarını yaradın
- [ ] Live Server və ya Vite konfiqurasiyasını qurın
- [ ] Browser DevTools üçün source maps konfiqurasiyasını hazırlayın

### MƏRHƏLƏ 2: BACKEND İNKİŞAFI (3-4 gün)

#### 2.1 Database Modellərinin Yaradılması
**Copilot/Sonnet tapşırıqları:**
- [ ] `Contact` modeli yaradın (ad, email, mesaj, tarix)
- [ ] `Project` modeli yaradın (başlıq, təsvir, texnologiyalar, linkler, şəkillər)
- [ ] `Skill` modeli yaradın (ad, kateqoriya, səviyyə, icon)
- [ ] `Experience` modeli yaradın (şirkət, vəzifə, başlama/bitmə tarixi, təsvir)
- [ ] `User` modeli yaradın (admin authentication üçün)
- [ ] `Admin` modeli yaradın (admin roles və permissions)
- [ ] Database migration scriptlərini yaradın
- [ ] Sample data üçün seed scriptləri yaradın

#### 2.2 Flask API Endpoints-lərinin İnkişafı
**Copilot/Sonnet tapşırıqları:**
- [ ] `POST /api/contact` - əlaqə formu endpoint
- [ ] `GET /api/projects` - layihələrin siyahısı
- [ ] `GET /api/projects/{id}` - xüsusi layihə məlumatları
- [ ] `GET /api/skills` - bacarıqlar məlumatları
- [ ] `GET /api/experience` - iş təcrübəsi
- [ ] Error handling və validation əlavə edin
- [ ] CORS konfiqurasiyasını qurın
- [ ] Rate limiting əlavə edin

#### 2.3 Admin Panel API Endpoints-lərinin İnkişafı
**Copilot/Sonnet tapşırıqları:**
- [ ] `POST /admin/login` - admin giriş
- [ ] `POST /admin/logout` - admin çıxış
- [ ] `GET /admin/dashboard` - dashboard məlumatları
- [ ] `GET /admin/projects` - layihələrin idarəetməsi
- [ ] `POST /admin/projects` - yeni layihə əlavə etmə
- [ ] `PUT /admin/projects/{id}` - layihə redaktəsi
- [ ] `DELETE /admin/projects/{id}` - layihə silmə
- [ ] `GET /admin/skills` - bacarıqların idarəetməsi
- [ ] `POST /admin/skills` - yeni bacarıq əlavə etmə
- [ ] `PUT /admin/skills/{id}` - bacarıq redaktəsi
- [ ] `DELETE /admin/skills/{id}` - bacarıq silmə
- [ ] `GET /admin/experience` - təcrübə idarəetməsi
- [ ] `POST /admin/experience` - yeni təcrübə əlavə etmə
- [ ] `PUT /admin/experience/{id}` - təcrübə redaktəsi
- [ ] `DELETE /admin/experience/{id}` - təcrübə silmə
- [ ] `GET /admin/messages` - əlaqə mesajları
- [ ] `PUT /admin/messages/{id}` - mesaj statusu yeniləmə
- [ ] `DELETE /admin/messages/{id}` - mesaj silmə
- [ ] `POST /admin/upload` - fayl upload (şəkillər, CV)
- [ ] JWT token authentication əlavə edin
- [ ] Admin role-based access control

#### 2.4 Email Funksionallığının Əlavə Edilməsi
**Copilot/Sonnet tapşırıqları:**
- [ ] Flask-Mail konfiqurasiyasını qurın
- [ ] Email template-ləri yaradın (HTML və plain text)
- [ ] Əlaqə formu üçün email göndərmə funksiyasını yazın
- [ ] Email validation və sanitization əlavə edin

#### 2.5 Security və Authentication
**Copilot/Sonnet tapşırıqları:**
- [ ] CSRF protection əlavə edin
- [ ] Input validation və sanitization
- [ ] SQL Injection protection
- [ ] XSS protection
- [ ] Rate limiting konfiqurasiyası
- [ ] Password hashing (Bcrypt)
- [ ] JWT token authentication
- [ ] Session management
- [ ] Admin role-based permissions

### MƏRHƏLƏ 3: FRONTEND İNKİŞAFI (5-7 gün)

#### 3.1 HTML Strukturunun Yaradılması
**Copilot/Sonnet tapşırıqları:**
- [ ] `index.html` - Hero section, CTA buttons, brief intro
- [ ] `about.html` - Şəxsi məlumatlar, təhsil, sertifikatlar
- [ ] `skills.html` - Texniki və soft skills ilə səviyyə göstəriciləri
- [ ] `projects.html` - Portfolio gallery və filter funksiyası
- [ ] `experience.html` - Timeline formatında iş təcrübəsi
- [ ] `contact.html` - Əlaqə formu və sosial media linkləri
- [ ] Navigation menu və footer komponentləri
- [ ] Semantic HTML5 elements istifadə edin

#### 3.2 CSS Styling və Responsive Design
**Copilot/Sonnet tapşırıqları:**
- [ ] CSS Custom Properties (variables) sistemi qurın
- [ ] Mobile-first responsive design
- [ ] CSS Grid və Flexbox layouts
- [ ] Typography sistemi (font-family, weights, sizes)
- [ ] Color palette və theme sistemi
- [ ] Component-based CSS architecture
- [ ] Animations və transitions (smooth scrolling, hover effects)
- [ ] Dark/Light mode toggle
- [ ] Cross-browser compatibility

#### 3.3 JavaScript Funksionallığı
**Copilot/Sonnet tapşırıqları:**
- [ ] `api.js` - Fetch API ilə backend communication
- [ ] `main.js` - Page initialization və event listeners
- [ ] `components.js` - Reusable UI components (modal, carousel, etc.)
- [ ] `utils.js` - Helper functions (validation, formatting, etc.)
- [ ] Form validation və real-time feedback
- [ ] Dynamic content loading (projects, skills, experience)
- [ ] Smooth scrolling və navigation
- [ ] Image lazy loading
- [ ] Search və filter functionality (projects səhifəsi üçün)
- [ ] Contact form AJAX submission
- [ ] Error handling və user feedback

#### 3.4 Interactive Elementlər
**Copilot/Sonnet tapşırıqları:**
- [ ] Skills section üçün progress bars və skill meters
- [ ] Projects üçün image gallery və modal popup
- [ ] Timeline animation (experience section)
- [ ] Typing animation (hero section)
- [ ] Scroll-triggered animations
- [ ] Mobile hamburger menu
- [ ] Back to top button
- [ ] Loading indicators

#### 3.5 Admin Panel Frontend İnkişafı
**Copilot/Sonnet tapşırıqları:**
- [ ] `login.html` - Admin giriş səhifəsi
- [ ] `dashboard.html` - Admin dashboard (statistics, overview)
- [ ] `projects.html` - Layihələrin CRUD idarəetməsi
- [ ] `skills.html` - Bacarıqların CRUD idarəetməsi
- [ ] `experience.html` - Təcrübənin CRUD idarəetməsi
- [ ] `messages.html` - Əlaqə mesajlarının idarəetməsi
- [ ] `settings.html` - Admin tənzimləmələri
- [ ] Admin panel üçün responsive design
- [ ] Data tables ilə sorting və filtering
- [ ] Form validation və error handling
- [ ] File upload interface (şəkillər, CV)
- [ ] Rich text editor (project descriptions üçün)
- [ ] Admin authentication və session management
- [ ] Sidebar navigation və breadcrumbs
- [ ] Dashboard charts və statistics (Chart.js)
- [ ] Admin notifications və alerts
- [ ] Bulk actions (multiple delete, edit)

### MƏRHƏLƏ 4: CONTENT İNTEGRASİYASI VƏ DATA MANAGEMENT (2-3 gün)

#### 4.1 Real Data ilə İnteqrasiya
**Copilot/Sonnet tapşırıqları:**
- [ ] Personal information və bio yaradın
- [ ] Skills database-ni real məlumatlarla doldurun
- [ ] Projects məlumatlarını əlavə edin (şəkillər, demo links, GitHub)
- [ ] Experience timeline-nı doldurun
- [ ] CV/Resume PDF faylını hazırlayın və upload funksiyasını əlavə edin
- [ ] Admin hesabını yaradın və authentication test edin
- [ ] Admin panel ilə content management test edin

#### 4.2 SEO Optimizasiyası
**Copilot/Sonnet tapşırıqları:**
- [ ] Meta tags (title, description, keywords)
- [ ] Open Graph və Twitter Card tags
- [ ] Structured data (JSON-LD schema)
- [ ] XML sitemap yaradın
- [ ] robots.txt faylını yaradın
- [ ] Alt tags və ARIA labels əlavə edin
- [ ] Page load optimization (image compression, minification)

#### 4.3 Analytics və Monitoring
**Copilot/Sonnet tapşırıqları:**
- [ ] Google Analytics konfiqurasiyası
- [ ] Google Search Console qurımu
- [ ] Performance monitoring scriptləri
- [ ] Error tracking və logging

### MƏRHƏLƏ 5: TEST VƏ QUALİTY ASSURANCE (2-3 gün)

#### 5.1 Functionality Testing
**Copilot/Sonnet tapşırıqları:**
- [ ] Contact form testing (validation, submission, email delivery)
- [ ] Navigation testing (tüm linklər və routing)
- [ ] API endpoints testing (Postman və ya Thunder Client)
- [ ] Form validation testing (client-side və server-side)
- [ ] Error handling testing
- [ ] Database operations testing
- [ ] Admin panel functionality testing (login, CRUD operations)
- [ ] File upload testing
- [ ] Authentication və authorization testing

#### 5.2 Cross-browser və Device Testing
**Copilot/Sonnet tapşırıqları:**
- [ ] Chrome, Firefox, Safari, Edge-də test
- [ ] Mobile devices (iOS, Android) test
- [ ] Tablet test
- [ ] Different screen resolutions test
- [ ] Internet Explorer compatibility (lazım olduqda)

#### 5.3 Performance Optimization
**Copilot/Sonnet tapşırıqları:**
- [ ] Google PageSpeed Insights test və optimizasiya
- [ ] Image optimization və compression
- [ ] CSS və JavaScript minification
- [ ] GZIP compression qurımu
- [ ] Caching strategies
- [ ] CDN konfiqurasiyası (lazım olduqda)

#### 5.4 Security Testing
**Copilot/Sonnet tapşırıqları:**
- [ ] SQL Injection testing
- [ ] XSS vulnerability testing
- [ ] CSRF protection testing
- [ ] Input validation testing
- [ ] HTTPS konfiqurasiyası
- [ ] Admin panel security testing
- [ ] Session security və timeout testing
- [ ] File upload security testing

### MƏRHƏLƏ 6: DEPLOYMENT VƏ HOSTİNG (1-2 gün)

#### 6.1 Domain və Hosting Qurımu
**Copilot/Sonnet tapşırıqları:**
- [ ] Domain adı seçimi və qeydiyyat
- [ ] Frontend hosting (Netlify/Vercel) qurımu
- [ ] Backend hosting (PythonAnywhere/Heroku) qurımu
- [ ] Database hosting konfiqurasiyası
- [ ] SSL sertifikatı qurımu

#### 6.2 CI/CD Pipeline
**Copilot/Sonnet tapşırıqları:**
- [ ] GitHub Actions workflow-ları yaradın
- [ ] Automatic deployment konfiqurasiyası
- [ ] Testing automation (unit tests, integration tests)
- [ ] Environment variables qurımu
- [ ] Production və development environments ayrılması

#### 6.3 Production Deployment
**Copilot/Sonnet tapşırıqları:**
- [ ] Production database-i qurın və migrate edin
- [ ] Environment konfiqurasiyasını tənzimləyin
- [ ] Static files və media hosting
- [ ] Domain DNS konfiqurasiyası
- [ ] Email hosting və konfiqurasiya (contact form üçün)
- [ ] Admin panel SSL və security konfiqurasiyası
- [ ] File storage və backup sistemi

### MƏRHƏLƏ 7: POST-DEPLOYMENT VƏ MAİNTENANCE (Davamlı)

#### 7.1 Monitoring və Analytics
**Copilot/Sonnet tapşırıqları:**
- [ ] Google Analytics və Search Console monitoring
- [ ] Server monitoring və alertlər qurın
- [ ] Error tracking və logging sistemi
- [ ] Performance monitoring
- [ ] User behavior analytics

#### 7.2 Content Management
**Copilot/Sonnet tapşırıqları:**
- [ ] Blog section əlavə edin (opsional)
- [ ] Content update sistemi
- [ ] Project gallery-ni genişləndirin
- [ ] Skills və experience-i yeniləyin
- [ ] CV/Resume-ni müntəzəm yeniləyin
- [ ] Admin panel vasitəsilə content update workflow-unu optimallaşdırın

#### 7.4 Admin Panel Maintenance
**Copilot/Sonnet tapşırıqları:**
- [ ] Admin panel security updates
- [ ] User activity logging və monitoring
- [ ] Backup və restore funksionallığı
- [ ] Admin panel performance optimization
- [ ] Database optimization və cleanup
- [ ] Admin dashboard analytics improvement

#### 7.3 Continuous Improvement
**Copilot/Sonnet tapşırıqları:**
- [ ] User feedback əsasında təkmilləşdirmələr
- [ ] Performance optimizasiyalarının davam etdirilməsi
- [ ] Yeni features əlavə edilməsi
- [ ] Security updates və patches
- [ ] Browser compatibility yeniləmələri

## İSTİFADƏ EDİLƏCƏK ALƏTLƏR VƏ TEXNOLOGİYALAR

### Frontend:
- HTML5, CSS3, Vanilla JavaScript (ES6+)
- CSS Grid, Flexbox
- Sass/SCSS (opsional)
- Webpack/Vite (bundling)

### Backend:
- Python 3.8+
- Flask web framework
- SQLite/PostgreSQL
- SQLAlchemy ORM
- Flask-Login (Authentication)
- Flask-JWT-Extended (JWT Tokens)
- Flask-Bcrypt (Password Hashing)

### Development Tools:
- VS Code
- Git və GitHub
- ESLint, Prettier
- Chrome DevTools

### Hosting:
- Frontend: Netlify/Vercel
- Backend: PythonAnywhere/Heroku
- Admin Panel: Aynı backend hosting
- Domain: Domain registrar
- File Storage: Cloudinary/AWS S3 (media files üçün)

## MÜVƏFFƏQIYYƏT KRİTERİYALARI

- [ ] Page load speed < 3 saniyə
- [ ] Google PageSpeed score > 90
- [ ] Mobile-friendly test passed
- [ ] Cross-browser compatibility
- [ ] Contact form düzgün işləyir
- [ ] All API endpoints respond correctly
- [ ] SEO score > 95
- [ ] Accessibility (WCAG 2.1) compliance
- [ ] Admin panel login və authentication işləyir
- [ ] CRUD əməliyyatları düzgün işləyir
- [ ] File upload və management düzgün işləyir
- [ ] Admin panel security measures tətbiq edilib
- [ ] Content management workflow optimal işləyir

## TİMELİNE

**Həftə 1:**
- Mərhələ 1: Layihə quruluşu (1-2 gün)
- Mərhələ 2: Backend inkişafı (3-4 gün) - Admin API və Authentication daxil

**Həftə 2:**
- Mərhələ 3: Frontend inkişafı (5-7 gün) - Admin Panel Frontend daxil

**Həftə 3:**
- Mərhələ 4: Content inteqrasiyası (2-3 gün) - Admin panel testing daxil
- Mərhələ 5: Test və QA (2-3 gün)
- Mərhələ 6: Deployment (1-2 gün)

**Həftə 4+:**
- Mərhələ 7: Maintenance və təkmilləşdirmə (davamlı) - Admin panel maintenance daxil

## QEYDLƏR

1. Hər mərhələdə Copilot/Sonnet-dən kömək istəyərkən konkret təlimatlar verin
2. Code review və testing-i hər mərhələdə aparın
3. Git commit-lərini mərhələ və feature əsasında təşkil edin
4. Documentation-u kod yazarkən paralel olaraq aparın
5. Backup və version control strategiyasını həyata keçirin
6. **Admin Panel Security**: Admin panel üçün güclü authentication və authorization tətbiq edin
7. **Admin Access Control**: Admin panel-ə girişi IP whitelist və ya VPN ilə məhdudlaşdırın
8. **Regular Backups**: Database və uploaded files üçün müntəzəm backup strategiyası həyata keçirin
9. **Admin Activity Logging**: Admin hərəkətlərini log edin və monitor edin
10. **Content Versioning**: Mühüm content dəyişikliklərini version history ilə saxlayın

## ADMİN PANEL XÜSUSİYYƏTLƏRİ

### Dashboard Əsas Funksiyalar:
- **Statistics Overview**: Site ziyarətləri, contact messages, layihə sayı
- **Recent Activity**: Son əlavə edilən layihələr, mesajlar, dəyişikliklər
- **Quick Actions**: Tez layihə əlavə etmə, mesaj cavablama
- **System Status**: Server status, database size, backup status

### Content Management Features:
- **Rich Text Editor**: Layihə təsvirləri üçün WYSIWYG editor
- **Image Management**: Drag & drop upload, image resizing, gallery
- **Bulk Operations**: Multiple layihə/skill/experience idarəetməsi
- **Content Preview**: Dəyişiklikləri publish etməzdən əvvəl preview
- **Version Control**: Content dəyişikliklərinin tarixi

### Advanced Features:
- **SEO Management**: Meta tags, descriptions idarəetməsi
- **Analytics Integration**: Google Analytics data admin paneldə göstərmə
- **Contact Form Management**: Mesaj filterleme, status tracking, auto-response
- **Site Settings**: Site title, description, social links idarəetməsi
- **Backup & Restore**: One-click backup və restore funksionallığı

---

**Əhəmiyyətli:** Bu plan mürəkkəb bir layihə olduğuna görə hər mərhələdə Copilot və Sonnet-dən maximum faydalanmaq üçün dəqiq və aydın tapşırıqlar verməyi unutmayın. Hər addımı test edərək irəliləyin. **Admin panel təhlükəsizliyinə xüsusi diqqət yetirin!**
https://github.com/Heyyam0855/portfolio-project.githttps://github.com/Heyyam0855/portfolio-project.git