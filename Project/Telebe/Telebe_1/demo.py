"""
CPU SİMULYATORU DEMO
Assembly faylındakı əməlləri Python-da simulyasiya edir
"""

from cpu_simulator import CPUSimulator
from alu import ALU
from instruction_set import InstructionSet


def demo_basic_operations():
    """Əsas əməlləri göstər (cpu_core_demo-asm.md-dən)"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*15 + "CPU NÜVƏSİ SİMULYATORU" + " "*21 + "║")
    print("║" + " "*10 + "x86 Assembly Python-da simulyasiya" + " "*13 + "║")
    print("╚" + "="*58 + "╝\n")
    
    cpu = CPUSimulator()
    
    print("🔹 ƏMƏL 1: MOV EAX, 5  (EAX registrinə 5 yüklə)")
    cpu.mov('EAX', 5)
    print(f"   Nəticə: EAX = {cpu.get_register('EAX')}")
    
    print("\n🔹 ƏMƏL 2: MOV EBX, 3  (EBX registrinə 3 yüklə)")
    cpu.mov('EBX', 3)
    print(f"   Nəticə: EBX = {cpu.get_register('EBX')}")
    
    print("\n🔹 ƏMƏL 3: ADD EAX, EBX  (EAX = EAX + EBX = 5 + 3 = 8)")
    cpu.add('EAX', 'EBX')
    print(f"   Nəticə: EAX = {cpu.get_register('EAX')}")
    print(f"   Bayraqlar: ZF={cpu.flags['ZF']}, CF={cpu.flags['CF']}")
    
    print("\n🔹 ƏMƏL 4: SHL EAX, 1  (Sola sürüşdür = 2-yə vur)")
    print(f"   Əvvəl:  EAX = {cpu.get_register('EAX')} = {cpu._int_to_binary(cpu.get_register('EAX'))}")
    cpu.shl('EAX', 1)
    print(f"   Sonra:  EAX = {cpu.get_register('EAX')} = {cpu._int_to_binary(cpu.get_register('EAX'))}")
    
    print("\n🔹 ƏMƏL 5: CMP EAX, 16  (EAX-i 16 ilə müqayisə et)")
    cpu.cmp('EAX', 16)
    if cpu.flags['ZF'] == 1:
        print("   ✅ EAX == 16 (Bərabərdir!)")
    else:
        print("   ❌ EAX != 16 (Bərabər deyil)")
    
    # CPU vəziyyətini göstər
    cpu.print_state()
    cpu.print_history()


def demo_alu_operations():
    """ALU əməliyyatları"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*20 + "ALU ƏMƏLİYYATLARI" + " "*21 + "║")
    print("╚" + "="*58 + "╝\n")
    
    alu = ALU()
    
    # Toplama
    print("🔹 TOPLAMA (5 + 3):")
    result = alu.add(5, 3)
    print(f"   5 + 3 = {result}")
    print(f"   Carry: {alu.carry}, Overflow: {alu.overflow}")
    
    # Çıxma
    print("\n🔹 ÇIXMA (10 - 4):")
    result = alu.subtract(10, 4)
    print(f"   10 - 4 = {result}")
    
    # Vurma
    print("\n🔹 VURMA (7 * 8):")
    result = alu.multiply(7, 8)
    print(f"   7 * 8 = {result}")
    
    # Bölmə
    print("\n🔹 BÖLMƏ (20 / 3):")
    quotient, remainder = alu.divide(20, 3)
    print(f"   20 / 3 = {quotient}, qalıq = {remainder}")
    
    # Bitwise əməliyyatlar
    print("\n🔹 BITWISE AND (0b11110000 & 0b10101010):")
    result = alu.bitwise_and(0b11110000, 0b10101010)
    print(f"   {0b11110000:08b}")
    print(f" & {0b10101010:08b}")
    print(f"   ──────────")
    print(f"   {result:08b}  ({result})")
    
    print("\n🔹 BITWISE OR (0b11110000 | 0b10101010):")
    result = alu.bitwise_or(0b11110000, 0b10101010)
    print(f"   {0b11110000:08b}")
    print(f" | {0b10101010:08b}")
    print(f"   ──────────")
    print(f"   {result:08b}  ({result})")
    
    print("\n🔹 BITWISE XOR (0b11110000 ^ 0b10101010):")
    result = alu.bitwise_xor(0b11110000, 0b10101010)
    print(f"   {0b11110000:08b}")
    print(f" ^ {0b10101010:08b}")
    print(f"   ──────────")
    print(f"   {result:08b}  ({result})")
    
    # Shift əməliyyatları
    print("\n🔹 SHIFT LEFT (8 << 2):")
    result = alu.shift_left(8, 2)
    print(f"   {8:08b} << 2 = {result:08b}  ({result})")
    
    print("\n🔹 SHIFT RIGHT (32 >> 2):")
    result = alu.shift_right(32, 2)
    print(f"   {32:08b} >> 2 = {result:08b}  ({result})")


def demo_complex_program():
    """Mürəkkəb proqram - faktorial hesablama"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*15 + "MÜRƏKKƏB PROQRAM: FAKTORİAL" + " "*16 + "║")
    print("╚" + "="*58 + "╝\n")
    
    cpu = CPUSimulator()
    
    # 5! hesabla (5 * 4 * 3 * 2 * 1 = 120)
    n = 5
    print(f"📊 {n}! hesablanır...")
    print(f"\nAssembly kodu:")
    print(f"  MOV EAX, {n}      ; EAX-ə {n} yüklə")
    print(f"  MOV EBX, 1      ; EBX-ə 1 yüklə (nəticə)")
    print(f"  .loop:")
    print(f"    CMP EAX, 0    ; EAX-i 0 ilə müqayisə et")
    print(f"    JE .done      ; Əgər 0-sa, bitir")
    print(f"    IMUL EBX, EAX ; EBX = EBX * EAX")
    print(f"    DEC EAX       ; EAX--")
    print(f"    JMP .loop     ; Döngüyə qayıt")
    print(f"  .done:")
    print(f"\nSimulyasiya:\n")
    
    # Python simulyasiyası
    cpu.mov('EAX', n)      # counter
    cpu.mov('EBX', 1)      # result
    cpu.mov('ECX', 0)      # loop counter (debug üçün)
    
    max_iterations = 10
    for i in range(max_iterations):
        eax_value = cpu.get_register('EAX')
        ebx_value = cpu.get_register('EBX')
        
        print(f"  İterasiya {i+1}: EAX={eax_value}, EBX={ebx_value}")
        
        # CMP EAX, 0
        cpu.cmp('EAX', 0)
        if cpu.flags['ZF'] == 1:  # JE .done
            print(f"\n✅ Nəticə: {n}! = {ebx_value}")
            break
        
        # Manual multiply (IMUL simulyasiyası)
        result = ebx_value * eax_value
        cpu.mov('EBX', result)
        
        # DEC EAX
        cpu.sub('EAX', 1)
    
    cpu.print_state()


def demo_instruction_set():
    """Əmr seti məlumatları"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*20 + "ƏMR SETİ SİYAHISI" + " "*21 + "║")
    print("╚" + "="*58 + "╝\n")
    
    iset = InstructionSet()
    
    # Əmr kateqoriyaları
    categories = [
        ('Data Transfer', '📦'),
        ('Arithmetic', '➕'),
        ('Logic', '🔣'),
        ('Shift/Rotate', '↔️'),
        ('Control Flow', '🔀')
    ]
    
    for category, emoji in categories:
        print(f"\n{emoji}  {category.upper()}")
        print("─" * 50)
        instructions = iset.list_by_category(category)
        for name, info in instructions:
            print(f"  {name:8s} 0x{info['opcode']:4s} - {info['description']}")


def demo_binary_visualization():
    """İkili kod vizuallaşdırması"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*15 + "İKİLİ KOD VİZUALLAŞDIRMA" + " "*18 + "║")
    print("╚" + "="*58 + "╝\n")
    
    # MOV EAX, 5 əmrini göstər
    print("🔹 ƏMR: MOV EAX, 5")
    print("\nMaşın kodu (HEX): B8 05 00 00 00")
    print("\nİkili kod (BIN):")
    print("┌────────┬────────┬────────┬────────┬────────┐")
    print("│10111000│00000101│00000000│00000000│00000000│")
    print("├────────┼────────┼────────┼────────┼────────┤")
    print("│ OPCODE │ Dəyər=5│    0   │    0   │    0   │")
    print("│  MOV   │(little │        │        │        │")
    print("│ EAX,imm│endian) │        │        │        │")
    print("└────────┴────────┴────────┴────────┴────────┘")
    
    print("\n🔹 Tranzistor səviyyəsi (OPCODE: 10111000):")
    print("   ⚡🚫⚡⚡⚡🚫🚫🚫")
    print("   ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑")
    print("   1  0  1  1  1  0  0  0")
    
    # ADD EAX, EBX
    print("\n\n🔹 ƏMR: ADD EAX, EBX")
    print("\nMaşın kodu (HEX): 01 D8")
    print("\nİkili kod (BIN):")
    print("┌────────┬────────┐")
    print("│00000001│11011000│")
    print("├────────┼────────┤")
    print("│ OPCODE │ ModR/M │")
    print("│  ADD   │ 11=reg │")
    print("│        │ 011=EBX│")
    print("│        │ 000=EAX│")
    print("└────────┴────────┘")


def main():
    """Əsas demo funksiyası"""
    import sys
    
    if len(sys.argv) > 1:
        demo_choice = sys.argv[1]
    else:
        demo_choice = "all"
    
    demos = {
        "1": ("Əsas əməllər", demo_basic_operations),
        "2": ("ALU əməliyyatları", demo_alu_operations),
        "3": ("Faktorial proqramı", demo_complex_program),
        "4": ("Əmr seti", demo_instruction_set),
        "5": ("İkili kod vizuallaşdırma", demo_binary_visualization),
        "all": ("Hamısı", None)
    }
    
    if demo_choice == "all":
        demo_basic_operations()
        demo_alu_operations()
        demo_complex_program()
        demo_instruction_set()
        demo_binary_visualization()
    elif demo_choice in demos:
        name, func = demos[demo_choice]
        print(f"\n🚀 {name} göstərilir...\n")
        func()
    else:
        print("CPU Simulyator Demo")
        print("="*50)
        print("\nİstifadə:")
        print("  python demo.py [seçim]")
        print("\nSeçimlər:")
        for key, (name, _) in demos.items():
            print(f"  {key:4s} - {name}")
        print("\nNümunə:")
        print("  python demo.py 1")
        print("  python demo.py all")


if __name__ == "__main__":
    main()
