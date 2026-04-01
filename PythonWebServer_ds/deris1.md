# 📚 Python Web Server - HTML Layihəsi Dərsi

## 🎯 Dərsin Məqsədi

Bu dərsdə biz sadə bir HTML səhifəsindən başlayaraq, **interaktiv və professional** bir web layihəsi yaratmağı öyrənəcəyik.

---

## 📖 Dərs 1: Layihənin Strukturu

### 🗂️ Fayl Strukturu

Layihəmiz aşağıdaki fayllardan ibarətdir:

```
PythonWebServer_ds/
├── index.html      # Ana səhifə
├── about.html      # Haqqında səhifəsi
├── contact.html    # Əlaqə səhifəsi
├── server.py       # Python server
└── readme.md       # Dokumentasiya
```

---

## 📖 Dərs 2: HTML Strukturu və Əsaslar

### 🎨 HTML Səhifəsinin Əsas Hissələri

```html
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Səhifə Başlığı</title>
</head>
<body>
    <!-- Məzmun buraya yazılır -->
</body>
</html>
```

**İzahat:**
- `<!DOCTYPE html>` - HTML5 versiyasını bildirir
- `<html lang="az">` - Səhifənin dilini müəyyən edir
- `<head>` - Meta məlumatlar, başlıq, CSS kodları
- `<body>` - Səhifənin görünən məzmunu

---

## 📖 Dərs 3: CSS ilə Dizayn

### 🎨 Gradient Arxa Fon Yaratmaq

```css
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
```

**İzahat:**
- `linear-gradient()` - Rəng keçidləri yaradır
- `animation` - Animasiya əlavə edir
- `@keyframes` - Animasiyanın addımlarını təyin edir

---

## 📖 Dərs 4: JavaScript ilə İnteraktivlik

### ⏰ Canlı Saat Yaratmaq

```javascript
function updateClock() {
    const now = new Date();
    const time = now.toLocaleTimeString('az-AZ');
    document.getElementById('clock').textContent = time;
}
setInterval(updateClock, 1000);
```

**İzahat:**
- `Date()` - Hazırkı tarixi və vaxtı alır
- `toLocaleTimeString()` - Vaxtı formatlaşdırır
- `setInterval()` - Funksiyanı hər saniyə çağırır

---

### 📊 Ziyarətçi Sayğacı

```javascript
let visitors = localStorage.getItem('visitors') || 0;
visitors++;
localStorage.setItem('visitors', visitors);
document.getElementById('visitors').textContent = visitors;
```

**İzahat:**
- `localStorage` - Brauzerdə məlumat saxlayır
- `getItem()` - Məlumatı oxuyur
- `setItem()` - Məlumatı saxlayır

---

### 🎨 Rəng Dəyişdirmə Funksiyası

```javascript
function changeColor() {
    const colors = ['#667eea', '#f093fb', '#4facfe', '#43e97b', '#fa709a'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.background = `linear-gradient(135deg, ${randomColor} 0%, #764ba2 100%)`;
}
```

**İzahat:**
- `Math.random()` - Təsadüfi ədəd yaradır
- `Math.floor()` - Ədədi aşağı yuvarlaqlaşdırır
- Array indeksləməsi ilə təsadüfi rəng seçir

---

## 📖 Dərs 5: CSS Animasiyaları

### 🎭 Bounce Animasiyası

```css
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}

.emoji {
    animation: bounce 2s infinite;
}
```

**İzahat:**
- `transform: translateY()` - Elementi şaquli hərəkət etdirir
- `infinite` - Animasiyanı sonsuz təkrarlayır
- `2s` - Animasiyanın müddəti

---

### ✨ Hover Effektləri

```css
.card {
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.3);
}
```

**İzahat:**
- `transition` - Keçid effekti əlavə edir
- `:hover` - Mausun üzərinə gəldikdə aktivləşir
- `transform` - Elementi hərəkət etdirir

---

## 📖 Dərs 6: Python Web Server

### 🚀 Sadə HTTP Server

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

server = HTTPServer(('localhost', 8000), MyHandler)
print('🚀 Server başladı: http://localhost:8000')
server.serve_forever()
```

**İzahat:**
- `HTTPServer` - HTTP server yaradır
- `SimpleHTTPRequestHandler` - GET sorğularını idarə edir
- `serve_forever()` - Serveri daimi işlək saxlayır

---

## 📖 Dərs 7: Responsive Dizayn

### 📱 Media Queries

```css
@media (max-width: 768px) {
    .container {
        width: 95%;
        padding: 20px;
    }
    
    .card {
        margin: 10px 0;
    }
}
```

**İzahat:**
- `@media` - Ekran ölçüsünə görə stil dəyişir
- `max-width: 768px` - Mobil cihazlar üçün
- Kiçik ekranlarda dizayn uyğunlaşır

---

## 📖 Dərs 8: Form Yaratmaq

### 📧 Əlaqə Formu

```html
<form id="contactForm">
    <input type="text" name="name" placeholder="Adınız" required>
    <input type="email" name="email" placeholder="Email" required>
    <textarea name="message" placeholder="Mesajınız" required></textarea>
    <button type="submit">Göndər</button>
</form>
```

**İzahat:**
- `required` - Məcburi sahə
- `type="email"` - Email formatını yoxlayır
- `placeholder` - Sahədə məsləhət mətni

---

### ✅ Form Validasiyası

```javascript
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Mesajınız göndərildi! ✅');
    this.reset();
});
```

**İzahat:**
- `addEventListener()` - Hadisə dinləyicisi əlavə edir
- `preventDefault()` - Səhifənin yenilənməsinin qarşısını alır
- `reset()` - Formu təmizləyir

---

## 📖 Dərs 9: Naviqasiya Menyusu

### 🧭 Responsive Menyu

```css
nav {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 15px;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 10px 20px;
    transition: all 0.3s;
}

nav a:hover {
    background: rgba(255,255,255,0.2);
    border-radius: 10px;
}
```

**İzahat:**
- `backdrop-filter: blur()` - Arxa fonun bulanıqlığı
- `rgba()` - Şəffaf rəng
- Hover effekti ilə interaktiv menyu

---

## 📖 Dərs 10: Layihənin Xüsusiyyətləri

### ✨ Yaratdığımız Xüsusiyyətlər

1. **🌈 Animasiyalı Gradient Arxa Fon**
   - Dəyişən rənglər
   - Hamar keçidlər
   - 15 saniyəlik dövr

2. **⏰ Canlı Saat**
   - Real-time yeniləmə
   - Azərbaycan formatı
   - Hər saniyə yenilənir

3. **📊 Ziyarətçi Sayğacı**
   - LocalStorage istifadəsi
   - Avtomatik artım
   - Daimi saxlanma

4. **🎨 Rəng Dəyişdirmə**
   - 5 fərqli rəng
   - Təsadüfi seçim
   - Düymə ilə idarəetmə

5. **🎭 Animasiyalar**
   - Bounce effekti
   - Hover animasiyaları
   - Smooth transitions

6. **📱 Responsive Dizayn**
   - Mobil uyğun
   - Tablet dəstəyi
   - Desktop optimizasiyası

---

## 📖 Dərs 11: Layihəni İşə Salmaq

### 🚀 Serveri Başlatmaq

```bash
python server.py
```

### 🌐 Brauzerdə Açmaq

```
http://localhost:8000
```

### 📁 Faylları Yoxlamaq

- `index.html` - Ana səhifə
- `about.html` - Haqqında
- `contact.html` - Əlaqə
- `server.py` - Server

---

## 📖 Dərs 12: Təkmilləşdirmə İdeyaları

### 🎯 Əlavə Xüsusiyyətlər

1. **🌙 Dark/Light Mode**
   - Tema dəyişdirmə
   - LocalStorage-də saxlama

2. **🔍 Axtarış Funksiyası**
   - Məzmun axtarışı
   - Filter sistemi

3. **💬 Şərh Sistemi**
   - İstifadəçi şərhləri
   - Rating sistemi

4. **🖼️ Şəkil Qalereyası**
   - Lightbox effekti
   - Slider

5. **📊 Statistika Dashboard**
   - Charts və qrafiklər
   - Data visualization

---

## 🎓 Dərsin Nəticəsi

Bu dərsdə öyrəndiklərimiz:

✅ HTML strukturu və semantik təqlər  
✅ CSS ilə dizayn və animasiyalar  
✅ JavaScript ilə interaktivlik  
✅ Python ilə web server  
✅ Responsive dizayn prinsipləri  
✅ Form yaratmaq və validasiya  
✅ LocalStorage istifadəsi  
✅ Animasiya və effektlər  
✅ Naviqasiya sistemi  
✅ Layihə strukturu  

---

## 💡 Əlavə Resurslar

### 📚 Öyrənmək üçün:

- **HTML**: [MDN Web Docs](https://developer.mozilla.org)
- **CSS**: [CSS-Tricks](https://css-tricks.com)
- **JavaScript**: [JavaScript.info](https://javascript.info)
- **Python**: [Python.org](https://python.org)

### 🛠️ İstifadə Etdiyimiz Texnologiyalar

- HTML5
- CSS3
- JavaScript (ES6+)
- Python 3
- HTTP Server

---

## 🎉 Təbriklər!

Siz sadə bir HTML səhifəsindən başlayaraq, **professional və interaktiv** bir web layihəsi yaratmağı öyrəndiniz! 

Bu layihəni əsas götürərək daha böyük və mürəkkəb layihələr yarada bilərsiniz.

**Uğurlar!** 🚀💪

---

## 📝 Qeydlər

- Bu layihə təlim məqsədi daşıyır
- Production üçün əlavə təhlükəsizlik tədbirləri lazımdır
- Kodları öz ehtiyaclarınıza görə dəyişdirə bilərsiniz

---

**Müəllif:** Python Web Server Dərsləri  
**Tarix:** 2025  
**Versiya:** 1.0

