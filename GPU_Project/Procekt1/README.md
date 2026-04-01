# Wow Operating System

A simple x86 operating system written in C++ and Assembly.

## Features
- Custom bootloader
- 32-bit protected mode
- VGA text mode display
- Basic memory management
- Interrupt handling
- Command line interface

## Development Phases

### Phase 1: Basic Boot (Current)
- [x] Bootloader in assembly
- [x] Switch to protected mode
- [x] Load kernel
- [x] Basic display driver

### Phase 2: Core Systems
- [ ] Memory management (paging)
- [ ] Interrupt handling (IDT, IRQ)
- [ ] Keyboard driver
- [ ] Basic file system

### Phase 3: User Interface
- [ ] Command interpreter
- [ ] Basic graphics mode
- [ ] Window manager
- [ ] Mouse support

### Phase 4: Applications
- [ ] Text editor
- [ ] File manager
- [ ] Calculator
- [ ] System utilities

## Building

1. Install required tools:
   ```bash
   sudo apt-get install gcc g++ nasm make qemu
   sudo apt-get install gcc-multilib g++-multilib
   ```

2. Build cross-compiler:
   ```bash
   # Follow GCC cross-compiler tutorial for i686-elf target
   ```

3. Compile Wow OS:
   ```bash
   make clean
   make
   ```

4. Run in QEMU:
   ```bash
   make run
   ```

## Project Structure
```
Procekt1/
├── boot/          # Bootloader files
├── kernel/        # Kernel source code
├── drivers/       # Device drivers
├── lib/           # System libraries
├── apps/          # User applications
└── build/         # Build output
```

## License
MIT License - Wow Operating System 2024
