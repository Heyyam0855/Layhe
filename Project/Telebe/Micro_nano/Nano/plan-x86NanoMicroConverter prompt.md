# Plan: x86 Binary → Nano → Micro Çevirmə Sxemi

Bu layihə x86 binary (01) kodunu analiz edərək Nanocode və Microcode formatlarına çevirən bir sistem yaratmağı hədəfləyir. Sxem üç əsas mərhələdən ibarət olacaq: Binary dekoder, Nanocode generator və Microcode generator.

## Əsas Arxitektura Sxemi

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  BINARY (01)    │ ──► │   NANOCODE      │ ──► │   MICROCODE     │
│  x86 Opcodes    │     │  Control Siqnal │     │   µ-əməliyyat   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

**Səviyyə İzahı:**
- **Binary (Maşın Kodu):** CPU-nun oxuduğu ham opcode-lar (0x89, 0xC3 və s.)
- **Nanocode:** Binary-dən birbaşa control siqnalları çıxarılır (ALU_OP, MEM_READ və s.)
- **Microcode (µops):** Control siqnallarından yüksək səviyyəli mikro-əməliyyatlar formalaşır

## Addımlar

1. **Layihə strukturu yaratmaq** - `src/decoder/`, `src/nanocode/`, `src/microcode/` qovluqları ilə modular arxitektura qurmaq
2. **x86 Binary Dekoder hazırlamaq** - Opcode cədvəli, ModR/M və SIB bayt analizatoru ilə binary instruksiyaları parse etmək
3. **Nanocode Generator yazmaq** - Hardware control siqnalları (ALU_OP, REG_SELECT, MEM_READ/WRITE) generasiya edən modul
4. **Microcode Generator əlavə etmək** - Nano control siqnallarından µops (micro-operations) yaratmaq
5. **Test sistemi qurmaq** - Nümunə binary kodlar ilə çevirmə prosesini yoxlamaq

## Nəzərə Alınacaq Məsələlər

1. **Başlanğıc dəsti?** Bütün x86 instruksiyalar (1000+) yoxsa sadə subset (MOV, ADD, PUSH/POP) ilə başlamaq? → **Tövsiyə: Sadə subset ilə başlamaq**
2. **Proqramlaşdırma dili?** C/C++ (performans), Python (sadəlik), yoxsa Assembly? → **Tövsiyə: C dili**
3. **Nanocode formatı?** Bitfield (kompakt) yoxsa struct (oxunaqlı) formatı istifadə etmək?

## Layihə Strukturu

```
Micro_nano/
├── docs/
│   ├── architecture.md        # Sistem dizayn sənədi
│   ├── opcode_reference.md    # x86 opcode xəritələri
│   └── microcode_format.md    # µop spesifikasiyası
├── src/
│   ├── decoder/
│   │   ├── x86_decoder.c      # Binary instruksiya dekoderi
│   │   ├── prefix_parser.c    # x86 prefiksləri idarə et
│   │   └── modrm_sib.c        # Ünvan rejimi dekoderi
│   ├── nanocode/
│   │   ├── control_gen.c      # Control sözləri yarat
│   │   └── signal_defs.h      # Control siqnal tərifləri
│   ├── microcode/
│   │   ├── uop_generator.c    # Mikro-əməliyyatlara çevir
│   │   └── uop_database.c     # Microcode ROM emulyasiyası
│   └── main.c                 # Giriş nöqtəsi
├── data/
│   ├── opcodes.json           # x86 opcode verilənlər bazası
│   └── microcode.json         # µop xəritələmələri
└── tests/
    └── test_cases.bin         # Test binary girişləri
```

## Data Strukturları

```c
// Mərhələ 1: Dekod edilmiş instruksiya
typedef struct {
    uint8_t  prefixes[4];
    uint8_t  opcode[3];
    uint8_t  modrm;
    uint8_t  sib;
    int64_t  displacement;
    int64_t  immediate;
    uint8_t  operand_size;    // 8, 16, 32, 64 bit
    uint8_t  address_size;
    char     mnemonic[16];
} DecodedInstruction;

// Mərhələ 2: Nano Control Word
typedef struct {
    uint32_t alu_op       : 6;
    uint32_t src_a_sel    : 4;
    uint32_t src_b_sel    : 4;
    uint32_t dest_sel     : 4;
    uint32_t mem_read     : 1;
    uint32_t mem_write    : 1;
    uint32_t flags_write  : 1;
    uint32_t branch_cond  : 4;
    uint32_t imm_sel      : 1;
    uint32_t reserved     : 6;
} NanoControlWord;

// Mərhələ 3: Mikro-əməliyyat
typedef struct {
    uint8_t  uop_type;        // ALU, LOAD, STORE, BRANCH
    uint8_t  operation;       // Xüsusi əməliyyat kodu
    uint8_t  src1;            // Mənbə 1 (reg/mem/imm)
    uint8_t  src2;            // Mənbə 2
    uint8_t  dest;            // Hədəf
    uint8_t  flags_affected;  // CF, ZF, SF, OF və s.
} MicroOp;
```

## Nümunə Çevirmə

### Giriş: Binary `0x03 0x45 0x08`

**Mərhələ 1 - Dekod:**
```
Opcode: 0x03 = ADD r32, r/m32
ModR/M: 0x45 = [EBP+disp8], registr EAX
Displacement: 0x08

Nəticə: ADD EAX, [EBP+8]
```

**Mərhələ 2 - Nanocode (Control Siqnalları):**
```
Nano Word 1 (Yaddaş Oxuma):
  ┌─────────────────────────────────────┐
  │ ALU_OP=NOP | SRC_A=EBP | SRC_B=IMM │
  │ MEM_READ=1 | DEST=TMP1 | OFFSET=8  │
  └─────────────────────────────────────┘

Nano Word 2 (ALU Əməliyyatı):
  ┌─────────────────────────────────────┐
  │ ALU_OP=ADD | SRC_A=EAX | SRC_B=TMP1│
  │ MEM_READ=0 | DEST=EAX | FLAGS_WR=1 │
  └─────────────────────────────────────┘
```

**Mərhələ 3 - Microcode (µops):**
```
; Nano siqnallarından generasiya edilmiş µops:
µop1: LOAD  tmp1, [EBP+8]    ; Yaddaş operandını yüklə
µop2: ADD   EAX, EAX, tmp1   ; Toplama əməliyyatı, FLAGS yenilə
```
