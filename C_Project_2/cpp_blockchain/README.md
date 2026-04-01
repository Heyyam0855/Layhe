# Bitcoin Tipli Kriptovalyuta Sistemi (C++)

Bu layihə C++ dilində Bitcoin tipli kriptovalyuta sistemidir. Sistem blockchain texnologiyası ilə işləyir.

## 🚀 Xüsusiyyətlər

- ✅ **Blockchain Strukturu**: Blokların zəncirlənməsi və hash mexanizmi
- ✅ **Transaction Sistemi**: Pul göndərmə və qəbul etmə
- ✅ **Proof of Work**: Mining mexanizmi ilə yeni blokların yaradılması
- ✅ **Wallet (Cüzdan)**: Özəl və açıq açarlarla cüzdan sistemi
- ✅ **Balans Yoxlama**: Hər ünvanın balansını izləmə
- ✅ **Etibarlılıq Yoxlama**: Blockchain-in düzgünlüyünü yoxlama

## 📋 Layihə Strukturu

```
cpp_blockchain/
├── Transaction.hpp      # Transaction sinifinin header faylı
├── Transaction.cpp      # Transaction sinifinin implementation faylı
├── Block.hpp           # Block sinifinin header faylı
├── Block.cpp           # Block sinifinin implementation faylı
├── Blockchain.hpp      # Blockchain sinifinin header faylı
├── Blockchain.cpp      # Blockchain sinifinin implementation faylı
├── Wallet.hpp          # Wallet sinifinin header faylı
├── Wallet.cpp          # Wallet sinifinin implementation faylı
├── main.cpp            # Əsas proqram faylı
├── Makefile            # Build faylı
└── README.md           # Bu fayl
```

## 🔄 Python vs C++ - İcra Prosesi

### Python-da (`python main.py`):
```bash
python main.py  # Birbaşa icra olunur
```
- **Python interpreted dildir** - kod birbaşa icra olunur
- Python interpeteri kodu sətir-sətir oxuyur və icra edir
- Kompilyasiya lazım deyil

### C++-da (`main.cpp`):
```bash
# 1. ADIM: Kompilyasiya (Compile)
g++ -std=c++11 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp

# 2. ADIM: İcra (Run)
blockchain.exe
```
- **C++ compiled dildir** - əvvəlcə kompilyasiya lazımdır
- Kompilyator kodu maşın koduna çevirir və `.exe` faylı yaradır
- Sonra `.exe` faylını icra edirsiniz

### Fərq:
| Xüsusiyyət | Python | C++ |
|------------|--------|-----|
| **Tip** | Interpreted | Compiled |
| **Kompilyasiya** | Lazım deyil | Lazımdır |
| **İcra** | Birbaşa | Kompilyasiyadan sonra |
| **Sürət** | Yavaş | Sürətli |
| **Komanda** | `python main.py` | `g++ ... && ./blockchain.exe` |

## 🔧 Quraşdırma və Kompilasiya

### Linux/Mac üçün:

```bash
cd cpp_blockchain
make
./blockchain
```

### Windows üçün (MinGW):

```bash
cd cpp_blockchain
make windows
blockchain.exe
```

Və ya birbaşa:

```bash
g++ -std=c++11 -Wall -Wextra -O2 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp
blockchain.exe
```

## 💻 İstifadə Nümunəsi

```cpp
#include "Blockchain.hpp"
#include "Wallet.hpp"

int main() {
    // Blockchain yarat
    Blockchain blockchain(2);
    
    // Cüzdanlar yarat
    Wallet wallet1(&blockchain);
    Wallet wallet2(&blockchain);
    
    // Mining edərək pul qazan
    blockchain.minePendingTransactions(wallet1.getAddress());
    
    // Pul göndər
    wallet1.sendMoney(wallet2.getAddress(), 25);
    
    // Mining edərək əməliyyatı təsdiqlə
    blockchain.minePendingTransactions(wallet2.getAddress());
    
    // Balansı yoxla
    std::cout << "Balans: " << wallet1.getBalance() << std::endl;
    
    return 0;
}
```

## 🎯 Əsas Komponentlər

### 1. Transaction (Əməliyyat)
- Göndərən və alıcı ünvanlar
- Göndərilən məbləğ
- Vaxt möhürü

### 2. Block (Blok)
- İndeks nömrəsi
- Əməliyyatlar siyahısı
- Əvvəlki blokun hash-i
- Nonce (mining üçün)
- Öz hash-i

### 3. Blockchain
- Bloklar zənciri
- Gözləyən əməliyyatlar
- Mining mükafatı
- Balanslar bazası

### 4. Wallet (Cüzdan)
- Özəl açar
- Açıq açar/ünvan
- Balans yoxlama
- Pul göndərmə

## 🔐 Təhlükəsizlik Qeydləri

⚠️ **Vacib**: Bu sistem təhsil məqsədlidir və real kriptovalyuta kimi istifadə üçün nəzərdə tutulmayıb. Real kriptovalyuta sistemində:

- Daha güclü kriptoqrafiya (SHA-256, ECDSA)
- Network kommunikasiyası
- Konsensus mexanizmləri
- DDoS müdafiəsi
- və s. lazımdır

## 📊 Sistem Arxitekturası

```
Blockchain
├── Genesis Block (İlk Blok)
├── Block 1
│   ├── Transaction 1
│   └── Transaction 2
├── Block 2
│   ├── Transaction 3
│   └── Mining Reward
└── ...
```

## 🧪 Test

Sistemi test etmək üçün:

```bash
make run
```

Və ya Windows-da:

```bash
make windows
blockchain.exe
```

## 📝 Tələblər

- C++11 və ya daha yeni versiya
- GCC və ya MinGW compiler
- Make (Linux/Mac üçün)

## 📝 Əlavə İnkişaf İdeyaları

- [ ] Network funksionallığı (P2P)
- [ ] Merkle Tree implementasiyası
- [ ] Daha mürəkkəb konsensus mexanizmləri
- [ ] Smart Contract dəstəyi
- [ ] REST API
- [ ] Web interfeysi
- [ ] Verilənlər bazası ilə inteqrasiya
- [ ] OpenSSL ilə real SHA-256 hash

## 👨‍💻 Müəllif

Bu layihə təhsil məqsədlidir və blockchain texnologiyasının öyrənilməsi üçün hazırlanmışdır.

## 📄 Lisenziya

Bu kod azad şəkildə istifadə və dəyişdirilə bilər.

