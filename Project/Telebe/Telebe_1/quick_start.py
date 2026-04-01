"""
Sürətli Başlanğıc - CPU Simulyatorunu necə istifadə etmək olar
"""

from cpu_simulator import CPUSimulator
from alu import ALU

print("="*60)
print("CPU SIMULYATOR - SÜRƏTLI BAŞLANĞIC")
print("="*60)

# ═══════════════════════════════════════════════════════════
# NÜMUNƏ 1: Sadə Hesablama
# ═══════════════════════════════════════════════════════════
print("\n📝 Nümunə 1: Sadə hesablama (5 + 3) * 2")
print("-" * 60)

cpu = CPUSimulator()

# Assembly kodu:
#   MOV EAX, 5
#   ADD EAX, 3
#   SHL EAX, 1    ; 2-yə vurmaq üçün sola sürüşdür

cpu.mov('EAX', 5)
print(f"MOV EAX, 5    → EAX = {cpu.get_register('EAX')}")

cpu.add('EAX', 3)
print(f"ADD EAX, 3    → EAX = {cpu.get_register('EAX')}")

cpu.shl('EAX', 1)
print(f"SHL EAX, 1    → EAX = {cpu.get_register('EAX')}")

print(f"\n✅ Nəticə: (5 + 3) * 2 = {cpu.get_register('EAX')}")


# ═══════════════════════════════════════════════════════════
# NÜMUNƏ 2: İki ədədin maksimumunu tap
# ═══════════════════════════════════════════════════════════
print("\n\n📝 Nümunə 2: İki ədədin maksimumu (15 və 23)")
print("-" * 60)

cpu.reset()  # CPU-nu sıfırla

a, b = 15, 23

# Assembly kodu:
#   MOV EAX, 15
#   MOV EBX, 23
#   CMP EAX, EBX
#   ; Əgər EAX >= EBX, EAX-da qalır
#   ; Əgər EAX < EBX, EBX-i EAX-ə köçür

cpu.mov('EAX', a)
cpu.mov('EBX', b)
cpu.cmp('EAX', 'EBX')

# Python-da şərti məntiqi simulyasiya edirik
if cpu.flags['SF'] == 1:  # EAX < EBX
    cpu.mov('EAX', 'EBX')

print(f"MOV EAX, {a}")
print(f"MOV EBX, {b}")
print(f"CMP EAX, EBX")
print(f"\n✅ Maksimum: {cpu.get_register('EAX')}")


# ═══════════════════════════════════════════════════════════
# NÜMUNƏ 3: ALU ilə bitwise əməliyyatlar
# ═══════════════════════════════════════════════════════════
print("\n\n📝 Nümunə 3: Bitwise AND əməliyyatı")
print("-" * 60)

alu = ALU()

a = 0b11110000  # 240
b = 0b10101010  # 170

result = alu.bitwise_and(a, b)

print(f"A = {a:8d} = {a:08b}")
print(f"B = {b:8d} = {b:08b}")
print(f"      {'─'*8}   {'─'*8}")
print(f"R = {result:8d} = {result:08b}")
print(f"\n✅ {a} AND {b} = {result}")


# ═══════════════════════════════════════════════════════════
# NÜMUNƏ 4: Dövr (Loop) - Toplama
# ═══════════════════════════════════════════════════════════
print("\n\n📝 Nümunə 4: 1-dən 10-a qədər topla")
print("-" * 60)

cpu.reset()

# Assembly kodu:
#   MOV EAX, 0      ; Nəticə
#   MOV ECX, 10     ; Counter
# .loop:
#   ADD EAX, ECX
#   DEC ECX
#   CMP ECX, 0
#   JNZ .loop

cpu.mov('EAX', 0)   # Sum
cpu.mov('ECX', 10)  # Counter

iterations = 0
while cpu.get_register('ECX') > 0:
    cpu.add('EAX', 'ECX')
    cpu.sub('ECX', 1)
    iterations += 1

print(f"İterasiya sayı: {iterations}")
print(f"✅ Nəticə: 1+2+3+...+10 = {cpu.get_register('EAX')}")


# ═══════════════════════════════════════════════════════════
# NÜMUNƏ 5: Registr vəziyyətini göstər
# ═══════════════════════════════════════════════════════════
print("\n\n📝 Nümunə 5: CPU vəziyyəti")
print("-" * 60)

cpu.reset()

# Registrləri müxtəlif dəyərlərlə doldur
cpu.mov('EAX', 100)
cpu.mov('EBX', 200)
cpu.mov('ECX', 300)
cpu.mov('EDX', 400)

cpu.print_state()

print("\n" + "="*60)
print("🎉 Demo tamamlandı!")
print("="*60)
print("\nDaha çox nümunə üçün:")
print("  python demo.py all")
print("\nSənədləşdirmə:")
print("  README.md faylına baxın")
print("="*60)
