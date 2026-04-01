# C++ Kompilyatorları: Bayt Kodu və Binar Kod

## Ümumi Məlumat

Bu layihə C++ kompilyatorlarının necə işlədiyini, bayt kodu ilə binar kod arasındakı fərqləri və CPU/RAM ilə işləməni izah edir.

## Əsas Konsepsiyalar

### 1. Binar Kod (Binary Code)
- **CPU üçün**: Binar kod birbaşa CPU tərəfindən icra olunan maşın kodudur
- **Format**: 0 və 1-lərdən ibarətdir
- **Sürət**: Çox sürətlidir, çünki tərcümə lazım deyil
- **Platforma**: Platforma-spesifikdir (Windows/Linux/Mac)

### 2. Bayt Kodu (Bytecode)
- **Virtual Maşın üçün**: Virtual maşın tərəfindən icra olunan ara formatdır
- **Format**: Bayt səviyyəsində təmsil olunur
- **Platforma**: Platforma-müstəqildir
- **Tərcümə**: JIT (Just-In-Time) və ya interpretasiya lazımdır

### 3. CPU və RAM
- **RAM**: Məlumatları binar formatda (0 və 1) saxlayır
- **CPU**: Binar kodları birbaşa icra edir
- **Əlaqə**: CPU və RAM binar kodla işləyir, buna görə qismən yaxındır

## Kompilyasiya Prosesi

### C++ Native Kompilyator (GCC, Clang, MSVC)
```
C++ Mənbə Kodu (.cpp)
    ↓
Kompilyator (g++, clang++, MSVC)
    ↓
Binar Kod (.exe, .o, .obj)
    ↓
CPU tərəfindən icra
```

### LLVM Kompilyator (Bayt Kodu ilə)
```
C++ Mənbə Kodu (.cpp)
    ↓
LLVM Frontend
    ↓
LLVM IR (Intermediate Representation - Bayt Kodu)
    ↓
LLVM Backend
    ↓
Binar Kod (CPU üçün)
```

## Kompilyasiya və İcra

### Windows üçün:
```bash
# Kompilyasiya
g++ cpp_compiler_concepts.cpp -o compiler_concepts.exe

# İcra
./compiler_concepts.exe
```

### Linux/Mac üçün:
```bash
# Kompilyasiya
g++ cpp_compiler_concepts.cpp -o compiler_concepts

# İcra
./compiler_concepts
```

## Fərqlər

| Xüsusiyyət | Binar Kod | Bayt Kodu |
|------------|-----------|-----------|
| İcra | CPU birbaşa | Virtual Maşın |
| Platforma | Spesifik | Müstəqil |
| Sürət | Çox sürətli | Nisbətən yavaş |
| Format | 0 və 1 | Bayt səviyyəsi |
| Tərcümə | Lazım deyil | Lazımdır |

## CPU və RAM İlə İşləmə

1. **RAM-də saxlanılma**: Bütün məlumatlar RAM-də binar formatda (0 və 1) saxlanılır
2. **CPU icrası**: CPU binar kodları oxuyur və birbaşa icra edir
3. **Əlaqə**: CPU və RAM hər ikisi binar kodla işləyir, buna görə qismən yaxındır

## Nümunə Kod

`cpp_compiler_concepts.cpp` faylında aşağıdakı nümunələr var:
- Binar kod nümunələri
- Bayt kodu konsepsiyası
- CPU və RAM ilə işləmə
- Kompilyator növləri
- Praktik nümunələr

## Əlavə Məlumat

- C++ kompilyatorları adətən birbaşa binar kod yaradır
- LLVM kimi bəzi kompilyatorlar ara format (IR) istifadə edir
- Binar kod CPU-nun başa düşdüyü formatdadır
- RAM və CPU binar kodla işləyir, buna görə qismən yaxındır

