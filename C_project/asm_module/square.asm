; NASM Assembly - Windows x64
; Funksiya: square - Ədədin kvadratını hesablayır

section .text
global square

square:
    ; RCX - ilk arqument (Windows x64 calling convention)
    ; Funksiya: int square(int x)
    ; Return: x * x
    
    mov eax, ecx        ; x-i EAX-a köçür
    imul eax, eax       ; EAX = EAX * EAX (kvadrat)
    ret                 ; Nəticə EAX-dadır
