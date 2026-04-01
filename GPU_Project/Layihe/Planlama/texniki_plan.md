# Personal Portfolio Layihəsi - Texniki Tapşırıq

## 1. Biznes Analiz

### 1.1 Məqsəd və Hədəf
- **Əsas məqsəd**: Peşəkar profilin gücləndirilməsi və iş imkanlarının artırılması
- **Hədəf auditoriya**: 
  - Potensial işəgötürənlər
  - Müştərilər və müştəri namizədləri
  - Peşəkar şəbəkə əlaqələri
  - Həmkarlar və sənaye mütəxəssisləri

### 1.2 Biznes Dəyəri
- **Brendinq**: Şəxsi brendin qurulması və gücləndirilməsi
- **Credibility**: Texniki bacarıqların real nümunələrlə sübut edilməsi
- **Networking**: Peşəkar əlaqələrin genişləndirilməsi
- **Career Growth**: İş imkanlarının artırılması və daha yaxşı mövqelər əldə etmə

### 1.3 Rəqabət Analizi
- Digər proqramçıların portfolio saytları
- LinkedIn profilləri və peşəkar şəbəkələr
- GitHub profili və açıq mənbə töhfələri
- Peşəkar blog və məqalələr

## 2. Funksional Tələblər

### 2.1 Əsas Səhifələr
1. **Ana Səhifə (Home)**
   - Qısa təqdimat və xoş gəlmisiniz mesajı
   - Hero section ilə əsas məlumatlar
   - CTA (Call to Action) düymələri

2. **Haqqımda (About)**
   - Şəxsi və peşəkar məlumatlar
   - Təhsil və sertifikatlar
   - Peşəkar yol xəritəsi

3. **Bacarıqlar (Skills)**
   - Texniki bacarıqlar (proqramlaşdırma dilləri, freymvorklar)
   - Soft skills
   - Alətlər və texnologiyalar
   - Skill level göstəriciləri

4. **Layihələr (Portfolio/Projects)**
   - Tamamlanmış layihələrin kataloqu
   - Hər layihə üçün:
     - Şəkillər və ya demo
     - Texnologiya stack-i
     - Layihə təsviri
     - GitHub linki
     - Canlı demo linki

5. **Təcrübə (Experience)**
   - İş təcrübəsi timeline-ı
   - Şirkətlər və rollar
   - Əsas nailiyyətlər

6. **Əlaqə (Contact)**
   - Əlaqə formu
   - Sosial media linkləri
   - Email və telefon məlumatları

### 2.2 Əlavə Funksiyalar
- **Blog bölməsi** (opsional)
- **CV/Resume yükləmə**
- **Çoxdilli dəstək** (Azərbaycan/İngilis)
- **Dark/Light mode**
- **Responsive design**

## 3. Texniki Tələblər

### 3.1 Frontend Texnologiyalar
**Əsas Stack (Vanilla Technologies):**
- **HTML5** (semantic markup, modern elements)
- **CSS3** (modern styling, flexbox, grid, animations)
- **Vanilla JavaScript** (ES6+, DOM manipulation, Fetch API)
- **CSS Preprocessor**: Sass/SCSS (opsional)
- **CSS Framework**: Bootstrap və ya Tailwind CSS (opsional, utility classes üçün)

**Əlavə Alətlər:**
- **Webpack** və ya **Vite** (bundling və development server)
- **Babel** (JavaScript transpilation)
- **PostCSS** (CSS processing)
- **ESLint** və **Prettier** (code quality)

### 3.2 Backend Tələbləri
- **Əlaqə formu və məlumat idarəetməsi üçün**:
  - **Flask** (Python web framework)
  - **SQLite** (verilənlər bazası)
  - **SQLAlchemy** (ORM - Object Relational Mapping)
  - **Flask-Mail** (email göndərmə üçün)
  - **Flask-WTF** (form validasiya)
  - **Flask-CORS** (cross-origin requests üçün)

### 3.3 Hosting və Domain
- **Domain**: şəxsi domain adı (məs: adınız.com)
- **Frontend Hosting** (Static Sites):
  - **GitHub Pages** (pulsuz, Git integration)
  - **Netlify** (pulsuz, continuous deployment)
  - **Vercel** (static sites üçün)
  - **Firebase Hosting** (Google)
- **Backend Hosting**:
  - **PythonAnywhere** (Flask üçün tövsiyə)
  - **Heroku** (Python apps üçün)
  - **DigitalOcean** (VPS)
  - **Railway** (modern Python hosting)
- **Verilənlər Bazası**:
  - SQLite (development və kiçik production üçün)
  - PostgreSQL (böyük production üçün upgrade)

### 3.4 Frontend Arxitektura (HTML/CSS/JS)
- **Fayl Strukturu**:
  ```
  portfolio-frontend/
  ├── index.html
  ├── about.html
  ├── projects.html
  ├── skills.html
  ├── experience.html
  ├── contact.html
  ├── css/
  │   ├── main.css
  │   ├── components.css
  │   └── responsive.css
  ├── js/
  │   ├── main.js
  │   ├── api.js
  │   ├── components.js
  │   └── utils.js
  ├── assets/
  │   ├── images/
  │   ├── icons/
  │   └── fonts/
  └── data/
      └── config.js
  ```
- **JavaScript Modulları**:
  - API communication (Fetch API)
  - DOM manipulation
  - Form validation
  - Responsive navigation
  - Smooth scrolling və animasiyalar
- **CSS Organizasiyası**:
  - CSS Grid və Flexbox layouts
  - CSS Custom Properties (variables)
  - Mobile-first responsive design
  - CSS animations və transitions

### 3.5 Backend Arxitektura (Flask + SQLite)
- **API Endpoints**:
  - `POST /api/contact` - əlaqə formu üçün
  - `GET /api/projects` - layihələrin siyahısı
  - `GET /api/skills` - bacarıqlar məlumatları
  - `GET /api/experience` - iş təcrübəsi
- **Verilənlər Bazası Strukturu**:
  - `contacts` cədvəli (əlaqə formları)
  - `projects` cədvəli (portfolio layihələri)
  - `skills` cədvəli (texniki bacarıqlar)
  - `experience` cədvəli (iş təcrübəsi)
- **Security**:
  - Flask-Login (authentication)
  - CSRF protection
  - Input validation
  - Rate limiting

### 3.5 İdarəetmə Sistemi
- **Git versiya idarəetməsi**
- **GitHub repository**
- **CI/CD pipeline** (automatic deployment)

## 4. UX/UI Tələbləri

### 4.1 Dizayn Prinsipləri
- **Minimalist və təmiz dizayn**
- **Professional görünüş**
- **User-friendly naviqasiya**
- **Mobile-first approach**

### 4.2 Performance Tələbləri
- **Sürətli yüklənmə** (<3 saniyə)
- **SEO optimizasiyası**
- **Accessibility (WCAG 2.1)**
- **Cross-browser compatibility**

### 4.3 Responsiv Dizayn
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## 5. İcra Planı

### 5.1 Faza 1: Planlaşdırma (1-2 həftə)
- [ ] Wireframe və mockup hazırlanması
- [ ] Content strategiyasının müəyyənləşdirilməsi
- [ ] Texnologiya stack-inin seçilməsi
- [ ] Domain və hosting seçimi

### 5.2 Faza 2: Dizayn (1-2 həftə)
- [ ] UI/UX dizaynının hazırlanması
- [ ] Rəng palitrasının müəyyənləşdirilməsi
- [ ] Typography və iconların seçilməsi
- [ ] Asset-lərin hazırlanması

### 5.3 Faza 3: İnkişaf (3-5 həftə)
**Backend Development (1-2 həftə):**
- [ ] Flask layihə strukturunun qurulması
- [ ] SQLite verilənlər bazası modellərin yaradılması
- [ ] API endpoints-lərin yazılması
- [ ] Authentication və security tətbiqi

**Frontend Development (2-3 həftə):**
- [ ] HTML strukturunun yaradılması (semantic markup)
- [ ] CSS styling və responsive dizayn
- [ ] JavaScript funksionallığının əlavə edilməsi:
  - [ ] API communication (Fetch API)
  - [ ] Form validation və submission
  - [ ] Dynamic content loading
  - [ ] Navigation və user interactions
  - [ ] Animations və transitions
- [ ] Cross-browser compatibility test

### 5.4 Faza 4: Test və Deploy (1 həftə)
- [ ] Cross-browser test
- [ ] Mobile test
- [ ] Performance optimizasiyası
- [ ] SEO optimizasiyası
- [ ] Deployment

### 5.5 Faza 5: Təkmilləşdirmə (davamlı)
- [ ] Analytics əlavə edilməsi
- [ ] Content yenilənməsi
- [ ] Yeni layihələrin əlavə edilməsi
- [ ] Feedback əsasında təkmilləşdirmələr

## 6. Resurslar və Alətlər

### 6.1 Dizayn Alətləri
- Figma və ya Adobe XD (UI/UX dizayn)
- Canva və ya Adobe Creative Suite (qrafik elementlər)
- Unsplash və ya Pexels (foto resursları)

### 6.2 İnkişaf Alətləri
- **Code Editors**:
  - VS Code (tövsiyə olunan)
  - VS Code Extensions: Live Server, Prettier, ESLint
- **Version Control**:
  - Git və GitHub
- **Browser Development**:
  - Chrome DevTools
  - Firefox Developer Tools
- **Frontend Development**:
  - Live Server (development server)
  - Sass (CSS preprocessing, opsional)
  - Webpack və ya Vite (bundling, opsional)
  - Browser Sync (cross-device testing)
- **Python Development**:
  - Python 3.8+ (programming language)
  - pip (package manager)
  - Virtual Environment (venv)
  - Flask CLI (development server)
- **Database Management**:
  - SQLite Browser (verilənlər bazası idarəetməsi)
  - DB Browser for SQLite
- **API Testing**:
  - Postman (API test)
  - Thunder Client (VS Code extension)
  - Browser Network Tab (simple testing)

### 6.3 Test Alətləri
- Google PageSpeed Insights
- GTmetrix
- Google Mobile-Friendly Test
- BrowserStack (cross-browser test)

## 7. Müvəffəqiyyət Kriteriyaları

### 7.1 Texniki Metrikalar
- [ ] Page load speed < 3 saniyə
- [ ] Google PageSpeed score > 90
- [ ] Mobile-friendly
- [ ] SEO score > 95

### 7.2 Biznes Metrikalar
- [ ] İş müraciətlərinin artması
- [ ] Peşəkar şəbəkənin genişlənməsi
- [ ] Brendin tanınırlığının artması
- [ ] Portfolio görüntülənmələrinin artması

## 8. Büdcə və Resurslar

### 8.1 Minimal Büdcə
- Domain: $10-15/il
- Frontend Hosting: Pulsuz (Vercel/Netlify)
- Backend Hosting: Pulsuz (PythonAnywhere Beginner Plan)
- SSL Sertifikat: Pulsuz (Let's Encrypt)
- **Toplam**: ~$10-15/il

### 8.2 Professional Büdcə
- Premium domain: $50-100/il
- Frontend hosting: Pulsuz və ya $5-10/ay
- Backend hosting: $5-20/ay (PythonAnywhere/Heroku)
- Database: SQLite (pulsuz) və ya PostgreSQL ($7-15/ay)
- Professional email: $5-10/ay
- Premium dizayn alətləri: $20-50/ay
- **Toplam**: ~$40-100/ay

## 9. Risklər və Məhdudiyyətlər

### 9.1 Texniki Risklər
- **Frontend spesifik risklər**:
  - Browser compatibility problemləri (vanilla JS)
  - JavaScript performance məsələləri
  - CSS layout problems across devices
  - Manual state management complexity
- **Backend risklər**:
  - Flask security vulnerabilities
  - SQLite performance limitations
  - Server downtime və deployment issues
- **Integration risklər**:
  - CORS problemləri
  - API connectivity issues

### 9.2 Biznes Risklər
- Rəqabətli bazar
- Teknologiyaların sürətli dəyişməsi
- Content-in köhnəlməsi

### 9.3 Həllər
- Regular testing və monitoring
- Continuous learning və skill development
- Regular content updates və maintenance

---

**Qeyd**: Bu texniki tapşırıq dinamik sənəddir və layihənin gedişatında yenilənə bilər.