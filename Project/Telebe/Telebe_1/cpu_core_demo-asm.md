;; ══════════════════════════════════════════════════════════════
;; CPU NÜVƏSİ - x86 Assembly ilə İkili Kod Sxemi
;; Nano/Mikro kod səviyyəsində işləmə prinsipi
;; ══════════════════════════════════════════════════════════════

section .data
    msg db "CPU Nuvesi isleyir!", 0x0A
    len equ $ - msg

section .text
    global _start

;; ┌──────────────────────────────────────────────────────────┐
;; │ MƏRHƏLƏLƏRİ 1: FETCH (GƏTİR) - Yaddaşdan əmr gətir    │
;; │                                                          │
;; │ Yaddaş ünvanı:  0x00400000                               │
;; │ Binary məzmun:  10111000 00000101 00000000 00000000...    │
;; └──────────────────────────────────────────────────────────┘

_start:
;; ════════════════════════════════════════════════════════════
;; ƏMƏL 1:  MOV EAX, 5    (EAX registrinə 5 yükləa)
;; ════════════════════════════════════════════════════════════
;;
;; x86 Assembly:     MOV EAX, 5
;; Maşın kodu (HEX): B8 05 00 00 00
;; İKİLİ KOD (BIN):
;; ┌────────┬────────┬────────┬────────┬────────┐
;; │10111000│00000101│00000000│00000000│00000000│
;; ├────────┼────────┼────────┼────────┼────────┤
;; │ OPCODE │ Dəyər=5│  0     │   0    │   0    │
;; │ "MOV"  │(little │        │        │        │
;; │ EAX,imm│endian) │        │        │        │
;; └────────┴────────┴────────┴────────┴────────┘
;;
;; Mikrokod çevrilməsi (μOps):
;;   μOp1: LOAD_IMM  tmp0, 0x00000005
;;   μOp2: MOV_REG   EAX, tmp0
;;
;; Tranzistor səviyyəsi:
;;   10111000 → 8 tranzistor ON/OFF vəziyyəti
;;   ⚡🚫⚡⚡⚡🚫🚫🚫
;;

    mov eax, 5          ; B8 05 00 00 00

;; ════════════════════════════════════════════════════════════
;; ƏMƏL 2:  MOV EBX, 3    (EBX registrinə 3 yüklə)
;; ════════════════════════════════════════════════════════════
;;
;; x86 Assembly:     MOV EBX, 3
;; Maşın kodu (HEX): BB 03 00 00 00
;; İKİLİ KOD (BIN):
;; ┌────────┬────────┬────────┬────────┬────────┐
;; │10111011│00000011│00000000│00000000│00000000│
;; ├────────┼────────┼────────┼────────┼────────┤
;; │ OPCODE │ Dəyər=3│   0    │   0    │   0    │
;; │ "MOV"  │        │        │        │        │
;; │ EBX,imm│        │        │        │        │
;; └────────┴────────┴────────┴────────┴────────┘
;;
;; Mikrokod:
;;   μOp1: LOAD_IMM  tmp1, 0x00000003
;;   μOp2: MOV_REG   EBX, tmp1

    mov ebx, 3          ; BB 03 00 00 00

;; ════════════════════════════════════════════════════════════
;; ƏMƏL 3:  ADD EAX, EBX   (EAX = EAX + EBX = 5 + 3 = 8)
;; ════════════════════════════════════════════════════════════
;;
;; x86 Assembly:     ADD EAX, EBX
;; Maşın kodu (HEX): 01 D8
;; İKİLİ KOD (BIN):
;; ┌────────┬────────┐
;; │00000001│11011000│
;; ├────────┼────────┤
;; │ OPCODE │ ModR/M │
;; │ "ADD"  │11=reg  │
;; │        │011=EBX │
;; │        │000=EAX │
;; └────────┴────────┘
;;
;; ┌─────── ModR/M Baytı Detalları ────────┐
;; │  Bit:  7  6 │ 5  4  3 │ 2  1  0      │
;; │       ──────┼─────────┼──────────     │
;; │        1  1 │ 0  1  1 │ 0  0  0      │
;; │        MOD  │  REG    │   R/M        │
;; │       (reg) │ (EBX)   │  (EAX)       │
;; └────────────────────────────────────────┘
;;
;; ══════ MİKROKOD SXEMİ (ALU daxili) ══════
;;
;;   μOp1: READ_REG   tmp0, EAX    → tmp0 = 00000000 00000000 00000000 00000101
;;   μOp2: READ_REG   tmp1, EBX    → tmp1 = 00000000 00000000 00000000 00000011
;;   μOp3: ALU_ADD    tmp2, tmp0, tmp1
;;   μOp4: WRITE_REG  EAX, tmp2    → EAX  = 00000000 00000000 00000000 00001000
;;   μOp5: UPDATE_FLAGS CF=0, ZF=0, SF=0, OF=0

    add eax, ebx        ; 01 D8


;; ════════════════════════════════════════════════════════════
;; ƏMƏL 4:  SHL EAX, 1   (Sola sürüşdür = 2-yə vur)
;; ════════════════════════════════════════════════════════════
;;
;; x86 Assembly:     SHL EAX, 1
;; Maşın kodu (HEX): D1 E0
;; İKİLİ KOD:
;; ┌────────┬────────┐
;; │11010001│11100000│
;; └────────┴────────┘
;;
;; ══════ NANO TRANZİSTOR SƏVİYYƏSİ ══════
;;
;;  ƏVVƏL (EAX = 8):     SONRA (EAX = 16):
;;  00000000 00001000     00000000 00010000
;;                ↓ sola sürüşdür ↓
;;  ┌─┬─┬─┬─┬─┬─┬─┬─┐   ┌─┬─┬─┬─┬─┬─┬─┬─┐
;;  │0│0│0│0│1│0│0│0│ → │0│0│0│1│0│0│0│0│
;;  └─┴─┴─┴─┴─┴─┴─┴─┘   └─┴─┴─┴─┴─┴─┴─┴─┘
;;  🚫🚫🚫🚫⚡🚫🚫🚫   🚫🚫🚫⚡🚫🚫🚫🚫
;;
;; Mikrokod:
;;   μOp1: READ_REG   tmp0, EAX
;;   μOp2: SHIFT_L    tmp1, tmp0, 1
;;   μOp3: WRITE_REG  EAX, tmp1

    shl eax, 1           ; D1 E0


;; ════════════════════════════════════════════════════════════
;; ƏMƏL 5:  CMP & JE (Müqayisə və şərti keçid)
;; ════════════════════════════════════════════════════════════
;;
;; CMP EAX, 16  →  3D 10 00 00 00
;; İKİLİ:
;; ┌────────┬────────┬────────┬────────┬────────┐
;; │00111101│00010000│00000000│00000000│00000000│
;; └────────┴────────┴────────┴────────┴────────┘
;;
;; Mikrokod:
;;   μOp1: READ_REG   tmp0, EAX
;;   μOp2: ALU_SUB    tmp1, tmp0, 16  (fərqi hesabla)
;;   μOp3: UPDATE_FLAGS  ZF=1 (bərabərdir!), CF=0, SF=0
;;   μOp4: BRANCH_IF  ZF==1, target_address

    cmp eax, 16          ; 3D 10 00 00 00
    je  .equal           ; 74 XX (şərti keçid)

    ; Bərabər deyilsə bura gəlir
    jmp .done

.equal:
    ; EAX == 16 olduqda bura gəlir (Nəticə düzgündür!)
    nop                  ; 90 → 10010000

.done:

;; ════════════════════════════════════════════════════════════
;; SİSTEM ÇAĞIRIŞI - Linux Syscall (exit)
;; ════════════════════════════════════════════════════════════
;;
;; MOV EAX, 1  → Syscall nömrəsi (exit)
;; MOV EBX, 0  → Çıxış kodu
;; INT 0x80    → Kəsmə (interrupt) - kernel çağır
;;
;; INT 0x80 İkili: CD 80 → 11001101 10000000
;;
;; Mikrokod (INT 0x80):
;;   μOp1: SAVE_STATE    (registrləri saxla)
;;   μOp2: PRIV_CHECK    (icazə yoxla)
;;   μOp3: LOAD_IDT      (Interrupt Descriptor Table)
;;   μOp4: JUMP_KERNEL   (kernel rejiminə keç)
;;   μOp5: EXEC_SYSCALL  (sistem çağırışını icra et)

    mov eax, 1           ; B8 01 00 00 00
    mov ebx, 0           ; BB 00 00 00 00
    int 0x80             ; CD 80