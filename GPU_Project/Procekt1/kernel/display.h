#ifndef DISPLAY_H
#define DISPLAY_H

#include <stdint.h>

class Display {
private:
    static const uint32_t VGA_ADDRESS = 0xB8000;
    static const uint16_t VGA_WIDTH = 80;
    static const uint16_t VGA_HEIGHT = 25;
    uint16_t cursor_x;
    uint16_t cursor_y;
    uint8_t color;
    
public:
    Display();
    void clear();
    void print(const char* str);
    void putchar(char c);
    void set_color(uint8_t foreground, uint8_t background);
    void move_cursor(uint16_t x, uint16_t y);
};

#endif
