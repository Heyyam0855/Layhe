# C++ Portfolio Layihəsi

Bu layihə C++ proqramçılıq bacarıqlarını nümayiş etdirmək üçün hazırlanmış comprehensive bir portflio tədbiqidir.

## Özəlliklər

- **Modular Arxitektura**: Ayrı-ayrı modullar (Calculator, FileManager, DataProcessor)
- **Modern C++**: C++17/C++20 standartları, RAII, smart pointers
- **Cross-platform**: Windows (MinGW), Linux, macOS dəstəyi
- **CLI Interface**: Command-line və interactive məntiq
- **Unit Testing**: Test infrastructure dəstəyi
- **CMake Build**: Modern build sistemi

## Modullar

### 1. Calculator Module
- Sadə arifmetik əməliyyatlar (+ - * /)
- Error handling və input validation
- İnteraktiv hesablayıcı interfeysi

### 2. File Manager Module  
- Fayl və qovluq əməliyyatları
- Fayl yaratma, silmə, siyahılanması
- Filesystem API istifadəsi

### 3. Data Processor Module
- Rəqəmsal məlumat analizi
- Statistik hesablamalar (ortalama, min, max)
- Məlumat strukturları və alqoritmlər

## Quraşdırma və İstifadə

### Tələblər
- **Kompaylər**: GCC 8.0+ (MinGW-w64), Clang 10+, MSVC 2019+
- **Build Sistemi**: CMake 3.15+
- **C++ Standart**: C++17 və ya daha yeni

### Windows (MSYS2/MinGW) üçün
```bash
# MSYS2 paketlərini quraşdırın
pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-make

# Layihəni klonlayın və build edin
git clone <repository-url>
cd Tedbiq
mkdir build && cd build
cmake ..
make

# Və ya
cmake --build .
```

### Linux üçün
```bash
# Tələbləri quraşdırın
sudo apt update
sudo apt install build-essential cmake

# Build edin
mkdir build && cd build
cmake ..
make -j$(nproc)
```

### Proqramı işə salın
```bash
# Köməyə baxın
./portfolio_app --help

# Müxtəlif modulları işə salın
./portfolio_app --calculator
./portfolio_app --filemanager  
./portfolio_app --dataprocessor

# İnteraktiv rejim
./portfolio_app --interactive
```

## İnkişaf

### Layihə Strukturu
```
Tedbiq/
├── src/                    # Kaynak kodları
│   ├── main.cpp           # Ana giriş faylı
│   ├── core/              # Əsas sistem komponentləri
│   │   └── Application.cpp
│   ├── modules/           # Ayrı funksional modullar
│   │   ├── Calculator/
│   │   ├── FileManager/
│   │   └── DataProcessor/
│   └── tests/             # Unit testlər
├── include/               # Header faylları
├── lib/                   # Xarici kitabxanalar
├── build/                 # Build nəticələri
├── docs/                  # Dokumentasiya
├── examples/              # İstifadə nümunələri
├── CMakeLists.txt         # Build konfiqurasiyası
└── README.md             # Bu fayl
```

### Yeni Modul Əlavə Etmək
1. `src/modules/` qovluğunda yeni qovluq yaradın
2. Header faylını `include/` qovluğuna əlavə edin
3. `CMakeLists.txt`-ə source faylları əlavə edin
4. `Application.cpp`-də modulu qeydiyyatdan keçirin

### Testing
```bash
# Testləri build etmək üçün
cmake -DBUILD_TESTS=ON ..
make
ctest
```

### Documentation
```bash
# Dokumentasiya yaratmaq üçün (Doxygen lazımdır)
cmake -DBUILD_DOCS=ON ..
make docs
```

## Texniki Detallar

### İstifadə Edilən Texnologiyalar
- **STL**: Containers, algorithms, smart pointers
- **Exception Handling**: RAII və exception safety
- **Design Patterns**: Factory, Command patterns
- **Modern C++**: Auto keyword, range-based loops, lambda expressions

### Performance Göstəriciləri
- Startup vaxtı: < 1 saniyə
- Yaddaş istifadəsi: < 50MB
- CPU-efficient alqoritmlər

### Kod Keyfiyyəti
- **Style Guide**: Google C++ Style Guide
- **Static Analysis**: clang-tidy dəstəyi
- **Memory Safety**: AddressSanitizer dəstəyi

## Gələcək Planlar

### v1.1 Özəllikləri
- [ ] JSON konfiqurasiya faylı dəstəyi
- [ ] Logging sistemi (spdlog)
- [ ] Network communication module
- [ ] Database connectivity (SQLite)

### v2.0 Özəllikləri  
- [ ] GUI interface (Qt və ya wxWidgets)
- [ ] Plugin sistemi
- [ ] Advanced data visualization
- [ ] Multi-threading support

## Lisenziya

Bu layihə təhsil və portfolio məqsədləri üçün hazırlanmışdır.

## Müəllif

**[Sizin Adınız]**
- Email: [email@example.com]
- LinkedIn: [profil linki]
- GitHub: [github profili]

## Kömək və Dəstək

Problemlər və ya suallar üçün:
1. GitHub Issues bölməsindən istifadə edin
2. Email göndərin
3. Pull request göndərin

---

*Bu layihə MinGW-w64/MSYS2 mühitində hazırlanmış və test edilmişdir.*