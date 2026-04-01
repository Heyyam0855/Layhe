# 🚀 SÜRƏTLI BAŞLANĞIC

## Hal-hazırda vəziyyət
❌ **Java/OpenJDK quraşdırılmayıb** - Pıllan işləməyəcək

## ⚡ 3 Addımda Quraşdırma

### 1️⃣ OpenJDK Quraşdırın

**Ən sürətli yol (tövsiyə):**
- **PowerShell-i Administrator olaraq açın**
- Bu əmri kopyalayıb yapışdırın:
```powershell
winget install EclipseAdoptium.Temurin.21.JDK
```

**və ya Manual:**
- https://adoptium.net/ - MSI installer yükləyin və quraşdırın

### 2️⃣ Terminal Yenidən Açın
- Bütün açıq terminalları **bağlayın**
- VS Code-u **yenidən başladın**
- Yeni terminal açın

### 3️⃣ Yoxlayın və İşə Salın
```bash
java -version    # Java versiyasını göstərməlidir
javac -version   # Compiler versiyasını göstərməlidir

# Pıllan-ı kompilyasiya edin
javac Pıllan.java

# İcra edin
java Pıllan
```

## 📁 Mövcud Fayllar

| Fayl | Təsvir |
|------|--------|
| `Pıllan.java` | Əsas proqram - Python çağıran Java class |
| `Pıllan.md` | Təfsilatlı istifadə təlimatları |
| `test_script.py` | Test üçün Python skripti |
| `JAVA_SETUP.md` | Ətraflı Java quraşdırma təlimatları |
| `setup_java.ps1` | Avtomatik quraşdırma skripti (PowerShell) |
| `check_java.bat` | Java yoxlama skripti (Batch) |
| `BAŞLANĞIC.md` | Bu fayl |

## ❓ Kömək

**Java quraşdırılıbmı yoxlamaq:**
```bash
java -version
```

**Ətraflı təlimatlar:**
- Bax: [JAVA_SETUP.md](JAVA_SETUP.md)

**Pıllan istifadəsi:**
- Bax: [Pıllan.md](Pıllan.md)

## 🎯 Növbəti Addım
➡️ **İndi OpenJDK quraşdırın!** (Yuxarıdakı Addım 1)
