# C++ Kitabxanalar və Alətlər Siyahısı

## Əsas İnkişaf Alətləri

### 1. MinGW-w64 və MSYS2 Quraşdırılması
```bash
# MSYS2 rəsmi saytından yükləyin: https://www.msys2.org/

# MSYS2 terminal açdıqdan sonra:
pacman -Syu                    # Sistem yeniləməsi
pacman -S mingw-w64-x86_64-gcc # GCC kompaylər
pacman -S mingw-w64-x86_64-gdb # Debugger
pacman -S mingw-w64-x86_64-cmake # CMake build sistemi
pacman -S mingw-w64-x86_64-make  # Make utility
```

### 2. Əsas Development Tools
```bash
pacman -S git                           # Versiya idarəetməsi
pacman -S mingw-w64-x86_64-pkg-config # Paket konfiqurasiyası
pacman -S mingw-w64-x86_64-ninja      # Build sistemi
pacman -S mingw-w64-x86_64-doxygen    # Dokumentasiya
```

## C++ Standart Kitabxanalar (Built-in)

### STL (Standard Template Library)
- **Containers**: `std::vector`, `std::map`, `std::set`, `std::unordered_map`
- **Algorithms**: `std::sort`, `std::find`, `std::transform`
- **Iterators**: Input, output, forward, bidirectional iterators
- **Smart Pointers**: `std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`
- **Threading**: `std::thread`, `std::mutex`, `std::future`
- **Filesystem**: `std::filesystem` (C++17)

### Input/Output
- **iostreams**: `std::cin`, `std::cout`, `std::ifstream`, `std::ofstream`
- **String streams**: `std::stringstream`, `std::istringstream`

## Xarici Kitabxanalar

### 1. JSON İşləmə
```bash
# nlohmann/json - Modern JSON kitabxanası
pacman -S mingw-w64-x86_64-nlohmann-json

# Kod nümunəsi:
#include <nlohmann/json.hpp>
using json = nlohmann::json;
```

### 2. HTTP Client/Server
```bash
# cURL - HTTP sorğuları üçün
pacman -S mingw-w64-x86_64-curl

# cpp-httplib - Sadə HTTP server/client
# Header-only library - manual yükləmə lazımdır
```

### 3. Database
```bash
# SQLite - Kiçik database
pacman -S mingw-w64-x86_64-sqlite3

# PostgreSQL client
pacman -S mingw-w64-x86_64-postgresql
```

### 4. Testing Framework
```bash
# Google Test - Unit testing
pacman -S mingw-w64-x86_64-gtest

# Catch2 - Sadə testing framework
pacman -S mingw-w64-x86_64-catch
```

### 5. Logging
```bash
# spdlog - Sürətli logging kitabxanası
pacman -S mingw-w64-x86_64-spdlog

# Kod nümunəsi:
#include <spdlog/spdlog.h>
spdlog::info("Hello World!");
```

### 6. Command Line Parsing
```bash
# CLI11 - Modern command line parser
# Header-only, manual yükləmə

# Boost Program Options
pacman -S mingw-w64-x86_64-boost
```

### 7. GUI Development (İsteğe bağlı)
```bash
# Qt5/Qt6 - Cross-platform GUI
pacman -S mingw-w64-x86_64-qt5-base
pacman -S mingw-w64-x86_64-qt6-base

# wxWidgets - Native look GUI
pacman -S mingw-w64-x86_64-wxwidgets3.2
```

### 8. Graphics və Game Development
```bash
# OpenGL
pacman -S mingw-w64-x86_64-freeglut
pacman -S mingw-w64-x86_64-glfw

# SDL2 - Media və Game development
pacman -S mingw-w64-x86_64-SDL2
```

### 9. Kriptoqrafiya və Təhlükəsizlik
```bash
# OpenSSL - Kriptoqrafik funksiyalar
pacman -S mingw-w64-x86_64-openssl

# Crypto++ - C++ crypto library
pacman -S mingw-w64-x86_64-crypto++
```

### 10. Data Processing
```bash
# Eigen - Linear algebra kitabxanası
pacman -S mingw-w64-x86_64-eigen3

# OpenCV - Computer vision (böyük kitabxana)
pacman -S mingw-w64-x86_64-opencv
```

## Header-Only Kitabxanalar (Manual Install)

### 1. fmt - String formatting
```cpp
// GitHub: https://github.com/fmtlib/fmt
#include <fmt/core.h>
fmt::print("Hello, {}!", "world");
```

### 2. CLI11 - Command line parser
```cpp
// GitHub: https://github.com/CLIUtils/CLI11
#include <CLI/CLI.hpp>
```

### 3. cpp-httplib - HTTP server/client
```cpp
// GitHub: https://github.com/yhirose/cpp-httplib
#include <httplib.h>
```

### 4. json.hpp - JSON parser
```cpp
// GitHub: https://github.com/nlohmann/json
#include <nlohmann/json.hpp>
```

## CMakeLists.txt Nümunəsi

```cmake
cmake_minimum_required(VERSION 3.15)
project(MyProject VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Pakləri tap
find_package(PkgConfig REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(spdlog REQUIRED)

# Executable yarat
add_executable(${PROJECT_NAME} 
    src/main.cpp
    src/core/Application.cpp
)

# Include directory-lər
target_include_directories(${PROJECT_NAME} PRIVATE include)

# Kitabxanaları link et
target_link_libraries(${PROJECT_NAME} 
    PRIVATE 
    nlohmann_json::nlohmann_json
    spdlog::spdlog
)

# Compiler flags
if(MSVC)
    target_compile_options(${PROJECT_NAME} PRIVATE /W4)
else()
    target_compile_options(${PROJECT_NAME} PRIVATE -Wall -Wextra -Wpedantic)
endif()
```

## Environment Setup Skripti

```bash
#!/bin/bash
# setup_environment.sh

echo "C++ Development Environment Setup"

# MSYS2 paketlərini yeniləyin
pacman -Syu --noconfirm

# Əsas development tools
pacman -S --noconfirm \
    mingw-w64-x86_64-gcc \
    mingw-w64-x86_64-gdb \
    mingw-w64-x86_64-cmake \
    mingw-w64-x86_64-make \
    mingw-w64-x86_64-ninja \
    git

# C++ kitabxanalar
pacman -S --noconfirm \
    mingw-w64-x86_64-nlohmann-json \
    mingw-w64-x86_64-spdlog \
    mingw-w64-x86_64-gtest \
    mingw-w64-x86_64-sqlite3 \
    mingw-w64-x86_64-curl \
    mingw-w64-x86_64-boost

echo "Setup completed successfully!"
echo "Add to PATH: C:\msys64\mingw64\bin"
```

## İstifadə Tövsiyələri

### 1. Development Workflow
1. MSYS2 MINGW64 terminal istifadə edin
2. CMake ilə build sistemi quraşdırın
3. Git ilə versiya idarəetməsi aparın
4. Unit testlər yazın

### 2. Performance Tips
- `-O2` və ya `-O3` optimization flags istifadə edin
- Profile-guided optimization (PGO) tətbiq edin
- Memory leaks üçün Valgrind (Linux) və ya Dr. Memory istifadə edin

### 3. Debugging
- GDB debugger istifadə edin
- AddressSanitizer və ThreadSanitizer aktivləşdirin
- Static analysis tools istifadə edin (cppcheck, clang-tidy)

Bu siyahı sizin C++ layihənizi uğurla həyata keçirməyiniz üçün lazımi olan bütün əsas kitabxana və alətləri əhatə edir.