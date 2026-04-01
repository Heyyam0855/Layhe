# CPU Simulyatoru - Python ilə x86 Assembly

🖥️ **x86 CPU arxitekturasının Python-da simulyasiyası**

Bu layihə x86 assembly əmrlərini Python-da simulyasiya edir və CPU-nun daxili işləmə prinsiplərini göstərir.

## 📋 Layihənin Strukturu

```
Telebe_1/
├── cpu_simulator.py      # Əsas CPU simulyator sinfi
├── alu.py               # ALU (Arithmetic Logic Unit) modulu
├── instruction_set.py   # x86 əmr seti tərifləri
├── demo.py             # Demo proqramlar
├── README.md           # Bu fayl
└── cpu_core_demo-asm.md # x86 Assembly referans kodu
```

## 🚀 Başlanğıc

### Tələblər

- Python 3.7 və ya yuxarı versiya
- Heç bir əlavə kitabxana tələb olunmur (Pure Python)

### Quraşdırma

```bash
# Layihəni yüklə
cd Telebe_1

# Birbaşa işə sal (əlavə quraşdırma lazım deyil)
python demo.py
```

## 📚 Modullar

### 1. `cpu_simulator.py` - CPU Simulyatoru

Əsas CPU sinfi - registrlər, bayraqlar və əsas əmrləri idarə edir.

**Xüsusiyyətlər:**
- 32-bit registrlər (EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP)
- CPU bayraqları (CF, ZF, SF, OF)
- 1MB yaddaş simulyasiyası
- Əmr tarixi

**İstifadə nümunəsi:**

```python
from cpu_simulator import CPUSimulator

cpu = CPUSimulator()

# Əməllər
cpu.mov('EAX', 5)        # EAX = 5
cpu.mov('EBX', 3)        # EBX = 3
cpu.add('EAX', 'EBX')    # EAX = EAX + EBX = 8
cpu.shl('EAX', 1)        # EAX = EAX << 1 = 16

# Vəziyyəti göstər
cpu.print_state()
cpu.print_history()

# Nəticə
result = cpu.get_register('EAX')  # 16
```

**Dəstəklənən əmrlər:**
- `MOV` - Məlumat köçür
- `ADD` - Toplama
- `SUB` - Çıxma
- `SHL` / `SHR` - Bit sürüşdürmə
- `AND` / `OR` / `XOR` - Məntiqi əməliyyatlar
- `CMP` - Müqayisə

### 2. `alu.py` - Arithmetic Logic Unit

CPU-nun hesablama və məntiqi bloku.

**Funksiyalar:**
- Arifmetik: `add`, `subtract`, `multiply`, `divide`
- Məntiqi: `bitwise_and`, `bitwise_or`, `bitwise_xor`, `bitwise_not`
- Sürüşdürmə: `shift_left`, `shift_right`, `rotate_left`, `rotate_right`
- Xüsusi: `increment`, `decrement`, `negate`

**İstifadə nümunəsi:**

```python
from alu import ALU

alu = ALU()

# Toplama
result = alu.add(5, 3)  # 8

# Bitwise AND
result = alu.bitwise_and(0b11110000, 0b10101010)  # 0b10100000

# Sola sürüşdürmə
result = alu.shift_left(8, 1)  # 16

# Tam toplayıcı (Full Adder)
sum_bit, carry_out = alu.full_adder(1, 1, 0)
```

### 3. `instruction_set.py` - Əmr Seti

x86 əmr setinin tərifləri və məlumatları.

**Kateqoriyalar:**
- Data Transfer (MOV, PUSH, POP)
- Arithmetic (ADD, SUB, MUL, DIV, INC, DEC)
- Logic (AND, OR, XOR, NOT)
- Shift/Rotate (SHL, SHR, ROL, ROR)
- Control Flow (CMP, JMP, JE, JNE, CALL, RET)

**İstifadə nümunəsi:**

```python
from instruction_set import InstructionSet

iset = InstructionSet()

# Əmr haqqında məlumat
iset.print_instruction_info('ADD')

# Kateqoriya üzrə əmrlər
instructions = iset.list_by_category('Arithmetic')

# Bütün əmrləri göstər
iset.print_all_instructions()
```

### 4. `demo.py` - Demo Proqramlar

Müxtəlif nümunə proqramlar və izahlar.

**Demo rejimləri:**

```bash
# Bütün demolari göstər
python demo.py all

# Əsas əməllər
python demo.py 1

# ALU əməliyyatları
python demo.py 2

# Faktorial proqramı
python demo.py 3

# Əmr seti siyahısı
python demo.py 4

# İkili kod vizuallaşdırma
python demo.py 5
```

## 💡 Nümunə Proqramlar

### Nümunə 1: Sadə Toplama

```python
from cpu_simulator import CPUSimulator

cpu = CPUSimulator()

# Assembly: 
#   MOV EAX, 10
#   MOV EBX, 20
#   ADD EAX, EBX

cpu.mov('EAX', 10)
cpu.mov('EBX', 20)
cpu.add('EAX', 'EBX')

print(f"Nəticə: {cpu.get_register('EAX')}")  # 30
```

### Nümunə 2: Bitwise Əməliyyatlar

```python
from cpu_simulator import CPUSimulator

cpu = CPUSimulator()

# Mask tətbiqi
cpu.mov('EAX', 0b11111111)      # 255
cpu.and_op('EAX', 0b11110000)   # Yalnız yuxarı 4 biti saxla

print(f"Nəticə: {cpu.get_register('EAX'):08b}")  # 11110000
```

### Nümunə 3: Dövr (Loop)

```python
from cpu_simulator import CPUSimulator

cpu = CPUSimulator()

# 1-dən 5-ə qədər topla
cpu.mov('EAX', 0)   # Nəticə
cpu.mov('ECX', 5)   # Counter

while cpu.get_register('ECX') > 0:
    cpu.add('EAX', 'ECX')
    cpu.sub('ECX', 1)

print(f"1+2+3+4+5 = {cpu.get_register('EAX')}")  # 15
```

### Nümunə 4: İkili Sistemdə Əməliyyatlar

```python
from alu import ALU, decimal_to_binary, print_binary_operation

alu = ALU()

# Toplama vizuallaşdırma
a, b = 5, 3
result = alu.add(a, b)
print_binary_operation(a, b, result, "ADD")

# Output:
# ADD əməliyyatı:
#   A:        5 = 00000101
#   B:        3 = 00000011
#   ─────────────────────────────────
#   R:        8 = 00001000
```

## 🔬 CPU İşləmə Prinsipi

CPU əmrləri aşağıdakı mərhələlərdən keçir:

### 1. **FETCH (Gətir)**
```
Yaddaşdan əmri oxu
├─ Program Counter (PC) istifadə edilir
└─ Əmr Instruction Register-ə (IR) yüklənir
```

### 2. **DECODE (Deşifrə et)**
```
Əmri təhlil et
├─ Opcode müəyyənləşdirilir
├─ Operandlar tanınır
└─ Mikro əməllərə (μOps) bölünür
```

### 3. **EXECUTE (İcra et)**
```
Əməli yerinə yetir
├─ ALU hesablamaları
├─ Registr dəyişiklikləri
└─ Bayraq yeniləmələri
```

### 4. **WRITEBACK (Yaz)**
```
Nəticəni saxla
├─ Registrləri yenilə
└─ Yaddaşa yaz (lazım olarsa)
```

## 📊 İkili Kod Təsviri

**Nümunə: MOV EAX, 5**

```
Maşın kodu (HEX):  B8 05 00 00 00

İkili kod (BIN):
┌────────┬────────┬────────┬────────┬────────┐
│10111000│00000101│00000000│00000000│00000000│
├────────┼────────┼────────┼────────┼────────┤
│ OPCODE │ Value=5│    0   │   0    │   0    │
│  MOV   │(little │        │        │        │
│ EAX,imm│endian) │        │        │        │
└────────┴────────┴────────┴────────┴────────┘

Tranzistor səviyyəsi (OPCODE: 10111000):
⚡🚫⚡⚡⚡🚫🚫🚫
```

## 🎯 Məqsəd və Fayda

Bu layihə aşağıdakıları başa düşməyə kömək edir:

1. **CPU Arxitekturası** - Registrlər, ALU, bayraqlar
2. **Assembly Dili** - x86 əmrlərinin işləməsi
3. **İkili Sistem** - Maşın kodunun strukturu
4. **Mikro Arxitektura** - Əmrin daxili mərhələləri
5. **Tranzistor Səviyyəsi** - Fiziki qat anlayışı

## 🛠️ Genişləndirmə İmkanları

Layihəyə əlavə edilə bilər:

- [ ] Yaddaş idarəetməsi (Memory Management)
- [ ] Stack əməliyyatları (PUSH/POP)
- [ ] Funksiya çağırışları (CALL/RET)
- [ ] Interrupt sistemi (INT)
- [ ] Pipeline simulyasiyası
- [ ] Cache simulyasiyası
- [ ] Multi-core dəstəyi

## 📖 Əlavə Mənbələr

- **x86 Assembly Reference**: [cpu_core_demo-asm.md](cpu_core_demo-asm.md)
- **Intel Manuallari**: Intel 64 and IA-32 Architectures Software Developer's Manual
- **Bitwise Əməliyyatlar**: Binary arithmetic və logic operations

## 🤝 Töhfə

Bu tədris layihəsidir. Təkliflər və düzəlişlər xoş qarşılanır.

## 📝 Lisenziya

Bu layihə tədris məqsədlidir və sərbəst istifadə oluna bilər.

---

**Hazırlanma tarixi**: 2026  
**Dil**: Python 3  
**Mövzu**: CPU Simulyasiyası və x86 Assembly

💻 Uğurlar!
