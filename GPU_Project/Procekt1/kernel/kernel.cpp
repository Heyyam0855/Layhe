#include "kernel.h"
#include "display.h"
#include "memory.h"
#include "interrupts.h"

extern "C" void kernel_main() {
    // Initialize display
    Display display;
    display.clear();
    display.print("Wow OS v1.0\n");
    display.print("Copyright 2024 - Wow Operating System\n");
    display.print("----------------------------------------\n");
    
    // Initialize memory manager
    MemoryManager::initialize();
    
    // Initialize interrupt handlers
    InterruptManager::initialize();
    
    // Enable interrupts
    asm volatile("sti");
    
    // Main kernel loop
    display.print("System ready.\n");
    display.print("Wow OS > ");
    
    while(true) {
        // Handle system events
        asm volatile("hlt");
    }
}
