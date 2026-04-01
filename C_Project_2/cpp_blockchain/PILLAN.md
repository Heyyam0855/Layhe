# 📖 Blockchain Layihəsi - Quraşdırma və İstifadə Təlimatları

Bu sənəd blockchain layihəsinin quraşdırılması və istifadəsi üçün addım-addım təlimatları ehtiva edir.

---

## 📋 Məzmun

1. [Sistem Tələbləri](#sistem-tələbləri)
2. [Layihə Strukturu](#layihə-strukturu)
3. [Quraşdırma Addımları](#quraşdırma-addımları)
4. [Kompilasiya](#kompilasiya)
5. [Proqramı İşə Salma](#proqramı-işə-salma)
6. [Kod Dəyişiklikləri](#kod-dəyişiklikləri)
7. [Problemlərin Həlli](#problemlərin-həlli)

---

## 🔧 Sistem Tələbləri

### Windows üçün:
- ✅ **MinGW** və ya **MSYS2** (GCC compiler)
- ✅ **Git Bash** və ya **PowerShell** (terminal)
- ✅ **Make** (optional, amma tövsiyə olunur)

### Linux üçün:
- ✅ **GCC** compiler (g++)
- ✅ **Make** utiliti
- ✅ **Bash** terminal

### Mac üçün:
- ✅ **Xcode Command Line Tools**
- ✅ **Make** utiliti
- ✅ **Terminal**

---

## 📁 Layihə Strukturu

Layihə aşağıdakı fayllardan ibarətdir:

```
cpp_blockchain/
├── Block.hpp           # Block sinifi header
├── Block.cpp           # Block sinifi implementasiyası
├── Blockchain.hpp      # Blockchain sinifi header
├── Blockchain.cpp      # Blockchain sinifi implementasiyası
├── Transaction.hpp     # Transaction sinifi header
├── Transaction.cpp     # Transaction sinifi implementasiyası
├── Wallet.hpp          # Wallet sinifi header
├── Wallet.cpp          # Wallet sinifi implementasiyası
├── main.cpp            # Əsas proqram faylı
├── Makefile            # Build konfiqurasiyası
├── README.md           # Layihə haqqında məlumat
└── PILLAN.md           # Bu təlimat faylı
```

---

## 🚀 Quraşdırma Addımları

### Addım 1: Layihəni Yükləyin

Əgər layihə Git repository-dən götürülürsə:

```bash
git clone <repository-url>
cd C_procekt/cpp_blockchain
```

Və ya faylları birbaşa kopyalayın və `cpp_blockchain` qovluğuna yerləşdirin.

### Addım 2: Compiler Quraşdırmasını Yoxlayın

**Windows üçün:**
```bash
g++ --version
```

Əgər xəta alırsınızsa, MinGW quraşdırın:
- [MinGW-w64](https://www.mingw-w64.org/downloads/) saytından yükləyin
- Sistem PATH-də `g++.exe` yolunu əlavə edin

**Linux üçün:**
```bash
g++ --version
```

Əgər quraşdırılmamışdırsa:
```bash
sudo apt-get update
sudo apt-get install g++ make
```

**Mac üçün:**
```bash
g++ --version
```

Əgər quraşdırılmamışdırsa:
```bash
xcode-select --install
```

### Addım 3: Make Faylını Yoxlayın

`Makefile` faylının mövcud olduğunu və düzgün formatda olduğunu yoxlayın:

```bash
ls -la Makefile
```

---

## ⚙️ Kompilasiya

### Windows üçün - Metod 1: Makefile istifadə edərək

```bash
cd cpp_blockchain
make windows
```

Bu komanda `blockchain.exe` faylını yaradacaq.

### Windows üçün - Metod 2: Birbaşa kompilyasiya

```bash
cd cpp_blockchain
g++ -std=c++11 -Wall -Wextra -O2 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp
```

### Linux/Mac üçün - Metod 1: Makefile istifadə edərək

```bash
cd cpp_blockchain
make
```

Bu komanda `blockchain` executable faylını yaradacaq.

### Linux/Mac üçün - Metod 2: Birbaşa kompilyasiya

```bash
cd cpp_blockchain
g++ -std=c++11 -Wall -Wextra -O2 -o blockchain main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp
```

### Kompilyasiya Parametrləri İzahı:

- `-std=c++11`: C++11 standartını istifadə et
- `-Wall`: Bütün xəbərdarlıqları göstər
- `-Wextra`: Əlavə xəbərdarlıqlar
- `-O2`: Optimizasiya səviyyəsi 2
- `-o blockchain`: Çıxış faylının adı

---

## ▶️ Proqramı İşə Salma

### Windows üçün:

```bash
blockchain.exe
```

Və ya:

```bash
./blockchain.exe
```

### Linux/Mac üçün:

```bash
./blockchain
```

Və ya Makefile ilə:

```bash
make run
```

### Gözlənilən Nəticə:

Proqram işə düşdükdə aşağıdakı kimi nəticə görəcəksiniz:

```
============================================================
BITCOIN TİPLİ KRİPTOVALYUTA SİSTEMİ (C++)
============================================================

Cüzdan 1 ünvanı: [hexadecimal ünvan]
Cüzdan 2 ünvanı: [hexadecimal ünvan]
Cüzdan 3 ünvanı: [hexadecimal ünvan]

============================================================
MİNİNG BAŞLAYIR...
============================================================
Block mined: [hash]
Cüzdan 1 balansı: 50
Block mined: [hash]
Cüzdan 2 balansı: 50

============================================================
ƏMƏLİYYATLAR
============================================================
25 coin [ünvan] ünvanına göndərildi
15 coin [ünvan] ünvanına göndərildi
Block mined: [hash]

============================================================
BALANSLAR
============================================================
Cüzdan 1 balansı: 25
Cüzdan 2 balansı: 60
Cüzdan 3 balansı: 65

============================================================
BLOCKCHAIN
============================================================

==================================================
Block #0
Hash: [hash]
Previous Hash: 0
Timestamp: [tarix]
Nonce: 0
Transactions:
  - Transaction(Genesis -> Genesis: 0.00)
==================================================

[digər bloklar...]

============================================================
BLOCKCHAIN ETİBARLILIĞI
============================================================
Blockchain düzgündür: Bəli
```

---

## 🔨 Kod Dəyişiklikləri

### Mining çətinliyini dəyişdirmək:

`main.cpp` faylında:

```cpp
// Cari:
Blockchain blockchain(2);

// Dəyişdirmək:
Blockchain blockchain(3);  // Daha çətin
Blockchain blockchain(1);  // Daha asan
```

### Mining mükafatını dəyişdirmək:

`Blockchain.cpp` faylında constructor-da:

```cpp
// Cari:
Blockchain::Blockchain(int difficulty) 
    : difficulty(difficulty), miningReward(50.0) {
```

```cpp
// Dəyişdirmək:
Blockchain::Blockchain(int difficulty) 
    : difficulty(difficulty), miningReward(100.0) {
```

### Yeni əməliyyatlar əlavə etmək:

`main.cpp` faylında:

```cpp
// Yeni cüzdan yarat
Wallet wallet4(&blockchain);

// Pul göndər
wallet1.sendMoney(wallet4.getAddress(), 10);

// Mining et
blockchain.minePendingTransactions(wallet4.getAddress());
```

---

## 🧹 Təmizləmə

### Kompilyasiya fayllarını silmək:

**Windows üçün:**
```bash
del *.o blockchain.exe
```

**Linux/Mac üçün:**
```bash
make clean
```

Və ya:

```bash
rm -f *.o blockchain
```

---

## ❗ Problemlərin Həlli

### Problem 1: `g++: command not found`

**Həll:**
- Windows: MinGW quraşdırın və PATH-ə əlavə edin
- Linux: `sudo apt-get install g++`
- Mac: `xcode-select --install`

### Problem 2: `make: command not found`

**Həll:**
- Windows: Makefile-dan istifadə etməyin, birbaşa kompilyasiya edin
- Linux: `sudo apt-get install make`
- Mac: Xcode Command Line Tools quraşdırın

### Problem 3: Linking xətası

**Həll:**
Bütün `.cpp` fayllarının kompilyasiya siyahısında olduğunu yoxlayın:

```bash
g++ -std=c++11 -o blockchain main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp
```

### Problem 4: `std::hash` xətası

**Həll:**
`#include <functional>` header-ının əlavə edildiyini yoxlayın (fayllarda artıq var).

### Problem 5: Windows-da `make` işləmir

**Həll:**
Birbaşa kompilyasiya komandasını istifadə edin:

```bash
g++ -std=c++11 -Wall -Wextra -O2 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp
```

### Problem 6: Mining çox uzun çəkir

**Həll:**
Difficulty-ni azaldın:

```cpp
Blockchain blockchain(1);  // 2 yerinə 1
```

### Problem 7: Balans düzgün hesablanmır

**Həll:**
- Mining-dən sonra balansları yoxlayın
- Sistem ünvanından ("System") göndərilən əməliyyatları yoxlayın
- `minePendingTransactions` funksiyasının çağırıldığını yoxlayın

---

## 📊 Test Ssenariləri

### Test 1: Əsas Funksionallıq

```cpp
Blockchain blockchain(2);
Wallet wallet1(&blockchain);
Wallet wallet2(&blockchain);

// Mining
blockchain.minePendingTransactions(wallet1.getAddress());
std::cout << "Balans: " << wallet1.getBalance() << std::endl;  // 50 olmalıdır

// Pul göndər
wallet1.sendMoney(wallet2.getAddress(), 25);
blockchain.minePendingTransactions(wallet2.getAddress());

// Balansları yoxla
std::cout << "Wallet1: " << wallet1.getBalance() << std::endl;  // 25 olmalıdır
std::cout << "Wallet2: " << wallet2.getBalance() << std::endl;  // 75 olmalıdır
```

### Test 2: Blockchain Etibarlılığı

```cpp
std::cout << "Blockchain düzgündür: " 
          << (blockchain.isChainValid() ? "Bəli" : "Xeyr") << std::endl;
```

### Test 3: Yetersiz Balans

```cpp
try {
    wallet1.sendMoney(wallet2.getAddress(), 1000);  // Çox pul
} catch (const std::runtime_error& e) {
    std::cout << "Xəta: " << e.what() << std::endl;
}
```

---

## 📚 Əlavə Resurslar

- **C++11 Standartı**: [cppreference.com](https://en.cppreference.com/w/cpp/11)
- **Blockchain Texnologiyası**: [Blockchain 101](https://www.investopedia.com/terms/b/blockchain.asp)
- **Git**: [Git Sənədləşməsi](https://git-scm.com/doc)

---

## ✅ Yoxlama Siyahısı

Layihəni uğurla quraşdırmaq üçün:

- [ ] Compiler quraşdırılmışdır (`g++ --version`)
- [ ] Bütün fayllar mövcuddur
- [ ] Kompilyasiya uğurla tamamlanıb
- [ ] Proqram işə düşür və nəticə göstərir
- [ ] Blockchain etibarlılıq testi keçir
- [ ] Balanslar düzgün hesablanır

---

## 💡 Məsləhətlər

1. **İlk dəfə kompilyasiya zamanı** `-Wall -Wextra` parametrlərini istifadə edin - xəbərdarlıqları görəcəksiniz
2. **Debugging üçün** `-g` parametrini əlavə edin: `g++ -std=c++11 -g ...`
3. **Performans üçün** `-O2` və ya `-O3` optimizasiyasını istifadə edin
4. **Kod dəyişiklikləri** sonra mutləq yenidən kompilyasiya edin
5. **Git istifadə edin** kod versiyalarını izləmək üçün

---

## 📞 Dəstək

Əgər problemləriniz varsa:

1. Yuxarıdakı "Problemlərin Həlli" bölməsinə baxın
2. Kompilyasiya xəta mesajlarını yoxlayın
3. Bütün faylların mövcud olduğunu təsdiqləyin
4. Compiler versiyasını yoxlayın (`g++ --version`)

---

**Son yeniləmə:** 2024  
**Versiya:** 1.0

