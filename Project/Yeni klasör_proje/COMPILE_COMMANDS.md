# C++ Kompilyasiya Əmrləri

## ⚠️ Əgər `g++: command not found` xətası alırsınızsa:

Sistemdə `g++` kompilyatoru quraşdırılmayıb. Aşağıdakı yollardan birini seçin:

### Seçim 1: MinGW-w64 quraşdırmaq (Tövsiyə olunur)

1. **MinGW-w64 yükləyin:**
   - https://www.mingw-w64.org/downloads/ saytına daxil olun
   - Və ya birbaşa: https://winlibs.com/ (asan quraşdırma üçün)

2. **Quraşdırma:**
   - Yüklənmiş faylı açın və quraşdırın
   - Quraşdırma zamanı `bin` qovluğunu PATH-ə əlavə edin

3. **Yoxlama:**
   ```bash
   g++ --version
   ```

### Seçim 2: MSYS2 istifadə etmək

1. MSYS2 yükləyin: https://www.msys2.org/
2. Terminaldə:
   ```bash
   pacman -S mingw-w64-x86_64-gcc
   ```
3. PATH-ə əlavə edin: `C:\msys64\mingw64\bin`

### Seçim 3: Visual Studio Build Tools

1. Visual Studio Build Tools yükləyin
2. "Desktop development with C++" komponentini seçin
3. `cl.exe` kompilyatorunu istifadə edin

### Seçim 4: Online kompilyator (tez test üçün)

- https://www.onlinegdb.com/online_c++_compiler
- https://cpp.sh/
- https://godbolt.org/

---

## Windows üçün C++ Kompilyator Əmrləri

### 1. GCC/G++ (MinGW) istifadə edərək:

**Sadə kompilyasiya:**
```bash
g++ main.cpp -o main.exe
```

**Kompilyasiya və işə salma:**
```bash
g++ main.cpp -o main.exe && ./main.exe
```

**Optimizasiya ilə kompilyasiya:**
```bash
g++ -O2 main.cpp -o main.exe
```

**Çoxlu faylları kompilyasiya etmək:**
```bash
g++ file1.cpp file2.cpp -o program.exe
```

**Standart və xəbərdarlıqlar ilə:**
```bash
g++ -std=c++17 -Wall -Wextra main.cpp -o main.exe
```

### 2. MSVC (Microsoft Visual C++) istifadə edərək:

**cl.exe kompilyatoru ilə:**
```bash
cl main.cpp /EHsc /Fe:main.exe
```

**Və ya:**
```bash
cl /EHsc main.cpp
```

### 3. Clang istifadə edərək:

```bash
clang++ main.cpp -o main.exe
```

## Əmrlərin izahı:

- `g++` / `clang++` - C++ kompilyatoru
- `main.cpp` - mənbə faylı
- `-o main.exe` - çıxış faylının adı
- `-O2` - optimizasiya səviyyəsi
- `-std=c++17` - C++ standartı
- `-Wall` - bütün xəbərdarlıqları göstər
- `-Wextra` - əlavə xəbərdarlıqlar

## İşə salma:

Windows-da:
```bash
./main.exe
```

Və ya sadəcə:
```bash
main.exe
```

