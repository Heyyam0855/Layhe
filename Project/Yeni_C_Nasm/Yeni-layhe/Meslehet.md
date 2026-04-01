User: Deyəkgi assenbly illə çəkirdək kodu yazıram Əvvəlcə pıllan düzəlir sonra 
C və ya C++ üzərindən gcc assenbly koduna çevrlir Bu qaydada bəzi metotlar bəzər işləyir Çüki çəkirdək kodu gcc isdfadə olunur bəzəndə nasm assenbly üçün bəzi allətlər lazım olur

GitHub Copilot: Başa düşdüm! Siz kernel (çəkirdək) inkişafı edirsiniz və qarışıq toolchain istifadə edirsiniz:

## Sizin İş Axınınız

```
C/C++ → GCC → AT&T/GAS Assembly
         +
NASM → Intel Assembly (boot, low-level)
```

## Tipik Kernel Layihə Strukturu

````makefile
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
````

## Boot Kodu (NASM)

````nasm
; filepath: boot.asm
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
````

## Kernel C Kodu

````c
void kernel_main(void) {
    char *video = (char*)0xB8000;
    const char *msg = "Kernel yuklendi!";
    
    for (int i = 0; msg[i]; i++) {
        video[i * 2] = msg[i];
        video[i * 2 + 1] = 0x0F;
    }
    
    while(1);
}
````

## GCC Assembly Çıxışı Almaq

```bash
# C-dən assembly yaratmaq
gcc -S -m32 -ffreestanding kernel.c -o kernel.s

# Intel sintaksisi ilə
gcc -S -m32 -ffreestanding -masm=intel kernel.c -o kernel_intel.s
```

## Lazımlı Alətlər (Windows)

```powershell
# MinGW/GCC
winget install -e --id mingw-w64

# NASM
winget install -e --id NASM.NASM

# QEMU (test üçün)
winget install -e --id SoftwareFreedomConservancy.QEMU
```

Hansı hissədə kömək lazımdır - boot, memory management, interrupts?

User: Bəs nasm gcc üzərində işlətmək üçün hansı aləti quraşdırmaq lazımdır ..

VS Code: Bu sual Visual Studio Code ilə əlaqəli deyil. Sualınız NASM (Netwide Assembler) və GCC (GNU Compiler Collection) haqqındadır ki, bu ümumi proqramlaşdırma alətləridir.

Lakin VS Code-da assembly inkişafı üçün axtarış edə bilərsiniz: 

Using "Search Extensions"
Completed with input: {"keywords":["nasm","assembly","x86"],"category":"Programming Languages"}

VS Code-da NASM və GCC ilə assembly inkişafı üçün bu uzantıları tövsiyə edirəm:


```vscode-extensions
rights.nas-vscode,13xforever.language-x86-64-assembly,kratosgado.nasm-compiler-linux
```


Bu uzantıları quraşdırmaq üçün **Search marketplace** əmrindən istifadə edə bilərsiniz:



Search Extension Marketplace



**Qeyd:** NASM və GCC-nin özünü sisteminizdə ayrıca quraşdırmalısınız (VS Code uzantıları deyil). Windows üçün:
- NASM: https://nasm.us saytından yükləyin
- GCC: MinGW və ya MSYS2 vasitəsilə quraşdırın