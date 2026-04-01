# HTML Əsas Strukturu - Dərs 2 (20.21 deyqe)

## Rəsmdəki HTML Kodunun Təhlili

Bu dərsdə rəsmdəki HTML kodunun hər bir hissəsini ətraflı şəkildə öyrənəcəyik.

---

## 1. `<!DOCTYPE html>`

**Nə iş görür:**
- Bu, HTML sənədinin versiyasını brauzərə bildirən deklarasiyadır
- HTML5 versiyasını istifadə etdiyimizi göstərir
- Brauzerin səhifəni düzgün render etməsi üçün lazımdır
- Bu sətir həmişə HTML faylının ən üstündə olmalıdır

**Nümunə:**
```html
<!DOCTYPE html>
```

---

## 2. `<html lang="en">`

**Nə iş görür:**
- HTML sənədinin əsas konteynerini (kök elementini) açır
- `lang="en"` atributu səhifənin dilinin ingilis dili olduğunu göstərir
- Axtarış motorları və ekran oxuyucuları üçün faydalıdır
- Azərbaycan dili üçün `lang="az"` istifadə edilə bilər

**Nümunə:**
```html
<html lang="az">
  <!-- Səhifənin bütün məzmunu buraya yazılır -->
</html>
```

---

## 3. `<head>`

**Nə iş görür:**
- Səhifə haqqında meta məlumatları saxlayan bölmədir
- Bu bölmədəki məlumatlar brauzerdə görünmür (title istisna olmaqla)
- CSS faylları, JavaScript faylları, meta teqlər burada qoşulur
- Səhifənin konfiqurasiyası burada edilir

**Nümunə:**
```html
<head>
  <meta charset="UTF-8">
  <title>Səhifə Başlığı</title>
</head>
```

---

## 4. `<meta charset="UTF-8">`

**Nə iş görür:**
- Səhifənin simvol kodlaşdırmasını təyin edir
- UTF-8 dünya üzrə ən çox istifadə olunan kodlaşdırmadır
- Azərbaycan dilindəki xüsusi hərfləri (ə, ı, ö, ü, ş, ç, ğ) düzgün göstərir
- Bu olmadan xüsusi simvollar səhv görünə bilər

**Nümunə:**
```html
<meta charset="UTF-8">
```

---

## 5. `<meta http-equiv="X-UA-Compatible" content="IE=edge">`

**Nə iş görür:**
- Internet Explorer brauzeri üçün uyğunluq rejimini təyin edir
- `IE=edge` - IE-nin ən son versiyasını istifadə etməsini təmin edir
- Köhnə IE versiyalarında səhifənin düzgün görünməsi üçün lazımdır
- Müasir brauzerlərdə bu teq artıq çox vacib deyil

**Nümunə:**
```html
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

---

## 6. `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

**Nə iş görür:**
- Mobil cihazlarda səhifənin necə görünəcəyini idarə edir
- `width=device-width` - səhifə enini cihazın eninə uyğunlaşdırır
- `initial-scale=1.0` - ilkin zoom səviyyəsini 1:1 təyin edir
- Responsive (adaptiv) dizayn üçün çox vacibdir
- Bu olmadan mobil cihazlarda səhifə kiçik görünər

**Nümunə:**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

## 7. `<title>Document</title>`

**Nə iş görür:**
- Brauzerin tab (vərəq) hissəsində görünən başlığı təyin edir
- Axtarış motorlarında səhifənin başlığı kimi göstərilir
- Əlfəcinlərə (bookmarks) əlavə edildikdə bu ad istifadə olunur
- SEO (Axtarış Motorları Optimallaşdırılması) üçün çox vacibdir

**Nümunə:**
```html
<title>Mənim Veb Səhifəm</title>
```

**Nəticə:** Brauzer tabında "Mənim Veb Səhifəm" yazısı görünəcək

---

## 8. `</head>`

**Nə iş görür:**
- `<head>` teqinin bağlanma teqidir
- Head bölməsinin bitdiyini göstərir
- Bundan sonra body bölməsi başlayır

---

## 9. `<body>`

**Nə iş görür:**
- Səhifənin görünən məzmununu saxlayan əsas bölmədir
- Bütün mətn, şəkil, video, link və digər elementlər buraya yazılır
- İstifadəçinin gördüyü hər şey body içərisindədir
- CSS ilə stilləşdirilə bilər

**Nümunə:**
```html
<body>
  <h1>Salam Dünya!</h1>
  <p>Bu mənim ilk veb səhifəmdir.</p>
</body>
```

---

## 10. `</body>`

**Nə iş görür:**
- `<body>` teqinin bağlanma teqidir
- Səhifənin görünən məzmununun bitdiyini göstərir

---

## 11. `</html>`

**Nə iş görür:**
- `<html>` teqinin bağlanma teqidir
- HTML sənədinin tamamilə bitdiyini göstərir
- Bu, faylın ən son sətri olmalıdır

---

## Tam Struktur və İzahı

```html
<!DOCTYPE html>           <!-- HTML5 versiyası -->
<html lang="en">          <!-- HTML sənədinin başlanğıcı -->
  <head>                  <!-- Meta məlumatlar bölməsi -->
    <meta charset="UTF-8">                                    <!-- Simvol kodlaşdırması -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">     <!-- IE uyğunluğu -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Mobil uyğunluq -->
    <title>Document</title>                                   <!-- Səhifə başlığı -->
  </head>                 <!-- Head bölməsinin sonu -->
  <body>                  <!-- Görünən məzmun bölməsi -->
    
    <!-- Buraya səhifənin məzmunu yazılır -->
    
  </body>                 <!-- Body bölməsinin sonu -->
</html>                   <!-- HTML sənədinin sonu -->
```

---

## Əlavə Qeydlər

### Teqlərin Açılması və Bağlanması

HTML-də əksər teqlər cüt şəkildə işləyir:
- **Açılan teq:** `<teq>`
- **Bağlanan teq:** `</teq>`

**Nümunə:**
```html
<body>
  Məzmun
</body>
```

### Meta Teqlər

Meta teqlər özü-özünə bağlanan teqlərdir və bağlanma teqinə ehtiyac yoxdur:
```html
<meta charset="UTF-8">
```

### Girintilər (Indentation)

Kodun oxunaqlı olması üçün girintilər istifadə edilir:
```html
<html>
  <head>
    <title>Başlıq</title>
  </head>
  <body>
    <h1>Mətn</h1>
  </body>
</html>
```

---

## Praktiki Tapşırıq

Aşağıdakı strukturu özünüz yaradın və brauzerdə açın:

```html
<!DOCTYPE html>
<html lang="az">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mənim İlk Səhifəm</title>
  </head>
  <body>
    <h1>Salam, Azərbaycan!</h1>
    <p>Bu mənim HTML ilə yaratdığım ilk səhifədir.</p>
  </body>
</html>
```

---

## Xülasə

Bu dərsdə öyrəndiklərimiz:

1. ✅ `<!DOCTYPE html>` - HTML versiyasını bildirir
2. ✅ `<html>` - Əsas konteyner
3. ✅ `<head>` - Meta məlumatlar bölməsi
4. ✅ `<meta charset>` - Simvol kodlaşdırması
5. ✅ `<meta http-equiv>` - Brauzer uyğunluğu
6. ✅ `<meta viewport>` - Mobil uyğunluq
7. ✅ `<title>` - Səhifə başlığı
8. ✅ `<body>` - Görünən məzmun

**Növbəti dərsdə:** HTML mətn elementləri (h1-h6, p, span, div) öyrənəcəyik.

---

**Müəllif Qeydi:** Bu struktur hər bir HTML səhifəsinin əsasını təşkil edir. Bu strukturu yaxşı mənimsəmək çox vacibdir!

