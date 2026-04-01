# C++ Kompilyator Quraşdırma Təlimatı (Windows)

## Problem: `g++: command not found`

Bu xəta o deməkdir ki, sistemdə C++ kompilyatoru quraşdırılmayıb.

## Həll yolları:

### 1️⃣ WinLibs (Ən asan yol) ⭐

1. **Yükləyin:**
   - https://winlibs.com/ saytına daxil olun
   - "Download" bölməsindən ən son versiyanı yükləyin
   - ZIP faylını çıxarın (məsələn: `C:\mingw64`)

2. **PATH-ə əlavə edin:**
   - Windows-da "Environment Variables" açın
   - System Variables-də `Path`-i tapın və Edit edin
   - `C:\mingw64\bin` qovluğunu əlavə edin

3. **Yoxlayın:**
   ```bash
   g++ --version
   ```

### 2️⃣ MSYS2 (Paket idarəçisi ilə)

1. **MSYS2 yükləyin:**
   - https://www.msys2.org/ saytından yükləyin
   - Quraşdırın

2. **MSYS2 terminalini açın və:**
   ```bash
   pacman -Syu
   pacman -S mingw-w64-x86_64-gcc
   ```

3. **Git Bash-də işləmək üçün PATH-ə əlavə edin:**
   - `C:\msys64\mingw64\bin`

### 3️⃣ Chocolatey ilə (paket idarəçisi)

```bash
choco install mingw
```

### 4️⃣ Visual Studio Community (Tam IDE)

1. Visual Studio Community yükləyin
2. Quraşdırma zamanı "Desktop development with C++" seçin
3. Developer Command Prompt-dan `cl.exe` istifadə edin

## Quraşdırmadan sonra:

1. **Terminali yenidən başladın** (Git Bash)
2. **Yoxlayın:**
   ```bash
   g++ --version
   ```
3. **Test edin:**
   ```bash
   g++ main.cpp -o main.exe
   ./main.exe
   ```

## Alternativ: Online kompilyatorlar

Quraşdırma etmədən test etmək üçün:
- https://www.onlinegdb.com/online_c++_compiler
- https://cpp.sh/
- https://replit.com/languages/cpp

