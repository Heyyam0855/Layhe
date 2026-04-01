## Sertifikat və Qanuni Status

### Fərqlər:

**1. Test Signing (Test İmzalama)**
- Yalnız **öz kompüterinizdə** istifadə üçün
- Pulsuz, qanuni
- Başqa kompüterlərə yayıla bilməz
```powershell
# Test rejimi aktivləşdirmə
bcdedit /set testsigning on
# Öz-özünə imzalama
makecert -r -pe -n "CN=TestCert" ...
```

**2. EV Code Signing Certificate**
- **DigiCert, Sectigo** və s. şirkətlərdən alınır
- Qiymət: ~$300-500/il
- Şirkət/fərdi sahibkarlıq tələb olunur
- **Public istifadə üçün qanunidir**

### Qanuni Məsələlər:

✅ **Qanuni hallara:**
- Öz sisteminizdə test/inkişaf
- Şəxsi driver-lər yaratmaq
- Açıq mənbə proyektlər
- Kommersiya məhsulları (düzgün sertifikatla)

❌ **Qeyri-qanuni hallara:**
- Virus/malware yaratmaq
- Windows-un təhlükəsizliyini sındırmaq
- Başqalarının sistemlərinə icazəsiz müdaxilə
- Sertifikatı sui-istifadə etmək

### Microsoft-un Yoxlaması:

Microsoft **nə driver yazdığınızı izləmir**, ancaq:
- WHQL sertifikasiyası istəsəniz, kod yoxlanılır
- Zərərli fəaliyyət aşkarlanarsa, sertifikat ləğv edilir
- Windows Defender avtomatik analiz edir

### Məsləhət:

**Öz sisteminiz üçün:** Test signing istifadə edin - tam qanunidir və pulsuz.

**Kommersiya/paylaşma üçün:** EV sertifikat alın və kod standartlarına riayət edin.

Çəkirdək səviyyə kodunuz qanunları pozmazsa, Microsoft-la heç bir problem olmaz.