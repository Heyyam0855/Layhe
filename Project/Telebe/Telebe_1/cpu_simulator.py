"""
CPU NÜVƏSİ SİMULYATORU - Python ilə
x86 Assembly əməliyyatlarını simulyasiya edir
"""

class CPUSimulator:
    """CPU simulyatoru - registrlər, yaddaş və əmrləri idarə edir"""
    
    def __init__(self):
        # 32-bit registrlər (x86 arxitekturası)
        self.registers = {
            'EAX': 0,
            'EBX': 0,
            'ECX': 0,
            'EDX': 0,
            'ESI': 0,
            'EDI': 0,
            'EBP': 0,
            'ESP': 0
        }
        
        # Bayraqlar (Flags)
        self.flags = {
            'CF': 0,  # Carry Flag
            'ZF': 0,  # Zero Flag
            'SF': 0,  # Sign Flag
            'OF': 0   # Overflow Flag
        }
        
        # Yaddaş (1MB simulyasiya)
        self.memory = [0] * (1024 * 1024)
        
        # Program Counter (Əmr göstəricisi)
        self.pc = 0
        
        # Əmr tarixi
        self.instruction_history = []
    
    def mov(self, dest, value):
        """MOV əmri - dəyər köçür"""
        if isinstance(value, str):
            # Registr-dan registr-ə
            self.registers[dest] = self.registers[value]
            opcode = f"MOV {dest}, {value}"
        else:
            # Birbaşa dəyər
            self.registers[dest] = value & 0xFFFFFFFF  # 32-bit mask
            opcode = f"MOV {dest}, {value}"
        
        self._log_instruction(opcode, self._int_to_binary(value if isinstance(value, int) else self.registers[value]))
        return self
    
    def add(self, dest, src):
        """ADD əmri - toplama"""
        if isinstance(src, str):
            value = self.registers[src]
            opcode = f"ADD {dest}, {src}"
        else:
            value = src
            opcode = f"ADD {dest}, {value}"
        
        old_value = self.registers[dest]
        result = (old_value + value) & 0xFFFFFFFF
        
        # Bayraqları yenilə
        self.flags['CF'] = 1 if (old_value + value) > 0xFFFFFFFF else 0
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        self.flags['OF'] = self._check_overflow_add(old_value, value, result)
        
        self.registers[dest] = result
        self._log_instruction(opcode, self._int_to_binary(result))
        return self
    
    def sub(self, dest, src):
        """SUB əmri - çıxma"""
        if isinstance(src, str):
            value = self.registers[src]
            opcode = f"SUB {dest}, {src}"
        else:
            value = src
            opcode = f"SUB {dest}, {value}"
        
        old_value = self.registers[dest]
        result = (old_value - value) & 0xFFFFFFFF
        
        self.flags['CF'] = 1 if value > old_value else 0
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        
        self.registers[dest] = result
        self._log_instruction(opcode, self._int_to_binary(result))
        return self
    
    def shl(self, dest, count=1):
        """SHL əmri - sola sürüşdürmə (bit shift left)"""
        old_value = self.registers[dest]
        result = (old_value << count) & 0xFFFFFFFF
        
        self.flags['CF'] = 1 if (old_value >> (32 - count)) & 1 else 0
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        
        self.registers[dest] = result
        self._log_instruction(f"SHL {dest}, {count}", self._int_to_binary(result))
        return self
    
    def shr(self, dest, count=1):
        """SHR əmri - sağa sürüşdürmə (bit shift right)"""
        old_value = self.registers[dest]
        result = old_value >> count
        
        self.flags['CF'] = (old_value >> (count - 1)) & 1
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        
        self.registers[dest] = result
        self._log_instruction(f"SHR {dest}, {count}", self._int_to_binary(result))
        return self
    
    def cmp(self, reg, value):
        """CMP əmri - müqayisə et (SUB kimi amma nəticəni saxlamır)"""
        if isinstance(value, str):
            cmp_value = self.registers[value]
        else:
            cmp_value = value
        
        reg_value = self.registers[reg]
        result = (reg_value - cmp_value) & 0xFFFFFFFF
        
        self.flags['CF'] = 1 if cmp_value > reg_value else 0
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        
        self._log_instruction(f"CMP {reg}, {value}", f"ZF={self.flags['ZF']}")
        return self
    
    def and_op(self, dest, src):
        """AND əmri - bitwise AND"""
        if isinstance(src, str):
            value = self.registers[src]
        else:
            value = src
        
        result = self.registers[dest] & value
        self.registers[dest] = result
        
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        
        self._log_instruction(f"AND {dest}, {src}", self._int_to_binary(result))
        return self
    
    def or_op(self, dest, src):
        """OR əmri - bitwise OR"""
        if isinstance(src, str):
            value = self.registers[src]
        else:
            value = src
        
        result = self.registers[dest] | value
        self.registers[dest] = result
        
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        
        self._log_instruction(f"OR {dest}, {src}", self._int_to_binary(result))
        return self
    
    def xor_op(self, dest, src):
        """XOR əmri - bitwise XOR"""
        if isinstance(src, str):
            value = self.registers[src]
        else:
            value = src
        
        result = self.registers[dest] ^ value
        self.registers[dest] = result
        
        self.flags['ZF'] = 1 if result == 0 else 0
        self.flags['SF'] = 1 if result & 0x80000000 else 0
        
        self._log_instruction(f"XOR {dest}, {src}", self._int_to_binary(result))
        return self
    
    def get_register(self, reg):
        """Registr dəyərini al"""
        return self.registers.get(reg, 0)
    
    def get_flags(self):
        """Bütün bayraqları al"""
        return self.flags.copy()
    
    def reset(self):
        """CPU-nu sıfırla"""
        for reg in self.registers:
            self.registers[reg] = 0
        for flag in self.flags:
            self.flags[flag] = 0
        self.instruction_history.clear()
        self.pc = 0
        return self
    
    def print_state(self):
        """CPU vəziyyətini göstər"""
        print("\n" + "="*60)
        print("CPU VƏZİYYƏTİ")
        print("="*60)
        print("\n📊 REGİSTRLƏR:")
        for reg, value in self.registers.items():
            binary = self._int_to_binary(value)
            print(f"  {reg}: {value:10d} | 0x{value:08X} | {binary}")
        
        print("\n🚩 BAYRAQLAR:")
        print(f"  CF={self.flags['CF']}  ZF={self.flags['ZF']}  "
              f"SF={self.flags['SF']}  OF={self.flags['OF']}")
        print("="*60)
    
    def print_history(self):
        """Əmr tarixini göstər"""
        print("\n" + "="*60)
        print("ƏMRLƏR TARİXİ")
        print("="*60)
        for i, (instr, detail) in enumerate(self.instruction_history, 1):
            print(f"{i:2d}. {instr:20s} → {detail}")
        print("="*60)
    
    def _log_instruction(self, instruction, detail):
        """Əmri qeyd et"""
        self.instruction_history.append((instruction, detail))
    
    def _int_to_binary(self, value):
        """Tam ədədi ikili sistemə çevir (32-bit)"""
        if isinstance(value, str):
            return value
        return f"{value & 0xFFFFFFFF:032b}"
    
    def _check_overflow_add(self, a, b, result):
        """Toplama üçün overflow yoxla"""
        sign_a = (a >> 31) & 1
        sign_b = (b >> 31) & 1
        sign_result = (result >> 31) & 1
        return 1 if (sign_a == sign_b) and (sign_a != sign_result) else 0
