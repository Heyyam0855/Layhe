# Python + C++ İnteqrasiya Layihəsi

## 📖 Haqqında

Bu layihə Python və C++ proqramlaşdırma dillərini **pybind11** istifadə edərək birləşdirir. Məqsəd Python-un istifadə rahatlığını C++-ın yüksək performansı ilə birləşdirməkdir.

## 🚀 Başlanğıc

### Tələblər

- Python 3.8+
- C++ Kompilyator (MSVC, GCC, və ya Clang)
- CMake 3.15+
- pybind11

### Quraşdırma

1. **Asılılıqları quraşdırın:**
   ```bash
   pip install -r requirements.txt
   ```

2. **C++ modulunu kompilyasiya edin:**
   ```bash
   mkdir build
   cd build
   cmake ../src/cpp
   cmake --build . --config Release
   ```

3. **Testləri işə salın:**
   ```bash
   # Python testləri
   pytest tests/test_python.py -v
   
   # C++ testləri
   cd build
   ./test_cpp
   ```

## 📁 Layihə Strukturu

```
project/
├── src/
│   ├── cpp/           # C++ mənbə kodları
│   │   ├── calculator.cpp
│   │   ├── calculator.h
│   │   ├── bindings.cpp
│   │   └── CMakeLists.txt
│   └── python/        # Python kodları
│       ├── main.py
│       ├── wrapper.py
│       └── utils.py
├── build/             # Kompilyasiya edilmiş fayllar
├── tests/             # Test faylları
├── docs/              # Sənədləşdirmə
└── requirements.txt   # Python asılılıqları
```

## 💻 İstifadə

### Əsas İstifadə

```python
from wrapper import Calculator, MathFunctions, ArrayProcessor

# Hesablama
result = Calculator.add(5, 3)        # 8
product = Calculator.multiply(4, 2)   # 8.0

# Riyazi funksiyalar
fact = MathFunctions.factorial(5)     # 120
fib = MathFunctions.fibonacci(10)     # 55
prime = MathFunctions.is_prime(17)    # True

# Massiv əməliyyatları
import numpy as np
arr = np.array([1.0, 2.0, 3.0])
total = ArrayProcessor.sum(arr)       # 6.0
```

### Birbaşa C++ Modulu

```python
import calculator

# C++ funksiyalarını birbaşa çağırın
result = calculator.add(10, 20)
factorial = calculator.factorial(10)
```

## 📊 API Referansı

### Calculator

| Metod | Təsvir | Parametrlər | Qaytarır |
|-------|--------|-------------|----------|
| `add(a, b)` | Toplama | int, int | int |
| `subtract(a, b)` | Çıxma | int, int | int |
| `multiply(a, b)` | Vurma | float, float | float |
| `divide(a, b)` | Bölmə | float, float | float |

### MathFunctions

| Metod | Təsvir |
|-------|--------|
| `factorial(n)` | n! hesablayır |
| `fibonacci(n)` | n-ci Fibonacci ədədi |
| `is_prime(n)` | Sadə ədəd yoxlaması |
| `gcd(a, b)` | Ən böyük ortaq bölən |
| `lcm(a, b)` | Ən kiçik ortaq bölünən |

### ArrayProcessor

| Metod | Təsvir |
|-------|--------|
| `process(arr)` | Hər elementi 2-yə vurur |
| `sum(arr)` | Elementlərin cəmi |
| `average(arr)` | Orta qiymət |
| `min(arr)` | Minimum element |
| `max(arr)` | Maksimum element |

## ⚡ Performans

C++ implementasiyası Python-a nisbətən əhəmiyyətli sürət artımı təmin edir:

| Əməliyyat | Python | C++ | Sürətlənmə |
|-----------|--------|-----|------------|
| Factorial(20) x 100K | ~1.2s | ~0.08s | **15x** |
| Fibonacci(30) x 100K | ~2.5s | ~0.1s | **25x** |
| Array Sum (1M elements) | ~0.05s | ~0.003s | **17x** |

## 🧪 Testlər

```bash
# Bütün Python testlərini işə sal
pytest tests/test_python.py -v

# Performans testləri
pytest tests/test_python.py -v -m performance

# Coverage hesabatı
pytest tests/test_python.py --cov=src/python
```

## 🤝 Töhfə

1. Fork edin
2. Feature branch yaradın (`git checkout -b feature/amazing`)
3. Dəyişiklikləri commit edin (`git commit -m 'Add amazing feature'`)
4. Branch-ı push edin (`git push origin feature/amazing`)
5. Pull Request açın

## 📝 Lisenziya

Bu layihə MIT lisenziyası altında yayımlanır.

## 📚 Resurslar

- [pybind11 Sənədləşdirmə](https://pybind11.readthedocs.io/)
- [CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/)
- [Python C API](https://docs.python.org/3/c-api/)

---

**Müəllif:** Python + C++ İnteqrasiya Komandası  
**Versiya:** 1.0.0  
**Son yenilənmə:** Yanvar 2026
