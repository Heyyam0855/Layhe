"""
ALU (Arithmetic Logic Unit) - Hesablama və Məntiqi Vahid
Bütün arifmetik və məntiqi əməliyyatları yerinə yetirir
"""

class ALU:
    """ALU - CPU-nun hesablama bloku"""
    
    def __init__(self):
        self.last_result = 0
        self.carry = 0
        self.overflow = 0
    
    def add(self, a, b, mask=0xFFFFFFFF):
        """İkilik toplama (32-bit)
        
        Tranzistor səviyyəsi:
        ┌─────┬─────┬──────┬────────┐
        │  A  │  B  │ Cin  │  Sum   │
        ├─────┼─────┼──────┼────────┤
        │  0  │  0  │  0   │   0    │
        │  0  │  1  │  0   │   1    │
        │  1  │  0  │  0   │   1    │
        │  1  │  1  │  0   │   0    │
        └─────┴─────┴──────┴────────┘
        """
        result = a + b
        self.last_result = result & mask
        self.carry = 1 if result > mask else 0
        self.overflow = self._check_overflow_add(a, b, self.last_result, mask)
        return self.last_result
    
    def subtract(self, a, b, mask=0xFFFFFFFF):
        """İkilik çıxma (32-bit)"""
        result = a - b
        self.last_result = result & mask
        self.carry = 1 if b > a else 0
        return self.last_result
    
    def multiply(self, a, b, mask=0xFFFFFFFF):
        """Vurma"""
        result = a * b
        self.last_result = result & mask
        self.carry = 1 if result > mask else 0
        return self.last_result
    
    def divide(self, a, b):
        """Bölmə"""
        if b == 0:
            raise ZeroDivisionError("Sıfıra bölmə mümkün deyil!")
        self.last_result = a // b
        remainder = a % b
        return self.last_result, remainder
    
    def bitwise_and(self, a, b):
        """Bitwise AND
        
        0 AND 0 = 0
        0 AND 1 = 0
        1 AND 0 = 0
        1 AND 1 = 1
        """
        self.last_result = a & b
        return self.last_result
    
    def bitwise_or(self, a, b):
        """Bitwise OR
        
        0 OR 0 = 0
        0 OR 1 = 1
        1 OR 0 = 1
        1 OR 1 = 1
        """
        self.last_result = a | b
        return self.last_result
    
    def bitwise_xor(self, a, b):
        """Bitwise XOR
        
        0 XOR 0 = 0
        0 XOR 1 = 1
        1 XOR 0 = 1
        1 XOR 1 = 0
        """
        self.last_result = a ^ b
        return self.last_result
    
    def bitwise_not(self, a, mask=0xFFFFFFFF):
        """Bitwise NOT (inversion)"""
        self.last_result = (~a) & mask
        return self.last_result
    
    def shift_left(self, value, count):
        """Sola sürüşdürmə (Shift Left)
        
        Nümunə: 0000 1000 << 1 = 0001 0000
        """
        self.last_result = (value << count) & 0xFFFFFFFF
        return self.last_result
    
    def shift_right(self, value, count):
        """Sağa sürüşdürmə (Shift Right)
        
        Nümunə: 0001 0000 >> 1 = 0000 1000
        """
        self.last_result = value >> count
        return self.last_result
    
    def rotate_left(self, value, count, bits=32):
        """Sola fırlatma (Rotate Left)"""
        count = count % bits
        mask = (1 << bits) - 1
        value = value & mask
        self.last_result = ((value << count) | (value >> (bits - count))) & mask
        return self.last_result
    
    def rotate_right(self, value, count, bits=32):
        """Sağa fırlatma (Rotate Right)"""
        count = count % bits
        mask = (1 << bits) - 1
        value = value & mask
        self.last_result = ((value >> count) | (value << (bits - count))) & mask
        return self.last_result
    
    def compare(self, a, b):
        """Müqayisə et
        
        Qaytarır:
            -1: a < b
             0: a == b
             1: a > b
        """
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    
    def increment(self, value, mask=0xFFFFFFFF):
        """Artır (INC)"""
        self.last_result = (value + 1) & mask
        return self.last_result
    
    def decrement(self, value, mask=0xFFFFFFFF):
        """Azalt (DEC)"""
        self.last_result = (value - 1) & mask
        return self.last_result
    
    def negate(self, value, mask=0xFFFFFFFF):
        """Mənfi et (NEG) - Two's complement"""
        self.last_result = ((~value) + 1) & mask
        return self.last_result
    
    def sign_extend(self, value, from_bits, to_bits):
        """İşarə genişləndirmə"""
        sign_bit = 1 << (from_bits - 1)
        if value & sign_bit:
            # Mənfi ədəd
            mask = (1 << to_bits) - 1
            extension = mask ^ ((1 << from_bits) - 1)
            return value | extension
        return value
    
    def full_adder(self, a, b, carry_in):
        """Tam toplayıcı (1-bit)
        
        Transistor səviyyəsi əməliyyat:
        Sum = A XOR B XOR Cin
        Cout = (A AND B) OR (Cin AND (A XOR B))
        """
        sum_bit = (a ^ b ^ carry_in) & 1
        carry_out = ((a & b) | (carry_in & (a ^ b))) & 1
        return sum_bit, carry_out
    
    def ripple_carry_adder(self, a, b, bits=8):
        """Dalğavari daşıma toplayıcısı (çox bitli)"""
        result = 0
        carry = 0
        
        for i in range(bits):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            sum_bit, carry = self.full_adder(bit_a, bit_b, carry)
            result |= (sum_bit << i)
        
        self.last_result = result
        self.carry = carry
        return result, carry
    
    def _check_overflow_add(self, a, b, result, mask):
        """Overflow yoxla (işarəli toplama üçün)"""
        msb = (mask + 1) >> 1
        sign_a = 1 if a & msb else 0
        sign_b = 1 if b & msb else 0
        sign_result = 1 if result & msb else 0
        return 1 if (sign_a == sign_b) and (sign_a != sign_result) else 0


def binary_to_decimal(binary_str):
    """İkilik sistemi onluğa çevir"""
    return int(binary_str, 2)


def decimal_to_binary(decimal, bits=32):
    """Onluq sistemi ikiliyə çevir"""
    return format(decimal & ((1 << bits) - 1), f'0{bits}b')


def print_binary_operation(a, b, result, operation):
    """İkilik əməliyyatı vizuallaşdır"""
    print(f"\n{operation} əməliyyatı:")
    print(f"  A: {a:8d} = {decimal_to_binary(a, 8)}")
    print(f"  B: {b:8d} = {decimal_to_binary(b, 8)}")
    print(f"  ─────────────────────────────────")
    print(f"  R: {result:8d} = {decimal_to_binary(result, 8)}")


if __name__ == "__main__":
    # ALU test
    print("="*60)
    print("ALU (Arithmetic Logic Unit) Test")
    print("="*60)
    
    alu = ALU()
    
    # Toplama
    result = alu.add(5, 3)
    print_binary_operation(5, 3, result, "ADD")
    
    # Çıxma
    result = alu.subtract(10, 4)
    print_binary_operation(10, 4, result, "SUB")
    
    # Sola sürüşdürmə
    result = alu.shift_left(8, 1)
    print(f"\nSHL 8, 1 = {result}")
    print(f"  {decimal_to_binary(8, 8)} << 1 = {decimal_to_binary(result, 8)}")
    
    # AND əməliyyatı
    result = alu.bitwise_and(0b11110000, 0b10101010)
    print_binary_operation(0b11110000, 0b10101010, result, "AND")
