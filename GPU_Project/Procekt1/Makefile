# Wow OS Build System

CC = i686-elf-g++
AS = nasm
LD = i686-elf-ld

CFLAGS = -ffreestanding -O2 -Wall -Wextra -fno-exceptions -fno-rtti
ASFLAGS = -f elf32
LDFLAGS = -T linker.ld -nostdlib

KERNEL_OBJS = kernel/kernel.o kernel/display.o kernel/memory.o kernel/interrupts.o
BOOT_BIN = boot/boot.bin

all: wowos.iso

kernel.bin: $(KERNEL_OBJS)
	$(LD) $(LDFLAGS) -o kernel.bin $(KERNEL_OBJS)

boot.bin: boot/boot.asm
	$(AS) -f bin boot/boot.asm -o boot/boot.bin

wowos.img: boot.bin kernel.bin
	dd if=/dev/zero of=wowos.img bs=512 count=2880
	dd if=boot/boot.bin of=wowos.img conv=notrunc
	dd if=kernel.bin of=wowos.img bs=512 seek=1 conv=notrunc

wowos.iso: wowos.img
	mkdir -p iso
	cp wowos.img iso/
	genisoimage -o wowos.iso -b wowos.img iso/

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.asm
	$(AS) $(ASFLAGS) $< -o $@

clean:
	rm -f kernel/*.o boot/*.bin *.bin *.img *.iso
	rm -rf iso/

run: wowos.iso
	qemu-system-i386 -cdrom wowos.iso
