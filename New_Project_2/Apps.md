# Python Tətbiqi Hazırlıq Planı

## 1. Layihəyə Baxış
- Məqsəd: Mövcud Python nüvəsini refaktor edib, istifadəçi üçün tətbiq şəklində təqdim olunan stabil və genişlənə bilən sistem hazırlamaq.
- Nəticə: Konfiqurasiya edilə bilən, GUI və ya veb interfeysə malik, paylama paketinə çevrilmiş tətbiq.

## 2. Əsas Tələblər və Məhdudiyyətlər
- Platforma: Windows əsas mühit, gələcəkdə multiplatform dəstəyi nəzərdə tutulur.
- Versiya: Python 3.11+ (performans və kitabxana uyğunluğu üçün).
- Sürüm nəzarəti: Git inteqrasiyası, GitHub və ya Azure DevOps reposu.
- Müddət: 6-8 həftəlik mərhələli inkişaf planı.

## 3. Texniki Yığın
- **Dil:** Python (PEP8 standartı, mypy ilə tip yoxlaması).
- **GUI / Veb qat:**
  - Masaüstü üçün: `PySide6` (Qt6 əsaslı, kommersiya/OSS icazəsi balanslı).
  - Veb üçün alternativ: `FastAPI` + `Uvicorn` (əgər brauzer əsaslı təqdimat tələb olunarsa).
- **Çekirdek modulu:** Mövcud biznes məntiqi üçün modul strukturu, `pydantic` ilə verilənlərin doğrulanması.
- **Məlumat mübadiləsi:** `SQLAlchemy` + SQLite (lokal), gələcəkdə PostgreSQL dəstəyi üçün abstraksiya.
- **Testlər:** `pytest`, `pytest-cov`, ssenari əsaslı inteqrasiya testləri.
- **Quraşdırma və Yayım:** `Poetry` ilə paketləmə, `PyInstaller` və ya `Briefcase` ilə icra edilə bilən tətbiq.

## 4. Mərhələlər
1. **Analiz və Arxitektura (Həftə 1-2)**
   - Mövcud kod bazasının auditini aparmaq.
   - Modul sərhədlərini və domen obyektlərini müəyyənləşdirmək.
   - Arxitektura diaqramı və modul məsuliyyətləri.
2. **Çekirdek Refaktoru (Həftə 2-3)**
   - Məzmunu modullara bölmək (domen, xidmət, infrastruktur qatları).
   - `pydantic` modelləri ilə giriş/çıxış validasiyası.
   - Əlaqədar testlər və sənədləşmə.
3. **İnterfeys Layihələndirməsi (Həftə 3-4)**
   - GUI prototipi (Figma / Qt Designer).
   - `PySide6` komponentlərinin ilkin inteqrasiyası.
   - İstifadəçi axınlarının təsdiqi.
4. **İnteqrasiya və Zorlamalar (Həftə 4-5)**
   - Çekirdek modulunu GUI və ya API-lə birləşdirmək.
   - Verilənlər bazası bağlantısının abstraksiyası.
   - Logging (`structlog`), səhv izləmə (`sentry-sdk` opsional).
5. **Test və Keyfiyyət Təmini (Həftə 5-6)**
   - Unit və inteqrasiya testləri.
  - Performans ölçmələri (`pytest-benchmark`).
   - QA ssenarilərinin icrası.
6. **Paketləmə və Yayım (Həftə 6-7)**
   - `Poetry` ilə asılılıqları kilidləmək.
   - `PyInstaller` ilə Windows exe, opsi olaraq macOS/Linux paketləri.
   - CI/CD boru xətti (GitHub Actions) qurmaq.
7. **Sənədləşmə və Təlim (Həftə 7-8)**
   - İstifadəçi təlimatı, texniki sənəd.
   - Daxili komanda üçün təlim sessiyası.

## 5. Kitabxana Tövsiyələri
- `PySide6`: Qt əsaslı GUI, modern və geniş widget dəstəyi.
- `pydantic`: Daxili validasiya və tip təhlükəsizliyi.
- `SQLAlchemy`: ORM və verilənlər bazası abstraksiyası.
- `alembic`: Migrasiya idarəçiliyi.
- `pytest`, `pytest-cov`, `pytest-qt`: Test ekosistemi.
- `structlog`: Strukturlu loglama.
- `Poetry`: Asılılıq idarəetməsi və versiyalaşdırma.
- `PyInstaller` və ya `BeeWare Briefcase`: Tətbiq kimi paketləmə.

## 6. Komanda Rolları və Resurs Planı
- **Layihə rəhbəri:** Planlama, paydaş əlaqəsi.
- **Baş backend mühəndisi:** Çekirdek refaktoru və modul dizaynı.
- **Frontend/GUI mühəndisi:** İstifadəçi interfeysinin implementasiyası.
- **DevOps mühəndisi:** CI/CD, paketləmə, paylama.
- **QA mühəndisi:** Test planlaması, avtomatlaşdırma.

## 7. Risklər və Azaltma Strategiyası
- **Texniki borc:** Refaktor planı, kod review proseduru.
- **Təyinatın gecikməsi:** Sprint əsaslı izləmə, prioritetlərin yenilənməsi.
- **Asılılıqların dəyişməsi:** `Dependabot`/`poetry update` siyasəti, semantik versiyalaşdırma.
- **Performans problemləri:** Erkən optimizasiya deyil, ölçmələrə əsaslanan düzəliş.

## 8. Nəticə
Bu plan Python əsaslı tətbiqin mərhələli şəkildə hazırlanmasını, nüvənin gücləndirilməsini və son istifadəçilər üçün paylana bilən tətbiq formasına gətirilməsini təmin edir. Hər mərhələ üçün konkret tapşırıqlar və alətlər təyin olunmuşdur ki, komanda sinxron şəkildə irəliləyə bilsin.
