# Bitcoin Tipli Kriptovalyuta Sistemi

Bu layihə Python dilində sadələşdirilmiş Bitcoin tipli kriptovalyuta sistemidir. Sistem blockchain texnologiyası ilə işləyir və aşağıdakı funksionallıqları dəstəkləyir:

## 🚀 Xüsusiyyətlər

- ✅ **Blockchain Strukturu**: Blokların zəncirlənməsi və hash mexanizmi
- ✅ **Transaction Sistemi**: Pul göndərmə və qəbul etmə
- ✅ **Proof of Work**: Mining mexanizmi ilə yeni blokların yaradılması
- ✅ **Wallet (Cüzdan)**: Özəl və açıq açarlarla cüzdan sistemi
- ✅ **Balans Yoxlama**: Hər ünvanın balansını izləmə
- ✅ **Etibarlılıq Yoxlama**: Blockchain-in düzgünlüyünü yoxlama

## 📋 Sistem Komponentləri

### 1. **Transaction (Əməliyyat)**
- Göndərən və alıcı ünvanlar
- Göndərilən məbləğ
- Vaxt möhürü

### 2. **Block (Blok)**
- İndeks nömrəsi
- Əməliyyatlar siyahısı
- Əvvəlki blokun hash-i
- Nonce (mining üçün)
- Öz hash-i

### 3. **Blockchain**
- Bloklar zənciri
- Gözləyən əməliyyatlar
- Mining mükafatı
- Balanslar bazası

### 4. **Wallet (Cüzdan)**
- Özəl açar
- Açıq açar/ünvan
- Balans yoxlama
- Pul göndərmə

## 🔧 Quraşdırma

1. Python 3.7 və ya daha yeni versiya lazımdır
2. Bütün paketlər Python standart kitabxanasındandır, əlavə quraşdırma lazım deyil

```bash
python main.py
```

## 💻 İstifadə Nümunəsi

```python
from main import Blockchain, Wallet

# Blockchain yarat
blockchain = Blockchain(difficulty=2)

# Cüzdanlar yarat
wallet1 = Wallet(blockchain)
wallet2 = Wallet(blockchain)

# Mining edərək pul qazan
blockchain.mine_pending_transactions(wallet1.get_address())

# Pul göndər
wallet1.send_money(wallet2.get_address(), 25)

# Mining edərək əməliyyatı təsdiqlə
blockchain.mine_pending_transactions(wallet2.get_address())

# Balansı yoxla
print(f"Balans: {wallet1.get_balance()}")
```

## 🎯 Əsas Addımlar

### Addım 1: Blockchain Yaratmaq
```python
blockchain = Blockchain(difficulty=2)
```

### Addım 2: Cüzdan Yaratmaq
```python
wallet = Wallet(blockchain)
address = wallet.get_address()
```

### Addım 3: Mining (Mükafat qazanmaq)
```python
blockchain.mine_pending_transactions(wallet.get_address())
```

### Addım 4: Pul Göndərmək
```python
wallet.send_money(receiver_address, amount)
```

### Addım 5: Əməliyyatları Təsdiqləmək
```python
blockchain.mine_pending_transactions(miner_address)
```

## 🔐 Təhlükəsizlik Qeydləri

⚠️ **Vacib**: Bu sistem təhsil məqsədlidir və real kriptovalyuta kimi istifadə üçün nəzərdə tutulmayıb. Real kriptovalyuta sistemində:

- Daha güclü kriptoqrafiya
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
python main.py
```

Bu əmr bütün funksionallığı nümayiş etdirəcək və blockchain-i göstərəcək.

## 📝 Əlavə İnkişaf İdeyaları

- [ ] Network funksionallığı (P2P)
- [ ] Merkle Tree implementasiyası
- [ ] Daha mürəkkəb konsensus mexanizmləri
- [ ] Smart Contract dəstəyi
- [ ] REST API
- [ ] Web interfeysi
- [ ] Verilənlər bazası ilə inteqrasiya

## 👨‍💻 Müəllif

Bu layihə təhsil məqsədlidir və blockchain texnologiyasının öyrənilməsi üçün hazırlanmışdır.

## 📄 Lisenziya

Bu kod azad şəkildə istifadə və dəyişdirilə bilər.

