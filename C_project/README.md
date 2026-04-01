# 🚀 Çoxdilli Proqramlaşdırma Proyekti

**Python ↔ C ↔ Assembly** inteqrasiyasını göstərən praktiki layihə.

---

## 📋 Proyekt Haqqında

Bu proyekt üç müxtəlif proqramlaşdırma dilinin bir-biri ilə əlaqəsini nümayiş etdirir:
- **Python** → C funksiyalarını çağırır (ctypes vasitəsilə)
- **C** → Assembly funksiyalarını çağırır (extern vasitəsilə)
- **Assembly** → Maşın səviyyəsində əməliyyatlar icra edir

---

## 🏗️ Proyekt Strukturu

```
C_project/
│
├── Documentation.md           # Ətraflı texniki sənədləşdirmə
├── README.md                  # Bu fayl
│
├── c_module/                  # C modulu
│   ├── math_ops.h            # Header fayl
│   ├── math_ops.c            # C funksiyaları
│   └── math_ops.dll          # Kompil edilmiş library (yaradılacaq)
│
├── asm_module/                # Assembly modulu
│   ├── square.asm            # Assembly funksiyası
│   └── square.obj            # Kompil edilmiş obyekt (yaradılacaq)
│
├── python_caller.py           # Python → C
├── c_caller.c                # C → Assembly
└── c_caller.exe              # Kompil edilmiş C proqramı (yaradılacaq)
```

---

## ⚙️ Quraşdırma

### **Tələb olunan proqramlar:**

1. **GCC Compiler** (MinGW və ya MSYS2):
   ```bash
   # MSYS2 istifadə edərək
   pacman -S mingw-w64-x86_64-gcc
   ```

2. **NASM Assembler**:
   ```bash
   pacman -S nasm
   ```

3. **Python 3.x**:
   - [Python.org](https://www.python.org/downloads/) saytından yükləyin

---

## 🔨 Qurma və İşə Salma

### **Addım 1: Assembly Modulunu Kompil Edin**

```bash
# square.asm-ı obyekt fayla çevir
nasm -f win64 asm_module/square.asm -o asm_module/square.obj
```

**Nəticə:** `asm_module/square.obj` faylı yaranacaq.

---

### **Addım 2: C Modulunu Shared Library Olaraq Kompil Edin**

```bash
# C kodunu DLL-ə çevir
gcc -shared -o c_module/math_ops.dll c_module/math_ops.c
```

**Nəticə:** `c_module/math_ops.dll` faylı yaranacaq.

---

### **Addım 3: C Proqramını Assembly ilə Kompil Edin**

```bash
# C proqramını Assembly obyekti ilə əlaqələndir
gcc c_caller.c asm_module/square.obj -o c_caller.exe
```

**Nəticə:** `c_caller.exe` faylı yaranacaq.

---

## ▶️ İcra

### **1. C → Assembly Testini İşə Salın**

```bash
./c_caller.exe
```

**Gözlənilən Nəticə:**
```
========================================
  C <-> Assembly İnteqrasiya Testi
========================================

Ədəd: 5
Kvadrat: 5^2 = 25

========================================
✓ Assembly funksiyası uğurla çağırıldı!
========================================
```

---

### **2. Python → C Testini İşə Salın**

```bash
python python_caller.py
```

**Gözlənilən Nəticə:**
```
==================================================
  Python <-> C İnteqrasiya Testi
==================================================

✓ Library yükləndi: c_module/math_ops.dll

Ədəd 1: 15
Ədəd 2: 27
Cəm: 15 + 27 = 42

==================================================
✓ C funksiyası uğurla çağırıldı!
==================================================
```

---

## 🧪 Funksiyaların İzahı

### **C Funksiyası (`add_numbers`)**
- **Fayl:** `c_module/math_ops.c`
- **İş:** İki ədədi toplayır
- **İmza:** `int add_numbers(int a, int b)`

### **Assembly Funksiyası (`square`)**
- **Fayl:** `asm_module/square.asm`
- **İş:** Ədədin kvadratını hesablayır
- **İmza:** `int square(int x)`
- **Çağırma konvensiyası:** Windows x64 (RCX - ilk arqument)

---

## 🔍 Problemlərin Həlli

### **Xəta: "gcc tapılmadı"**
**Həll:** GCC-nin PATH-a əlavə olunduğundan əmin olun:
```bash
# MSYS2 üçün
export PATH="/mingw64/bin:$PATH"
```

### **Xəta: "nasm tapılmadı"**
**Həll:** NASM-i quraşdırın və PATH-a əlavə edin.

### **Xəta: "math_ops.dll tapılmadı"**
**Həll:** Əvvəlcə Addım 2-ni icra edin (DLL yaradın).

### **Xəta: Python-da "OSError: [WinError 126]"**
**Həll:** DLL-in doğru yerdə olduğundan və GCC ilə düzgün kompil edildiyindən əmin olun.

---

## 📚 Əlavə Oxu

- **Python ctypes:** [Rəsmi Sənədlər](https://docs.python.org/3/library/ctypes.html)
- **NASM:** [Assembler Təlimatları](https://www.nasm.us/xdoc/)
- **GCC:** [GNU Compiler Sənədləri](https://gcc.gnu.org/onlinedocs/)
- **Windows x64 Calling Convention:** [Microsoft Docs](https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention)

---

## 📝 Qeydlər

- ✅ Windows 64-bit üçün hazırlanıb
- ℹ️ Linux/Mac üçün `.dll` → `.so` dəyişikliyi lazımdır
- ℹ️ Assembly x64 arxitekturası üçündür

---

## 🎓 Nə Öyrənəcəksiniz?

1. ✅ **ctypes** ilə Python-dan C çağırma
2. ✅ **extern** ilə C-dən Assembly çağırma
3. ✅ **Shared Library** (DLL) yaratma
4. ✅ **Windows x64 calling convention** anlayışı
5. ✅ Cross-language development təcrübəsi

---

## 📞 Əlaqə

**Müəllif:** Multi-Language Integration Project  
**Tarix:** 02 Yanvar 2026  
**Status:** ✅ Hazır

---

## 📜 Lisenziya

Bu proyekt təhsil məqsədlidir və sərbəst istifadə oluna bilər.
