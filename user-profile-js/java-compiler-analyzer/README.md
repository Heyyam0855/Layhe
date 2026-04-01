# Java Compiler Analyzer

Java source fayllarını analiz edən və kompilyasiya prosesini izah edən C++ alətdir.

## 📋 Xüsusiyyətlər

- ✅ Java fayllarındakı class-ları, method-ları, variable-ları tapır
- ✅ Import statement-lərini analiz edir
- ✅ Kompilyasiya mərhələlərini ətraflı izah edir
- ✅ AST (Abstract Syntax Tree) haqqında məlumat verir
- ✅ Rəngli və formatlaşdırılmış terminal output-u
- ✅ Verbose mode ilə ətraflı analiz
- ✅ Command line interfeys

## 🚀 Quraşdırma

### Tələblər

- C++17 və ya daha yeni versiya
- CMake 3.10+
- GCC və ya Clang kompilyator
- (Opsional) Clang library-ləri tam funksional AST analizi üçün

### Build etmə

```bash
# Build qovluğunu yaradın
mkdir build
cd build

# CMake konfiqurasiya
cmake ..

# Kompilyasiya
make

# və ya Windows-da
cmake --build .
```

## 📖 İstifadə

### Əsas istifadə

```bash
# Sadə analiz
./JavaCompilerAnalyzer MyClass.java

# Ətraflı analiz
./JavaCompilerAnalyzer -v MyClass.java

# Yardım
./JavaCompilerAnalyzer --help
```

### Əmrlər

| Əmr | Təsvir |
|-----|--------|
| `-v, --verbose` | Ətraflı output |
| `-h, --help` | Yardım mesajı |
| `-s, --stages` | Kompilyasiya mərhələlərini göstər |
| `-a, --ast` | AST haqqında məlumat |
| `-e, --explain` | Java kompilyatorunu izah et |
| `--create-sample` | Nümunə Java faylı yaradır |

### Nümunə output

```
===============================================================
                    Java Compiler Analyzer                    
===============================================================

[ℹ] Analiz başlayır: Sample.java
[ℹ] Class tapıldı: Sample
[ℹ] Method tapıldı: Sample
[ℹ] Method tapıldı: getName
[✓] Analiz tamamlandı!

===============================================================
                      Analiz Nəticələri                      
===============================================================

Fayl adı            : Sample.java
📊 Sətir sayı: 25
📊 Class sayı: 1
📊 Method sayı: 5
📊 Variable sayı: 3
📊 Import sayı: 2
```

## 🏗️ Layihə Strukturu

```
java-compiler-analyzer/
├── include/                 # Header faylları
│   ├── CompilerAnalyzer.h  # Əsas analyzer class
│   ├── JavaAnalyzer.h      # AST analiz class-ları
│   └── OutputFormatter.h   # Output formatlaşdırma
├── src/                    # Source faylları
│   ├── CompilerAnalyzer.cpp
│   ├── JavaAnalyzer.cpp
│   └── OutputFormatter.cpp
├── build/                  # Build faylları
├── main.cpp               # Əsas proqram
├── CMakeLists.txt         # CMake konfiqurasiya
└── README.md              # Bu fayl
```

## 🔍 Kompilyasiya Mərhələləri

Proqram Java kompilyasiyasının bu mərhələlərini izah edir:

1. **Leksik Analiz** - Token-ların ayrılması
2. **Sintaktik Analiz** - AST yaradılması  
3. **Semantik Analiz** - Tip yoxlaması
4. **Ara Kod** - Platform-müstəqil kod
5. **Optimallaşdırma** - Performans artırımı
6. **Kod Generasiyası** - Final bytecode

## 🧪 Test etmə

```bash
# Nümunə fayl yaradıb test edin
./JavaCompilerAnalyzer --create-sample
./JavaCompilerAnalyzer Sample.java

# Ətraflı test
./JavaCompilerAnalyzer -v Sample.java
```

## 📝 Məlumat

### Dəstəklənən Java elementləri

- ✅ Class declaration-ları
- ✅ Method declaration-ları
- ✅ Variable declaration-ları
- ✅ Import statement-ləri
- ✅ Package statement-ləri
- ✅ Constructor-lar
- ✅ Static method-lar

### Məhdudiyyətlər

- Inner class-lar tam dəstəklənmir
- Generic type-lar tam parse edilmir
- Lambda expression-lar analiz edilmir
- Annotation-lar oxunmur

## 🛠️ İnkişaf

### Yeni xüsusiyyət əlavə etmə

1. `include/` qovluğunda header-ləri yeniləyin
2. `src/` qovluğunda implementation əlavə edin
3. `main.cpp`-də command line seçimlərini əlavə edin
4. CMakeLists.txt-ni yeniləyin (lazımsa)

### Debug etmə

```bash
# Debug mode ilə build edin
cmake -DCMAKE_BUILD_TYPE=Debug ..
make

# GDB ilə debug edin
gdb ./JavaCompilerAnalyzer
```

## 📚 Əlavə məlumat

### Faydalı linklər

- [CMake Documentation](https://cmake.org/documentation/)
- [Clang AST Documentation](https://clang.llvm.org/docs/IntroductionToTheClangAST.html)
- [Java Language Specification](https://docs.oracle.com/javase/specs/)

### Əməkdaşlıq

1. Fork edin
2. Feature branch yaradın
3. Commit edin
4. Push edin
5. Pull Request göndərin

## 📄 Lisenziya

Bu layihə MIT lisenziyas altında paylaşılır.

## 👨‍💻 Müəllif

Java Compiler Analyzer - C++ ilə yazılmış Java kod analiz aləti

---

**Qeyd:** Bu alət təhsil məqsədilə yaradılıb və kompilyator texnologiyalarını öyrənmək üçün nəzərdə tutulub.