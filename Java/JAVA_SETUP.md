# OpenJDK Quraşdırma və Ayarlama Təlimatları

## 🔍 Hal-hazırda vəziyyət
- ❌ Java quraşdırılmayıb
- ❌ javac əmri tapılmır
- ✅ Python quraşdırılıb

## 📥 OpenJDK Quraşdırma (Seçimlər)

### Seçim 1: Chocolatey ilə quraşdırma (Ən sürətli)

1. PowerShell-i administrator olaraq açın
2. Bu əmri icra edin:
```powershell
choco install openjdk -y
```

### Seçim 2: Manual quraşdırma (Tövsiyə edilir)

1. OpenJDK səhifəsinə gedin: https://adoptium.net/
2. **Temurin 21 (LTS)** və ya **Temurin 17 (LTS)** versiyasını seçin
3. Windows x64 MSI installer yükləyin
4. MSI faylını işə salıb quraşdırın
5. Quraşdırma zamanı "Set JAVA_HOME" və "Add to PATH" seçimlərini işarələyin

### Seçim 3: WinGet ilə quraşdırma

PowerShell-də:
```powershell
winget install EclipseAdoptium.Temurin.21.JDK
```

### Seçim 4: ZIP faylından quraşdırma

1. https://adoptium.net/-dan ZIP yükləyin
2. `C:\Program Files\Java\` qovluğuna çıxarın
3. Manual olaraq PATH-a əlavə edin (aşağıda təlimatlar)

## ⚙️ PATH Ayarlaması (Manual üçün)

### PowerShell ilə PATH-a əlavə etmək:

```powershell
# JAVA_HOME dəyişənini təyin edin
[System.Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Program Files\Java\jdk-21", "Machine")

# PATH-a əlavə edin
$currentPath = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
$newPath = $currentPath + ";C:\Program Files\Java\jdk-21\bin"
[System.Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
```

### Windows Settings ilə:

1. **Settings** → **System** → **About** → **Advanced system settings**
2. **Environment Variables** düyməsinə klikləyin
3. **System variables** bölməsində:
   - **New** → `JAVA_HOME` = `C:\Program Files\Java\jdk-21`
   - **Path** seçin → **Edit** → **New** → `%JAVA_HOME%\bin` əlavə edin
4. **OK** ilə bağlayın

## ✅ Yoxlama

Yeni terminal açıb bu əmrləri icra edin:

```bash
java -version
javac -version
echo $JAVA_HOME  # Git Bash-də
echo %JAVA_HOME% # CMD-də
```

## 🚀 Sürətli quraşdırma skripti (setup_java.ps1)

PowerShell skriptini işə salın:
```powershell
.\setup_java.ps1
```

## 📌 Qeydlər

- Quraşdırmadan sonra **bütün terminalları yenidən açın**
- Git Bash-də PATH dəyişiklikləri üçün terminal yenidən başladılmalıdır
- JDK versiyası ən azı 8 olmalıdır (tövsiyə edilir: 17 və ya 21 LTS)

## 🎯 Növbəti addımlar

Quraşdırmadan sonra:
1. Terminal yenidən açın
2. `javac Pıllan.java` ilə kompilyasiya edin
3. `java Pıllan` ilə proqramı işə salın
