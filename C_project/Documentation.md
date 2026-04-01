# Çoxdilli Proqramlaşdırma Proyekti - Sənədləşdirmə

## 📋 Proyekt Haqqında

Bu proyekt **Python**, **C** və **Assembly** dillərinin bir-biri ilə necə əlaqə qurduğunu göstərir.

---

## 🎯 Məqsəd

Müxtəlif proqramlaşdırma dillərinin bir-biri ilə inteqrasiyasını praktiki olaraq öyrənmək:
- **Python ↔ C**: Python-dan C funksiyalarını çağırmaq
- **C ↔ Assembly**: C-dən Assembly funksiyalarını çağırmaq

---

## 📁 Proyekt Strukturu

```
C_project/
│
├── Documentation.md           # Bu fayl (proyekt sənədləşdirməsi)
├── README.md                  # İstifadə təlimatları
│
├── c_module/                  # C dili modulu
│   ├── math_ops.h            # Header fayl (funksiya deklarasiyaları)
│   ├── math_ops.c            # C funksiyaları (toplama əməliyyatı)
│   └── math_ops.dll          # Kompil edilmiş shared library
│
├── asm_module/                # Assembly modulu
│   ├── square.asm            # Assembly funksiyası (kvadrat hesablama)
│   └── square.obj            # Kompil edilmiş obyekt fayl
│
├── python_caller.py           # Python skript (C-ni çağırır)
├── c_caller.c                # C proqram (Assembly-ni çağırır)
└── c_caller.exe              # Kompil edilmiş C proqramı
```

---

## 🔄 Əlaqə Sxemi

```
┌─────────────┐
│   Python    │
│   Script    │
└──────┬──────┘
       │ ctypes
       ↓
┌─────────────┐
│  C Shared   │
│  Library    │
│  (.dll)     │
└──────┬──────┘
       │ extern
       ↓
┌─────────────┐
│  Assembly   │
│  Function   │
└─────────────┘
```

---

## 📝 Planın Addımları

### **1. Proyekt Strukturunun Yaradılması**
**Status**: 🔄 İcrada

**Məqsəd**: Lazımi qovluqlar və əsas faylları yaratmaq

**Əməliyyatlar**:
- ✅ `c_module/` qovluğunu yarat
- ✅ `asm_module/` qovluğunu yarat
- ✅ `Documentation.md` faylını yarat
- ⏳ Digər əsas fayllar

---

### **2. C Modulunun Hazırlanması**
**Status**: ⏳ Gözləmədə

**Məqsəd**: İki ədədi toplayan C funksiyası yazmaq və onu shared library (.dll) olaraq kompil etmək

**Fayllar**:
- `c_module/math_ops.h` - Header fayl
- `c_module/math_ops.c` - Əsas C kodu

**Funksiya**:
```c
int add_numbers(int a, int b);  // İki ədədi toplayır
```

**Kompilyasiya**:
```bash
gcc -shared -o c_module/math_ops.dll c_module/math_ops.c
```

---

### **3. Assembly Modulunun Hazırlanması**
**Status**: ⏳ Gözləmədə

**Məqsəd**: Kvadrat hesablayan Assembly funksiyası yazmaq (NASM sintaksisi)

**Fayl**:
- `asm_module/square.asm`

**Funksiya**:
```asm
global square
square:
    ; int square(int x) - ədədin kvadratını hesablayır
    ; x * x
```

**Kompilyasiya**:
```bash
nasm -f win64 asm_module/square.asm -o asm_module/square.obj
```

---

### **4. C-dən Assembly Çağırma**
**Status**: ⏳ Gözləmədə

**Məqsəd**: C proqramından Assembly funksiyasını çağırmaq

**Fayl**:
- `c_caller.c`

**Kod**:
```c
extern int square(int x);  // Assembly funksiyası

int main() {
    int result = square(5);  // 5^2 = 25
    printf("Nəticə: %d\n", result);
    return 0;
}
```

**Kompilyasiya**:
```bash
gcc c_caller.c asm_module/square.obj -o c_caller.exe
```

---

### **5. Python-dan C Çağırma**
**Status**: ⏳ Gözləmədə

**Məqsəd**: Python-dan ctypes istifadə edərək C library-ni çağırmaq

**Fayl**:
- `python_caller.py`

**Kod**:
```python
import ctypes

# DLL-i yüklə
lib = ctypes.CDLL('./c_module/math_ops.dll')

# Funksiyanı çağır
result = lib.add_numbers(10, 20)
print(f"Nəticə: {result}")
```

---

### **6. Test və Sənədləşdirmə**
**Status**: ⏳ Gözləmədə

**Məqsəd**: Bütün komponentləri test etmək və README yazmaq

**Test Addımları**:
1. ✅ C modulunu kompil et
2. ✅ Assembly modulunu kompil et
3. ✅ C-dən Assembly-ni test et
4. ✅ Python-dan C-ni test et
5. ✅ README.md faylı hazırla

---

## 🛠️ Tələb Olunan Vasitələr

### **Windows üçün**:
- **GCC** (MinGW və ya MSYS2): C kompilyatoru
- **NASM**: Assembly kompilyatoru
- **Python 3.x**: Python interpretoru

### **Quraşdırma**:
```bash
# MSYS2 istifadə edərək
pacman -S mingw-w64-x86_64-gcc
pacman -S nasm

# Python (əgər yoxdursa)
# Python.org saytından yüklə
```

---

## 📚 Əlavə Məlumat

### **ctypes Nədir?**
Python-un standart kitabxanası. C dilində yazılmış shared library-ləri Python-da istifadə etməyə imkan verir.

### **Shared Library (.dll) Nədir?**
Dinamik yüklənən kitabxana. Bir neçə proqram eyni koddan istifadə edə bilər.

### **NASM Nədir?**
Netwide Assembler - Assembly dilini maşın koduna çevirən assembler.

---

## 📖 İstinadlar

- [Python ctypes Documentation](https://docs.python.org/3/library/ctypes.html)
- [GCC Compiler Documentation](https://gcc.gnu.org/onlinedocs/)
- [NASM Documentation](https://www.nasm.us/xdoc/2.15.05/html/nasmdoc0.html)

---

## 📝 Qeydlər

- Bütün kodlar Windows üçün hazırlanıb (64-bit)
- Linux/Mac üçün kiçik dəyişikliklər lazımdır (.dll → .so)
- Assembly x64 arxitekturası üçündür

---

**Proyekt Tarixi**: 02 Yanvar 2026  
**Status**: İnkişaf mərhələsində  
**Müəllif**: Multi-Language Integration Project
