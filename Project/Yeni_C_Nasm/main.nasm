; Sadə NASM proqramı - Windows 64-bit
; Compile: nasm -f win64 main.nasm -o main.obj
; Link: gcc main.obj -o main.exe

section .data
    mesaj db "Salam, Dunya!", 10, 0    ; 10 = newline, 0 = null terminator

section .text
    global main
    extern printf

main:
    ; Stack alignment (Windows ABI üçün vacibdir)
    sub rsp, 40

    ; printf funksiyasını çağır
    lea rcx, [mesaj]      ; birinci arqument - mesajın adresi
    call printf

    ; Proqramı bitir
    xor eax, eax          ; return 0
    add rsp, 40
    ret
