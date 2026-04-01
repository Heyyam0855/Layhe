# Python və C++ inteqrasiyası üçün tövsiyələr

## Python və C++ arasında əlaqə üsulları

### A) Pybind11 (tövsiyə olunur)

- C++ funksiyalarını Python-dan çağırmaq üçün
- GCC lazım deyil, Clang ilə işləyir
- Sadə və performanslı

```cpp
// example.cpp
#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(example, m) {
    m.def("add", &add, "A function that adds two numbers");
}
```

Kompilyasiya:

```bash
clang++ -O3 -shared -std=c++17 -fPIC `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`
```

### B) Python C API

- Python-un daxili C API-si
- Daha çox kontrol, lakin daha mürəkkəb

### C) ctypes (Python tərəfindən)

- Python-dan C++ shared library-ləri çağırmaq
- GCC lazım deyil, yalnız compiled library lazımdır

```python
# Python tərəfindən
import ctypes

# C++ library-ni yüklə
lib = ctypes.CDLL('./libexample.so')  # Linux
# lib = ctypes.CDLL('./example.dll')  # Windows

# Funksiyanı çağır
result = lib.add(5, 3)
```

## Layihənizdə Python inteqrasiyası

### Tövsiyə olunan struktur:

```
pıllan-compiler/
├── src/
│   ├── cpp/
│   │   ├── compiler_core.cpp    # C++ core funksiyaları
│   │   └── encryption.cpp
│   └── python/
│       ├── python_bindings.cpp   # Pybind11 bindings
│       └── python_wrapper.py    # Python wrapper
├── python/
│   ├── pıllan/
│   │   ├── __init__.py
│   │   ├── compiler.py          # Python API
│   │   └── keywords.py          # 35 keywords
│   └── functions.py             # 70 functions
└── CMakeLists.txt
```

## Python keywords və functions inteqrasiyası

### Python keywords (35) və functions (70) üçün nümunə:

```cpp
// python_bindings.cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "compiler_core.h"

namespace py = pybind11;

PYBIND11_MODULE(pıllan_compiler, m) {
    m.doc() = "Pıllan Compiler - Python bindings";
    
    // Keywords modulu
    py::module keywords = m.def_submodule("keywords");
    keywords.def("is_keyword", &is_keyword, "Check if word is keyword");
    keywords.def("get_all_keywords", &get_all_keywords, "Get all 35 keywords");
    
    // Functions modulu
    py::module functions = m.def_submodule("functions");
    functions.def("encrypt_32bit", &encrypt_32bit, "32-bit encryption");
    functions.def("encrypt_16bit", &encrypt_16bit, "16-bit encryption");
    // ... digər 70 funksiya
}
```

## CMake konfiqurasiyası

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.15)
project(pıllan_compiler)

set(CMAKE_CXX_STANDARD 17)

# Python tapmaq
find_package(pybind11 REQUIRED)

# C++ core library
add_library(compiler_core STATIC
    src/cpp/compiler_core.cpp
    src/cpp/encryption.cpp
)

# Python bindings
pybind11_add_module(pıllan_compiler 
    src/python/python_bindings.cpp
)

target_link_libraries(pıllan_compiler PRIVATE compiler_core)
```

## Python-dan istifadə nümunəsi

```python
# Python kodunda
import pıllan_compiler

# Keywords işlətmə
keywords = pıllan_compiler.keywords.get_all_keywords()
print(f"Total keywords: {len(keywords)}")  # 35

# Functions işlətmə
data = [0x12345678, 0xABCDEF00]
key = 0xCAFEBABE

# C++ funksiyasını Python-dan çağır
encrypted = pıllan_compiler.functions.encrypt_32bit(data, key)
```

## GCC olmadan işləmə

- Python interpretasiya olunur, kompilyasiya lazım deyil
- C++ hissəsi üçün Clang istifadə edin (GCC alternativi)
- Windows-da MSVC də istifadə oluna bilər

```bash
# Clang ilə kompilyasiya (GCC olmadan)
clang++ -m32 -O2 -shared -fPIC python_bindings.cpp -o pıllan_compiler.so
```

## Tövsiyə olunan addımlar

1. Pybind11 quraşdırın:
   ```bash
   pip install pybind11
   ```

2. C++ core funksiyalarınızı hazırlayın

3. Python bindings yaradın (Pybind11 ilə)

4. Test edin:
   ```python
   python -c "import pıllan_compiler; print('Success!')"
   ```

## Performans üstünlükləri

- Kritik hissələr C++-da (sürət)
- Yüksək səviyyəli məntiq Python-da (rahatlıq)
- Python-dan C++ funksiyalarını çağırmaq (hibrid)

## Əlavə məlumat

- Pybind11 dokumentasiyası: https://pybind11.readthedocs.io/
- Python C API: https://docs.python.org/3/c-api/
- Clang dokumentasiyası: https://clang.llvm.org/docs/

Bu yanaşma ilə Python-dan C++ funksiyalarınızı istifadə edə bilərsiniz, GCC lazım deyil, Clang kifayətdir.

