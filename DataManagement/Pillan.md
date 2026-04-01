# HTML, CSS, JavaScript üçün Öyrənmə Planı (8 həftə)

Məqsəd: sıfırdan başlayıb 1–2 kiçik veb layihə hazırlamaq. Planı gündə 60–90 dəqiqə ilə izləmək kifayətdir.

## Necə işləməli
- Gündəlik ritual (20–20–20): qısa oxu → qısa video/istifadə → praktika.
- Praktika üstün: hər mövzudan sonra ən az 1 kiçik tapşırıq.
- Resurslar: MDN Web Docs, w3schools (baza üçün), YouTube-dan qısa dərslər.

## Bu repodakı fayllardan istifadə
- İş faylları: `main.html`, `main.css`, `main.js`.
- `main.html`-i brauzerdə açın. Stil və skript bağlı deyilsə, HTML `<head>` və sonuna aşağıdakı sətirləri əlavə edin:
	- CSS: `<link rel="stylesheet" href="main.css">`
	- JS: `<script src="main.js" defer></script>`

---

## Həftə 1 — HTML əsasları
Mövzular:
- HTML sənəd quruluşu: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`
- Mətn elementləri: `h1–h6`, `p`, `strong`, `em`
- Siyahılar: `ul`, `ol`, `li`
- Keçidlər və şəkillər: `a`, `img`
- Semantik etiketlər: `header`, `nav`, `main`, `section`, `article`, `footer`

Tapşırıq:
- “Haqqımda” səhifəsi qurun: başlıq, foto, 2–3 paraqraf, 2 daxili link.

Mini-yoxlama:
- Səhifə semantik bloklara bölünüb?
- Şəkillərə `alt` mətni var?

## Həftə 2 — CSS əsasları və Box Model
Mövzular:
- CSS əlavə etmə: external, selector-lar, specificity, irsilik
- Rənglər, şriftlər, `margin`/`padding`/`border`, `display`
- Reset/normalize anlayışı

Tapşırıq:
- Həftə 1 səhifəsini tam stilləyin: uyğun şrift, rəng palitrası, boşluqlar.

Mini-yoxlama:
- Mobil ekranlarda mətn oxunaqlıdır?
- Linklər hover zamanı vizual reaksiya verir?

## Həftə 3 — Layout: Flexbox və Grid, Responsiv dizayn
Mövzular:
- Flex konteyner və item-lər, hizalama
- CSS Grid: sütun/sətir, `gap`, sadə şəbəkə
- Media queries, mobil-öncə (mobile-first)

Tapşırıq:
- 3 kartlı (şəkil+başlıq+mətn+button) layout hazırlayın, 320px–1200px aralığında responsiv olsun.

Mini-yoxlama:
- Naviqasiya sətiri dar ekranda menyu düyməsinə çevrilə bilir? (sadə variant: vertikal siyahı)

## Həftə 4 — JavaScript əsasları və DOM-a giriş
Mövzular:
- Dəyişənlər (`let`, `const`), tiplər, operatorlar
- Şərtlər, dövrlər, funksiyalar
- DOM seçimi: `querySelector`, `classList`, event-lər

Tapşırıq:
- “Dark mode” düyməsi: kliklə body-ə `dark` class-ı əlavə/sil.
- Sadə sayğac: artım, azalma, sıfırlama düymələri.

Mini-yoxlama:
- Script `defer` ilə yüklənir?
- Konsolda səhv yoxdur?

## Həftə 5 — JS ilə praktika: massivlər, obyektlər, lokal yaddaş
Mövzular:
- Massiv metodları: `map`, `filter`, `reduce`
- Obyektlər və destrukturizasiya
- `localStorage` ilə sadə davamlılıq

Tapşırıq:
- Mini “Todo” app: əlavə et, sil, tamamlandı işarəsi; siyahını `localStorage`-da saxla.

Mini-yoxlama:
- Səhifə yenilənsə də siyahı qalır?

## Həftə 6 — Asinxron JS və Fetch API
Mövzular:
- `fetch`, `async/await`, `try/catch`
- JSON ilə işləmək, sadə API-lər

Tapşırıq:
- Placeholder API-dən (məs: postlar) məlumat çək və kartlar kimi göstər.

Mini-yoxlama:
- Yüklənmə vəziyyəti (“Loading…”) və səhv mesajları göstərilir?

## Həftə 7 — Kiçik Layihə 1: Statik + interaktiv sayt
Tələblər:
- 3–5 səhifəlik responsiv sayt (məs: portfolio, restoran, bloq)
- Naviqasiya, hero, kartlı bölmə, əlaqə forması (JS ilə sadə yoxlama)
- Dark mode, “yuxarı qayıt” düyməsi

Çatdırılma:
- `main.html/css/js` fayllarında işlək demo

## Həftə 8 — Kiçik Layihə 2: Mini tətbiq
İdeyalar:
- Hava proqnozu (şəhərə görə API-dən oxu)
- Qeydlər (CRUD + `localStorage`)
- Valyuta çevirmə (kurs API + formatlama)

Çatdırılma:
- Mobil-öncə dizayn, səhv idarəetməsi, əsas əlçatımlılıq (accessible) qaydaları

---

## Yoxlama siyahısı (Checklist)
- [ ] HTML semantika: başlıqlar, bölmələr, `alt` mətni
- [ ] CSS: box model, Flex/Grid, media queries
- [ ] JS: DOM, event-lər, massivlər/obyektlər, `localStorage`
- [ ] Asinxron: `fetch`, `async/await`, səhv idarəetməsi
- [ ] Responsiv və əlçatımlı dizayn
- [ ] Layihə: iki mini tətbiq tamamlanıb

## Faydalı praktikalar
- Commit-ləri kiçik və aydın mesajlarla edin.
- Konsol və DevTools ilə test edin (Mobil görünüş rejimi, şəbəkə sürəti).
- Kodu formatlayın (VS Code: Format on Save).

## Növbəti addımlar
- GitHub Pages ilə dərc (deploy).
- SASS və ya Tailwind CSS-ə baxış.
- Modul JS, build alətləri (Vite) ilə tanışlıq.

Uğurlar! Planı izləyərək hər həftə 1–2 səhifə/komponent tamamlayın və `main.html`, `main.css`, `main.js` fayllarında praktikaya çevirin.
