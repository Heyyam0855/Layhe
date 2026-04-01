# C++-da Kod İcrası - Ətraflı İzahat

## ❓ Sual: Python-da `python main.py` necə işləyir və C++-da necə yazılır?

### 📘 Python-da (`python main.py`)

Python-da kodun icra olunması çox sadədir:

```bash
python main.py
```

**Nə baş verir:**
1. Python interpeteri `main.py` faylını oxuyur
2. Kodu sətir-sətir analiz edir (parsing)
3. Hər sətiri birbaşa icra edir (execution)
4. Nəticəni ekranda göstərir

**Xüsusiyyətlər:**
- ✅ Kompilyasiya lazım deyil
- ✅ Kod dəyişdikdən sonra birbaşa icra edə bilərsiniz
- ✅ Yavaş ola bilər (runtime-da interpretasiya)

### 🔧 C++-da (`main.cpp`)

C++-da kodun icra olunması 2 addımdan ibarətdir:

#### **Addım 1: Kompilyasiya (Compilation)**

```bash
g++ -std=c++11 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp
```

**Nə baş verir:**
1. Kompilyator (`g++`) bütün `.cpp` fayllarını oxuyur
2. Kodu maşın koduna çevirir (machine code)
3. İcra olunan fayl yaradır (`blockchain.exe`)
4. Əgər xəta varsa, xəta mesajı göstərir

**Komanda parametrləri:**
- `-std=c++11` - C++11 standartını istifadə et
- `-o blockchain.exe` - Çıxış faylının adı
- `-Wall -Wextra` - Bütün xəbərdarlıqları göstər
- `-O2` - Optimallaşdırma səviyyəsi

#### **Addım 2: İcra (Execution)**

```bash
blockchain.exe
```

**Nə baş verir:**
1. Sistem `blockchain.exe` faylını tapır
2. Maşın kodunu birbaşa icra edir
3. Nəticəni ekranda göstərir

**Xüsusiyyətlər:**
- ⚠️ Kompilyasiya lazımdır
- ✅ Kod dəyişdikdən sonra yenidən kompilyasiya etmək lazımdır
- ✅ Çox sürətlidir (maşın kodu birbaşa icra olunur)

## 📊 Müqayisə Cədvəli

| Aspekt | Python | C++ |
|--------|--------|-----|
| **Dil Tipi** | Interpreted | Compiled |
| **Kompilyasiya** | ❌ Lazım deyil | ✅ Lazımdır |
| **İcra Komandası** | `python main.py` | `g++ ... && ./blockchain.exe` |
| **İcra Sürəti** | Yavaş | Çox sürətli |
| **Dəyişiklik Sonrası** | Birbaşa icra | Yenidən kompilyasiya |
| **Debugging** | Asan | Mürəkkəb |
| **Platform Müstəqilliyi** | ✅ Yüksək | ⚠️ Aşağı |

## 🚀 Praktiki Nümunələr

### Python-da:
```bash
# Kod dəyişdirin
# Sonra birbaşa icra edin
python main.py
```

### C++-da:

#### **Yol 1: Əl ilə kompilyasiya**
```bash
# 1. Kompilyasiya
g++ -std=c++11 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp

# 2. İcra
blockchain.exe
```

#### **Yol 2: Makefile istifadə edərək**
```bash
# Windows-da
make windows
blockchain.exe

# Linux/Mac-də
make
./blockchain
```

#### **Yol 3: Batch script ilə (Windows)**
```bash
# run.bat faylını icra edin
run.bat
```

Bu script avtomatik olaraq kompilyasiya edir və icra edir.

## 🎯 Nə Vaxt Hansı Dil?

### Python istifadə edin:
- ✅ Tez prototipləşdirmə
- ✅ Kiçik proyektlər
- ✅ Script yazma
- ✅ Data analizi
- ✅ Web development

### C++ istifadə edin:
- ✅ Sürət vacibdir
- ✅ Sistem proqramlaşdırma
- ✅ Oyun inkişafı
- ✅ Embedded sistemlər
- ✅ Yüksək performans tələb olunan proqramlar

## 💡 Üstünlüklər və Mənfi Cəhətlər

### Python:
**Üstünlüklər:**
- ✅ Kompilyasiya lazım deyil
- ✅ Kod yazmaq asandır
- ✅ Geniş kitabxana dəstəyi
- ✅ Platform müstəqil

**Mənfi cəhətlər:**
- ❌ Yavaş ola bilər
- ❌ Dependencies lazımdır

### C++:
**Üstünlüklər:**
- ✅ Çox sürətli
- ✅ Sistemə yaxın
- ✅ Tam nəzarət

**Mənfi cəhətlər:**
- ❌ Kompilyasiya lazımdır
- ❌ Kod yazmaq mürəkkəbdir
- ❌ Platform müstəqil deyil

## 📝 Nəticə

- **Python**: `python main.py` → Birbaşa icra
- **C++**: `g++ ... && ./blockchain.exe` → Kompilyasiya + İcra

C++-da kod dəyişdikdən sonra həmişə yenidən kompilyasiya etmək lazımdır!

