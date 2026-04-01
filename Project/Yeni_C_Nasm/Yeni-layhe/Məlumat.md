# Terminal → Kernel → Disk → RAM → CPU Zənciri

## Giriş

Bu sənəd terminaldan proqramın çağırılması və kernel səviyyəsində işləmə mexanizmini izah edir.

---

## 1. Proqramın Diskdən Yaddaşa Yüklənməsi

Terminalda bir proqram çağıranda aşağıdakı proses baş verir:

```
Terminal → Shell → Kernel → Disk I/O → RAM → CPU
```

### Addım-addım proses:

1. **Shell (bash/cmd)** əmri oxuyur
2. **`execve()` sistem çağırışı** kernel-ə göndərilir
3. **Kernel** diskdən (SSD/HDD) proqramı tapır
4. **Disk Controller** sektorları oxuyur
5. **DMA (Direct Memory Access)** məlumatı RAM-a köçürür
6. **Loader** proqramı yaddaşda düzənləyir
7. **CPU** icra etməyə başlayır

---

## 2. C və Assembly Əlaqəsi

| Səviyyə | Dil | Nümunə |
|---------|-----|--------|
| İstifadəçi proqramı | C/C++ | `main()` funksiyası |
| Sistem çağırışı | C + inline ASM | `read()`, `write()` |
| Kernel | C + Assembly | Linux kernel |
| Bootloader | Assembly | GRUB, boot sector |
| Hardware | Maşın kodu | CPU instruction set |

---

## 3. Sistem Çağırışı (Syscall) Mexanizmi

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

### Interrupt mexanizmi:
- CPU `syscall` və ya `int 0x80` instruction-ı icra edir
- Ring 3 (user mode) → Ring 0 (kernel mode) keçid baş verir
- Kernel disk əməliyyatını həyata keçirir

---

## 4. Disk Oxuma Prosesi (Aşağı Səviyyə)

```
1. Kernel → ATA/NVMe driver
2. Driver → Port I/O əmrləri (Assembly: IN/OUT)
3. Controller → Disk head/flash oxuma
4. DMA → RAM-a birbaşa transfer
5. Interrupt → Kernel-ə "hazırdır" siqnalı
6. Kernel → İstifadəçi buffer-inə kopyalama
```

---

## 5. C-dən Assembly-ə Keçid Nümunəsi

### Linux-da `read()` funksiyası:

```c
// C səviyyəsi (libc)
ssize_t read(int fd, void *buf, size_t count);
```

### Daxildə Assembly-ə çevrilir:

```nasm
; x86-64 Linux syscall
mov rax, 0        ; syscall number (read)
mov rdi, fd       ; file descriptor
mov rsi, buf      ; buffer pointer
mov rdx, count    ; byte count
syscall           ; kernel-ə keçid
```

---

## 6. Praktik Terminal Əmrləri

| Əmr | Funksiya |
|-----|----------|
| `strace ./program` | Sistem çağırışlarını göstərir |
| `ltrace ./program` | Library çağırışlarını göstərir |
| `objdump -d program` | Assembly kodunu göstərir |
| `cat /proc/[PID]/maps` | Yaddaş xəritəsini göstərir |

---

# Real Test Nəticələri (2026-01-10)

## Sistem Konfiqurasiyası

| Komponent | Dəyər |
|-----------|-------|
| **Terminal** | Git Bash (MINGW64) |
| **Shell** | `/usr/bin/bash` (PID: 357) |
| **Kernel** | MINGW64_NT-10.0-19045 |
| **CPU** | Intel Core i5-3230M @ 2.6GHz |
| **RAM** | 8GB (Total: 8,243,268 KB) |
| **Boş RAM** | ~1.5GB |

## Disk I/O Test Nəticəsi

```
dd if=/dev/zero of=/tmp/test_io bs=1K count=10

Nəticə:
- 10KB yazıldı
- Sürət: 1.8 MB/s
- Vaxt: 0.006 saniyə
```

---

# WhatsApp Kernel Analizi

## Proses Məlumatları

| Parametr | Dəyər |
|----------|-------|
| **Proses adı** | WhatsApp.Root.exe |
| **PID** | 2968 |
| **Parent PID** | 6992 |
| **Prioritet** | 4 (Normal) |

## Disk (SSD) Məlumatları

| Parametr | Dəyər |
|----------|-------|
| **EXE Yolu** | `C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2587.9.0_x64__cv1g1gvanyjgm\` |
| **Fayl adı** | `WhatsApp.Root.exe` |
| **Versiya** | 2.2587.9.0 |
| **Arxitektura** | x64 (64-bit) |

## RAM (Yaddaş) İstifadəsi

| Parametr | Dəyər |
|----------|-------|
| **Working Set** | ~201 MB (210,518,016 bytes) |
| **Mem Usage** | ~205 MB |

## Kernel Resursları

| Parametr | Dəyər | İzah |
|----------|-------|------|
| **Handle Count** | 1441 | Açıq kernel obyektləri (fayllar, soketlər, registrlər) |
| **Thread Count** | 35 | Paralel icra axınları |

## Zaman Məlumatı

| Parametr | Dəyər |
|----------|-------|
| **Yaranma tarixi** | 2026-01-10 |
| **Yaranma vaxtı** | 19:00:10 |

---

## Kernel Zənciri Vizual Diaqram

```
SSD Disk                    RAM                      CPU
    │                        │                        │
    ▼                        ▼                        ▼
┌─────────────┐      ┌──────────────┐       ┌─────────────┐
│ WhatsApp    │      │  201 MB      │       │ 35 Thread   │
│ .exe faylı  │ ───► │  Working Set │ ───►  │ işləyir     │
│ (WindowsApps)│      │  1441 Handle │       │ Priority: 4 │
└─────────────┘      └──────────────┘       └─────────────┘
      │                     │                      │
      └─────────────────────┴──────────────────────┘
                    KERNEL (NT Kernel)
                    Sistem çağırışları:
                    - NtReadFile (disk)
                    - NtAllocateVirtualMemory (RAM)
                    - NtCreateThread (CPU)
```

---

## Windows NT Kernel Sistem Çağırışları

WhatsApp işləyərkən istifadə olunan əsas kernel funksiyaları:

| Funksiya | Təyinatı |
|----------|----------|
| `NtReadFile` | Diskdən oxuma |
| `NtWriteFile` | Diskə yazma |
| `NtAllocateVirtualMemory` | RAM ayırma |
| `NtCreateThread` | Yeni thread yaratma |
| `NtCreateFile` | Fayl/soket açma |
| `NtClose` | Handle bağlama |

---

## Nəticə

Terminal əmri ilə proqram çağırılanda:

1. ✅ Shell əmri parse edir
2. ✅ Kernel sistem çağırışı qəbul edir
3. ✅ Disk driver SSD/HDD-dən oxuyur
4. ✅ DMA məlumatı RAM-a köçürür
5. ✅ CPU icra edir

**Bu zəncir hər proqram üçün eyni işləyir - WhatsApp, Chrome, VS Code və s.**

---

*Sənəd tarixi: 2026-01-10*
*Sistem: Windows 10 (MINGW64)*

---

# Tövsiyə Olunan Kitablar

## Linux/Unix Terminal və Shell üçün:
| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **The Linux Command Line** | William Shotts | Pulsuz PDF mövcuddur |
| **Linux Pocket Guide** | Daniel J. Barrett | Kompakt məlumat kitabı |
| **Learning the bash Shell** | Cameron Newham | Shell scripting üçün |

## Sistem Proqramlaşdırması (Kernel, Syscalls) üçün:
| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **Operating Systems: Three Easy Pieces** | Remzi & Andrea Arpaci-Dusseau | Pulsuz onlayn |
| **Linux System Programming** | Robert Love | Syscall dərindən |
| **Advanced Programming in the UNIX Environment** | W. Richard Stevens | Klassik kitab |

## Assembly və Aşağı Səviyyə üçün:
| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **Assembly Language Step-by-Step** | Jeff Duntemann | Başlanğıc üçün |
| **Programming from the Ground Up** | Jonathan Bartlett | Pulsuz PDF |
| **Low-Level Programming: C, Assembly, and Program Execution** | Igor Zhirkov | C + ASM birlikdə |

## Windows Kernel üçün:
| Kitab | Müəllif | Qeyd |
|-------|---------|------|
| **Windows Internals** | Mark Russinovich | Microsoft Press, ən dərin |
| **Windows System Programming** | Johnson M. Hart | Win32 API |

---

## Pulsuz Onlayn Resurslar

| Resurs | Link | Təyinat |
|--------|------|---------|
| **OSDev Wiki** | wiki.osdev.org | Kernel yazmaq üçün |
| **Linux From Scratch** | linuxfromscratch.org | Praktik öyrənmə |
| **Intel Software Developer Manuals** | intel.com | CPU instruction set |

---

*Kitab siyahısı əlavə edildi: 2026-01-10*
