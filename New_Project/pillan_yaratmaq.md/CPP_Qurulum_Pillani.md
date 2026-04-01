# C++ Quraşdırma Planı

## 1. Tələb olunan proqramlar

C++ dilində proqramlaşdırma etmək üçün aşağıdakı proqramları quraşdırmalısınız:

- **C++ Kompilyatoru**: Kodunuzu maşın koduna çevirmək üçün
- **IDE və ya Mətn Redaktoru**: Kod yazmaq üçün mühit
- **Debugger**: Kodunuzdakı səhvləri tapmaq və həll etmək üçün

## 2. C++ Kompilyatorunun quraşdırılması

### Windows sistemləri üçün:

#### Variant 1: MinGW (Minimalist GNU for Windows)

1. MinGW-w64 yükləmək üçün [rəsmi sayta](https://sourceforge.net/projects/mingw-w64/) daxil olun
2. İndiki versiyasını yükləyin
3. Quraşdırma zamanı aşağıdakı parametrləri seçin:
   - Version: son versiya (məsələn, 8.1.0)
   - Architecture: x86_64 (64-bit sistem üçün) və ya i686 (32-bit sistem üçün)
   - Threads: posix
   - Exception: seh (64-bit üçün) və ya dwarf (32-bit üçün)
   - Build revision: son versiya (məsələn, 0)
4. Quraşdırıldıqdan sonra sistem dəyişənlərinə `C:\mingw-w64\...\mingw64\bin` kimi yolu əlavə edin (PATH)

#### Variant 2: Visual Studio ilə MSVC

1. [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/) versiyasını yükləyin (pulsuz)
2. Quraşdırma zamanı "Desktop development with C++" modulunu seçin
3. Bu, sizə MSVC (Microsoft Visual C++ Compiler) və digər lazımi alətləri təmin edəcək

### Linux sistemləri üçün:

```bash
sudo apt update
sudo apt install build-essential
```

Bu əmr gcc/g++ kompilyatorları və make kimi lazımi alətləri quraşdıracaq.

### macOS sistemləri üçün:

1. Terminal açın
2. `xcode-select --install` əmrini yerinə yetirin. Bu, Xcode Command Line Tools yükləyəcək.

## 3. IDE və ya Mətn Redaktorunun seçilməsi və quraşdırılması

### Populyar IDE-lər:

#### Visual Studio Code (VS Code)

1. [VS Code](https://code.visualstudio.com/) rəsmi saytından yükləyin
2. Quraşdırıldıqdan sonra aşağıdakı əlavələri quraşdırın:
   - C/C++ (Microsoft tərəfindən)
   - C/C++ IntelliSense
   - C/C++ Themes

#### Visual Studio

- Əgər artıq "Desktop development with C++" ilə Visual Studio quraşdırmısınızsa, əlavə heç nə etməyə ehtiyac yoxdur.

#### CLion

- [CLion](https://www.jetbrains.com/clion/) tələbələr üçün pulsuz versiyası var. Digər hallarda 30 günlük sınaq müddəti təklif edir.

#### Dev-C++

- Sadə və başlanğıc səviyyəli istifadəçilər üçün [Dev-C++](https://sourceforge.net/projects/orwelldevcpp/) yükləyə bilərsiniz.

## 4. İlk C++ Proqramını Yazma və Test Etmə

1. Seçdiyiniz IDE və ya mətn redaktorunu açın
2. Yeni fayl yaradın və `.cpp` uzantısı ilə saxlayın (məsələn, `hello.cpp`)
3. Sadə bir C++ proqramı yazın:

```cpp
#include <iostream>

int main() {
    std::cout << "Salam, C++!" << std::endl;
    return 0;
}
```

4. Proqramı kompilyasiya və icra etmək üçün:

### VS Code ilə:

- Terminal açın (Ctrl+\`)
- Aşağıdakı əmrləri yerinə yetirin:
  ```
  g++ hello.cpp -o hello
  ./hello  # Windows üçün: hello.exe
  ```

### Visual Studio ilə:

- F5 düyməsinə basın və ya Debug > Start Debugging seçin

### CLion ilə:

- Run düyməsinə basın və ya Shift+F10 düyməsini istifadə edin

## 5. C++ Layihə Quruluşu

Böyük layihələr üçün aşağıdakı quruluşdan istifadə edə bilərsiniz:

```
project/
  ├── include/       # Header faylları (.h)
  ├── src/           # Mənbə faylları (.cpp)
  ├── lib/           # Kitabxanalar
  ├── build/         # Kompilyasiya olunmuş fayllar
  ├── docs/          # Sənədlər
  ├── tests/         # Test faylları
  └── CMakeLists.txt # CMake konfiqurasiyası (ixtiyari)
```

## 6. Faydalı Mənbələr

- [C++ Reference](https://en.cppreference.com/) - C++ dilinin ətraflı referansı
- [LearnCpp.com](https://www.learncpp.com/) - C++ öyrənmək üçün pulsuz onlayn dərslər
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) - Yaxşı C++ kodu yazmaq üçün qaydalar
- [Stack Overflow](https://stackoverflow.com/questions/tagged/c%2B%2B) - C++ ilə bağlı suallar və cavablar

## 7. Növbəti Addımlar

- C++ dilinin əsas sintaksis və konsepsiyalarını öyrənin
- Verilənlər strukturları və alqoritmlər ilə işləməyi öyrənin
- Kitabxanaların (məsələn, STL) istifadəsini öyrənin
- Kiçik layihələr üzərində işləyərək təcrübə qazanın

## 8. Ən Yaxşı Təcrübələr

- Kodunuzu mütəmadi olaraq test edin
- Kodunuzu kommentlərlə izah edin
- Səhvləri idarə etmək üçün "try-catch" bloklarından istifadə edin
- Yaddaş sızmalarını önləmək üçün resursları düzgün idarə edin
