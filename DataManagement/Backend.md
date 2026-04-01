# Backend üçün Öyrənmə Planı (8 həftə)

Məqsəd: sıfırdan başlayıb REST API + məlumat bazası ilə 1–2 kiçik backend tətbiqi hazırlamaq. Gündə 60–90 dəqiqə kifayətdir.

## Necə işləməli
- Gündəlik “20–20–20”: qısa oxu → qısa video/izləmə → praktika.
- Praktika üstün: hər mövzudan sonra ən az 1 kiçik tapşırıq.
- Resurslar: MDN (HTTP), FastAPI/Flask sənədləri, SQLBolt, w3schools (baza üçün), YouTube-dan qısa dərslər.

## Bu repodakı fayllardan istifadə
- İş faylları: `run.py` (başlanğıc server faylı), `data.db` (SQLite məlumat bazası), lazım olduqda `main.html/css/js` ilə sadə frontend testləri.
- Backend üçün tövsiyə: tədricən `app/` qovluğu altında struktur qurmaq (məs: `app/main.py`, `app/models.py`, `app/schemas.py`, `app/routes.py`). Mövcud `run.py` ilə başlaya və sonra köçürə bilərsiniz.
- Konfiqurasiya dəyişənləri üçün `.env` düşünün (API açarları, sirlər). Git-ə əlavə etməyin.

---

## Həftə 1 — Python və mühitin qurulması
Mövzular:
- Python əsasları: dəyişənlər, funksiyalar, modul/import, paketləndirmə, tip ipucları (typing).
- Virtual mühit və paket idarəetməsi, VS Code Debug.
- CLI-dən oxuma-yazma, fayl əməliyyatları.

Tapşırıq:
- `run.py`-də sadə “Hello API”/səhiyyə yoxlaması (məs: `/health` JSON cavabı) üçün skeleton yaradın (hələ framework-süz).

Mini-yoxlama:
- Kod PEP8-ə yaxın formatdadır?
- Layihə virtual mühitdə işləyir?

## Həftə 2 — HTTP/REST əsasları və framework seçimi
Mövzular:
- HTTP metodları, status kodları, başlıqlar, JSON.
- REST prinsipləri, resurslar, idempotentlik.
- Framework: FastAPI (tövsiyə) və ya Flask; ASGI/WSGI fərqi, Uvicorn.

Tapşırıq:
- FastAPI ilə start: `/health`, `/version` endpoint-ləri; Pydantic sxemləri ilə 1 resurs üçün in-memory CRUD (create/list/get/delete).

Mini-yoxlama:
- OpenAPI/Swagger səhifəsi açılır?
- Xətalar üçün düzgün status kodları qaytarılır?

## Həftə 3 — Məlumat bazası: SQL və SQLite
Mövzular:
- SQL əsasları: cədvəllər, sorğular, məhdudiyyətlər, indekslər.
- SQLite ilə lokal DB (`data.db`), ORM anlayışı (SQLAlchemy) vs düz `sqlite3`.
- Model dizaynı və əlaqələr (1:N).

Tapşırıq:
- Seçilmiş resurs üçün DB cədvəli yaradın və CRUD-u DB üzərindən işlədin. `data.db` istifadə edin.

Mini-yoxlama:
- Xətalar try/except ilə idarə olunur?
- “Not Found” üçün 404, unikallıq üçün 409 qaytarılır?

## Həftə 4 — Autentikasiya və təhlükəsizlik
Mövzular:
- Şifrə saxlama: hashing (bcrypt), “salt”.
- Sessiya vs JWT (tövsiyə: Bearer JWT), qorunan marşrutlar.
- CORS, konfiqurasiya və sirlər (.env), minimal RBAC.

Tapşırıq:
- `signup`/`login` endpoint-ləri, JWT ilə qorunan `me` marşrutu; şifrələr hash-lənir.

Mini-yoxlama:
- Token müddəti və yenilənməsi planlanıb?
- CORS düzgün konfiqurasiya olunub?

## Həftə 5 — Validasiya, səhv idarəetməsi, logging
Mövzular:
- Pydantic ilə giriş validasiyası; xüsusi Exception handler-lar.
- Structured logging (məs: `logging` modulu), request-id izləmə ideyası.
- Sürət məhdudiyyəti (rate limit) və təhlükəsizlik başlıqları (konseptual).

Tapşırıq:
- Qlobal error handler əlavə edin; yanlıș input üçün 422, biznes qaydaları üçün 400/409 verin. Istifadəçi fəaliyyətlərini loglayın.

Mini-yoxlama:
- Log səviyyələri (INFO/ERROR) düzgündür?
- Validasiyada mesajlar aydındır?

## Həftə 6 — Asinxron iş və xarici API-lər
Mövzular:
- `async/await` ilə asinxron endpoint-lər, HTTP müştəri (httpx).
- Zənglərdə timeout/retry strategiyası; sadə keş (in-memory) və ya ETag-lar.
- Background tasks (FastAPI BackgroundTasks) və ya scheduler anlayışı.

Tapşırıq:
- Xarici açıq API-dən məlumat çəkən endpoint yazın; yüklənmə vəziyyəti, səhv mesajları və caching tətbiq edin.

Mini-yoxlama:
- Xarici API dayananda düzgün 502/504 siyasəti var?
- Timeout və retry konfiqurasiya edilib?

## Həftə 7 — Testlərlə keyfiyyət və sənədləşmə
Mövzular:
- `pytest` ilə unit və inteqrasiya testləri; test client (FastAPI TestClient).
- Test üçün müvəqqəti SQLite DB/fixture-lər.
- Coverage, sadə CI (GitHub Actions), avtomatik OpenAPI sənədləri.

Tapşırıq:
- Əsas marşrutlar üçün testlər yazın (happy path + 1–2 kənar hal). Coverage ≥ 70% hədəfləyin.

Mini-yoxlama:
- Testlər deterministikdir?
- OpenAPI sxemi real cavablarla üst-üstə düşür?

## Həftə 8 — Kiçik Layihə 1–2: Tamamlama və dərc
İdeyalar:
- Qeydlər/Todo API (istifadəçi + CRUD + `data.db` davamlılıq + JWT).
- Hava proqnozu proxy API (xarici API + caching + rate limit konsepti).
- Kiçik “valyuta çevirmə” servisi (kurs API + formatlama + validasiya).

Çatdırılma:
- Mobil-öncə düşünülmüş API cavabları (yığcam JSON), səhv idarəetməsi, əsas təhlükəsizlik.
- Lokal “run” ssenarisi (README-də), OpenAPI linki və minimum deploy planı (Render/Railway/Docker opsional).

---

## Yoxlama siyahısı (Checklist)
- [ ] Python və mühit: venv, paketlər, struktur
- [ ] HTTP/REST: metodlar, statuslar, JSON cavablar
- [ ] Framework: FastAPI/Flask ilə işlək endpoint-lər
- [ ] DB: SQLite (`data.db`), ORM və CRUD
- [ ] Auth: JWT, şifrə hashing, qorunan marşrutlar
- [ ] Validasiya və xətalar: düzgün status kodları, aydın mesajlar
- [ ] Logging və (konseptual) rate limiting
- [ ] Asinxron: `async/await`, timeout/retry, caching
- [ ] Testlər: pytest, coverage, minimal CI
- [ ] Layihə(lər): 1–2 mini tətbiq tamamlanıb

## Faydalı praktikalar
- Kiçik və aydın commit mesajları; PR-larla baxış.
- `.env` ilə sirləri saxlayın; konfiqurasiyanı koddan ayırın.
- DevTools və curl/Postman/Insomnia ilə API testləri.
- Kodu formatlayın və lint edin (Black/Flake8 və s.).

## Növbəti addımlar
- Deploy: Docker, Nginx/Reverse proxy, HTTPS.
- Məlumat bazası: Postgres, miqrasiya (Alembic), indeks strategiyası.
- Background işlər: Celery/RQ, mesajlaşma (Redis, RabbitMQ).
- Müşahidəediləbilənlik: metrİkalar, tracing (OTel), səhv izləmə (Sentry).

Uğurlar! Planı izləyərək hər həftə 1–2 endpoint/komponent tamamlayın və `run.py` + `data.db` üzərində praktikaya çevirin. Ehtiyac olduqda strukturlaşdırmanı `app/` altına tədricən daşıyın.
