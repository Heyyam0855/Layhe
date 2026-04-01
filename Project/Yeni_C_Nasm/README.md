# NASM və C İlə Aşağı Səviyyəli Proqramlaşdırma

Bu layihə Assembly (NASM) və C/C++ ilə sistem səviyyəli proqramlaşdırma üçün tədris materiallarını ehtiva edir.

---

## 📋 Mündəricat

1. [Layihə Haqqında](#layihə-haqqında)
2. [Quraşdırma və Alətlər](#quraşdırma-və-alətlər)
3. [NASM və GCC İstifadəsi](#nasm-və-gcc-istifadəsi)
4. [Terminal → Kernel → Disk → RAM → CPU Zənciri](#terminal--kernel--disk--ram--cpu-zənciri)
5. [Praktik Nümunələr](#praktik-nümunələr)
6. [GitHub-a Yükləmə](#githuba-yükləmə)
7. [Tövsiyə Olunan Mənbələr](#tövsiyə-olunan-mənbələr)

---

## Layihə Haqqında

Bu layihə kernel inkişafı və aşağı səviyyəli proqramlaşdırma üçün nəzərdə tutulub. Qarışıq toolchain istifadə edirik:

```
C/C++ → GCC → AT&T/GAS Assembly
         +
NASM → Intel Assembly (boot, low-level)
```

---

## Quraşdırma və Alətlər

### Windows üçün Lazımlı Alətlər

| Alət | Quraşdırma | Təyinatı |
|------|------------|----------|
| **NASM** | https://nasm.us | Assembly compiler |
| **GCC** | MinGW/MSYS2 | C/C++ compiler |
| **QEMU** | `winget install QEMU` | Virtual maşın (test) |

#### PowerShell ilə quraşdırma:

```powershell
# MinGW/GCC
winget install -e --id mingw-w64

# NASM
winget install -e --id NASM.NASM

# QEMU (test üçün)
winget install -e --id SoftwareFreedomConservancy.QEMU
```

### VS Code Uzantıları

Assembly inkişafı üçün tövsiyə olunan uzantılar:

- **rights.nas-vscode** - NASM syntax highlighting
- **13xforever.language-x86-64-assembly** - x86-64 Assembly dəstəyi
- **kratosgado.nasm-compiler-linux** - NASM compiler inteqrasiyası

---

## NASM və GCC İstifadəsi

### Tipik Kernel Layihə Strukturu

```makefile
CC = gcc
AS = nasm
LD = ld

CFLAGS = -m32 -ffreestanding -fno-pie -nostdlib
ASFLAGS = -f elf32
LDFLAGS = -m elf_i386 -T linker.ld

# C faylları assembly-ə çevirmək
%.s: %.c
	$(CC) $(CFLAGS) -S $< -o $@

# NASM assembly
%.o: %.asm
	$(AS) $(ASFLAGS) $< -o $@

# GAS assembly
%.o: %.s
	$(CC) $(CFLAGS) -c $< -o $@

kernel.bin: boot.o kernel.o
	$(LD) $(LDFLAGS) -o $@ $^
```

### Boot Kodu (NASM)

```nasm
; boot.asm
[BITS 16]
[ORG 0x7C00]

start:
    cli
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7C00
    
    ; Kernel-ə keçid
    call load_kernel
    jmp 0x1000:0x0000

load_kernel:
    ; Disk əməliyyatları
    ret

times 510-($-$$) db 0
dw 0xAA55
```

### Kernel C Kodu

```c
void kernel_main(void) {
    char *video = (char*)0xB8000;
    const char *msg = "Kernel yuklendi!";
    
    for (int i = 0; msg[i]; i++) {
        video[i * 2] = msg[i];
        video[i * 2 + 1] = 0x0F;
    }
    
    while(1);
}
```

### GCC Assembly Çıxışı Almaq

```bash
# C-dən assembly yaratmaq
gcc -S -m32 -ffreestanding kernel.c -o kernel.s

# Intel sintaksisi ilə
gcc -S -m32 -ffreestanding -masm=intel kernel.c -o kernel_intel.s
```

### Layihədəki Nümunə Proqram

```nasm
; main.nasm - Windows 64-bit
; Compile: nasm -f win64 main.nasm -o main.obj
; Link: gcc main.obj -o main.exe

section .data
    mesaj db "Salam, Dunya!", 10, 0

section .text
    global main
    extern printf

main:
    sub rsp, 40
    lea rcx, [mesaj]
    call printf
    xor eax, eax
    add rsp, 40
    ret
```

---

## Terminal → Kernel → Disk → RAM → CPU Zənciri

### Prosesin Ümumi Strukturu

```
Terminal → Shell → Kernel → Disk I/O → RAM → CPU
```

### Addım-addım İzah

1. **Shell (bash/cmd)** əmri oxuyur
2. **`execve()` sistem çağırışı** kernel-ə göndərilir
3. **Kernel** diskdən (SSD/HDD) proqramı tapır
4. **Disk Controller** sektorları oxuyur
5. **DMA (Direct Memory Access)** məlumatı RAM-a köçürür
6. **Loader** proqramı yaddaşda düzənləyir
7. **CPU** icra etməyə başlayır

### C və Assembly Səviyyələri

| Səviyyə | Dil | Nümunə |
|---------|-----|--------|
| İstifadəçi proqramı | C/C++ | `main()` funksiyası |
| Sistem çağırışı | C + inline ASM | `read()`, `write()` |
| Kernel | C + Assembly | Linux kernel |
| Bootloader | Assembly | GRUB, boot sector |
| Hardware | Maşın kodu | CPU instruction set |

### Sistem Çağırışı (Syscall) Mexanizmi

```
İstifadəçi proqramı (C)
        ↓
    libc wrapper
        ↓
    int 0x80 / syscall (Assembly)
        ↓
    Kernel mode
        ↓
    Disk driver
        ↓
    SSD/HDD controller
```

### Disk Oxuma Prosesi

```
1. Kernel → ATA/NVMe driver
2. Driver → Port I/O əmrləri (Assembly: IN/OUT)
3. Controller → Disk head/flash oxuma
4. DMA → RAM-a birbaşa transfer
5. Interrupt → Kernel-ə "hazırdır" siqnalı
6. Kernel → İstifadəçi buffer-inə kopyalama
```

### C-dən Assembly-ə Keçid

```c
// C səviyyəsi (libc)
ssize_t read(int fd, void *buf, size_t count);
```

```nasm
; x86-64 Linux syscall
mov rax, 0        ; syscall number (read)
mov rdi, fd       ; file descriptor
mov rsi, buf      ; buffer pointer
mov rdx, count    ; byte count
syscall           ; kernel-ə keçid
```

### Vizual Diaqram

```
SSD Disk                    RAM                      CPU
    │                        │                        │
    ▼                        ▼                        ▼
┌─────────────┐      ┌──────────────┐       ┌─────────────┐
│ Program     │      │  Working Set │       │ Thread-lər  │
│ .exe faylı  │ ───► │  Handle-lər  │ ───►  │ işləyir     │
│             │      │              │       │             │
└─────────────┘      └──────────────┘       └─────────────┘
      │                     │                      │
      └─────────────────────┴──────────────────────┘
                    KERNEL
                    Sistem çağırışları:
                    - NtReadFile (disk)
                    - NtAllocateVirtualMemory (RAM)
                    - NtCreateThread (CPU)
```

---

## Praktik Nümunələr

### Debug Əmrləri

| Əmr | Funksiya |
|-----|----------|
| `strace ./program` | Sistem çağırışlarını göstərir |
| `ltrace ./program` | Library çağırışlarını göstərir |
| `objdump -d program` | Assembly kodunu göstərir |
| `cat /proc/[PID]/maps` | Yaddaş xəritəsini göstərir |

### Disk I/O Test

```bash
dd if=/dev/zero of=/tmp/test_io bs=1K count=10
```

### Windows NT Kernel Sistem Çağırışları

| Funksiya | Təyinatı |
|----------|----------|
| `NtReadFile` | Diskdən oxuma |
| `NtWriteFile` | Diskə yazma |
| `NtAllocateVirtualMemory` | RAM ayırma |
| `NtCreateThread` | Yeni thread yaratma |
| `NtCreateFile` | Fayl/soket açma |
| `NtClose` | Handle bağlama |

---

## GitHub-a Yükləmə

GitHub-a layihə yükləmək üçün əmrlər:

```bash
# README.md faylı yaradırıq
echo "# Github" >> README.md

# Git deposu yaradırıq
git init

# Faylları staging sahəsinə əlavə edirik
git add README.md

# İlk commit
git commit -m "first commit"

# Branch adını main olaraq təyin edirik
git branch -M main

# Uzaq depo əlavə edirik
git remote add origin https://github.com/xeyyam95/Github.git

# GitHub-a yükləyirik
git push -u origin main
```

### Əmrlərin İzahı

1. **`echo "# Github" >> README.md`** - README.md faylı yaradır
2. **`git init`** - Yeni Git deposu yaradır (`.git` qovluğu)
3. **`git add README.md`** - Faylı staging sahəsinə əlavə edir
4. **`git commit -m "first commit"`** - Dəyişiklikləri saxlayır
5. **`git branch -M main`** - Branch adını "main" olaraq dəyişir
6. **`git remote add origin [URL]`** - GitHub deposunu əlavə edir
7. **`git push -u origin main`** - Kodu GitHub-a yükləyir

**Qeyd:** GitHub-da repository yaratmış olmalısınız.

---

## Tövsiyə Olunan Mənbələr

### Linux/Unix Terminal və Shell

| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **The Linux Command Line** | William Shotts | Pulsuz PDF |
| **Linux Pocket Guide** | Daniel J. Barrett | Kompakt kitab |
| **Learning the bash Shell** | Cameron Newham | Shell scripting |

### Sistem Proqramlaşdırması

| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **Operating Systems: Three Easy Pieces** | Remzi & Andrea Arpaci-Dusseau | Pulsuz onlayn |
| **Linux System Programming** | Robert Love | Syscall dərindən |
| **Advanced Programming in the UNIX Environment** | W. Richard Stevens | Klassik |

### Assembly və Aşağı Səviyyə

| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **Assembly Language Step-by-Step** | Jeff Duntemann | Başlanğıc |
| **Programming from the Ground Up** | Jonathan Bartlett | Pulsuz PDF |
| **Low-Level Programming** | Igor Zhirkov | C + ASM |

### Windows Kernel

| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **Windows Internals** | Mark Russinovich | Ən dərin |
| **Windows System Programming** | Johnson M. Hart | Win32 API |

### Pulsuz Onlayn Resurslar

| Resurs | Link | Təyinat |
|--------|------|---------|
| **OSDev Wiki** | wiki.osdev.org | Kernel yazmaq |
| **Linux From Scratch** | linuxfromscratch.org | Praktik |
| **Intel Manuals** | intel.com | CPU instruction set |

---

## 📊 Test Nəticələri

### Sistem Konfiqurasiyası (2026-01-10)

| Komponent | Dəyər |
|-----------|-------|
| **Terminal** | Git Bash (MINGW64) |
| **Kernel** | MINGW64_NT-10.0-19045 |
| **CPU** | Intel Core i5-3230M @ 2.6GHz |
| **RAM** | 8GB |

---

## 📝 Layihə Strukturu

```
Yeni_C_Nasm/
│
├── main.nasm           # NASM nümunə proqramı
├── README.md           # Bu fayl
├── Meslehet.md         # NASM və GCC təlimatları
├── Məlumat.md          # Kernel və sistem məlumatları
│
└── Yeni-layhe/        # Alt layihə
    ├── main.nasm
    ├── Meslehet.md
    └── Məlumat.md
```

---

## 🚀 Başlamaq

```bash
# Layihəni klonlayın
git clone https://github.com/xeyyam95/Github.git

# Qovluğa keçin
cd Yeni_C_Nasm

# NASM proqramını compile edin
nasm -f win64 main.nasm -o main.obj

# Link edin
gcc main.obj -o main.exe

# İcra edin
./main.exe
```

---

## 📧 Əlaqə

**Müəllif:** Xeyyam  
**Tarix:** 2026-01-14

---

*Bu layihə tədris məqsədləri üçün hazırlanmışdır.*
