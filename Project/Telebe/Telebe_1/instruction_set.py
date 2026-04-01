"""
CPU ƏMRİ SETİ - x86 assembly əmrlərinin Python tətbiqi
Her əmr üçün opcode, format və izahlar
"""

class Instruction:
    """Tək bir CPU əmrini təmsil edir"""
    
    def __init__(self, mnemonic, opcode, operands, description):
        self.mnemonic = mnemonic      # Əmrin adı (MOV, ADD, vs.)
        self.opcode = opcode           # Maşın kodu (HEX)
        self.operands = operands       # Operandlar
        self.description = description # İzah
    
    def __str__(self):
        return f"{self.mnemonic} {', '.join(map(str, self.operands))}"
    
    def to_binary(self):
        """Əmri ikili kodda göstər"""
        return bin(int(self.opcode, 16))[2:].zfill(8)


class InstructionSet:
    """x86 əmr seti"""
    
    # Əmr kateqoriyaları
    DATA_TRANSFER = "Data Transfer"    # Məlumat köçürmə
    ARITHMETIC = "Arithmetic"           # Arifmetik
    LOGIC = "Logic"                     # Məntiqi
    SHIFT = "Shift/Rotate"             # Sürüşdürmə
    CONTROL = "Control Flow"            # İdarəetmə axını
    
    def __init__(self):
        self.instructions = {
            # ═══════════════════════════════════════════════
            # MƏLUMAT KÖÇÜRMƏ (Data Transfer)
            # ═══════════════════════════════════════════════
            'MOV': {
                'category': self.DATA_TRANSFER,
                'opcode': 'B8',  # MOV EAX, imm32
                'format': 'MOV dest, src',
                'description': 'Məlumatı köçür (src → dest)',
                'example': 'MOV EAX, 5',
                'binary_example': '10111000 00000101 00000000 00000000 00000000'
            },
            
            'PUSH': {
                'category': self.DATA_TRANSFER,
                'opcode': '50',  # PUSH EAX
                'format': 'PUSH src',
                'description': 'Stackə dəyər əlavə et',
                'example': 'PUSH EAX',
                'binary_example': '01010000'
            },
            
            'POP': {
                'category': self.DATA_TRANSFER,
                'opcode': '58',  # POP EAX
                'format': 'POP dest',
                'description': 'Stackdən dəyər çıxart',
                'example': 'POP EAX',
                'binary_example': '01011000'
            },
            
            # ═══════════════════════════════════════════════
            # ARİFMETİK ƏMƏLLAR (Arithmetic)
            # ═══════════════════════════════════════════════
            'ADD': {
                'category': self.ARITHMETIC,
                'opcode': '01',  # ADD reg, reg
                'format': 'ADD dest, src',
                'description': 'Toplama (dest = dest + src)',
                'example': 'ADD EAX, EBX',
                'binary_example': '00000001 11011000',
                'microcode': [
                    'μOp1: READ_REG   tmp0, dest',
                    'μOp2: READ_REG   tmp1, src',
                    'μOp3: ALU_ADD    tmp2, tmp0, tmp1',
                    'μOp4: WRITE_REG  dest, tmp2',
                    'μOp5: UPDATE_FLAGS'
                ]
            },
            
            'SUB': {
                'category': self.ARITHMETIC,
                'opcode': '29',
                'format': 'SUB dest, src',
                'description': 'Çıxma (dest = dest - src)',
                'example': 'SUB EAX, 3',
                'binary_example': '00101001'
            },
            
            'MUL': {
                'category': self.ARITHMETIC,
                'opcode': 'F7',
                'format': 'MUL src',
                'description': 'İşarəsiz vurma (EAX * src)',
                'example': 'MUL EBX',
                'binary_example': '11110111'
            },
            
            'DIV': {
                'category': self.ARITHMETIC,
                'opcode': 'F7',
                'format': 'DIV src',
                'description': 'İşarəsiz bölmə (EDX:EAX / src)',
                'example': 'DIV EBX',
                'binary_example': '11110111'
            },
            
            'INC': {
                'category': self.ARITHMETIC,
                'opcode': '40',  # INC EAX
                'format': 'INC dest',
                'description': 'Artır (dest = dest + 1)',
                'example': 'INC EAX',
                'binary_example': '01000000'
            },
            
            'DEC': {
                'category': self.ARITHMETIC,
                'opcode': '48',  # DEC EAX
                'format': 'DEC dest',
                'description': 'Azalt (dest = dest - 1)',
                'example': 'DEC EAX',
                'binary_example': '01001000'
            },
            
            # ═══════════════════════════════════════════════
            # MƏNTİQİ ƏMƏLLAR (Logic)
            # ═══════════════════════════════════════════════
            'AND': {
                'category': self.LOGIC,
                'opcode': '21',
                'format': 'AND dest, src',
                'description': 'Bitwise AND',
                'example': 'AND EAX, EBX',
                'binary_example': '00100001 11011000'
            },
            
            'OR': {
                'category': self.LOGIC,
                'opcode': '09',
                'format': 'OR dest, src',
                'description': 'Bitwise OR',
                'example': 'OR EAX, EBX',
                'binary_example': '00001001 11011000'
            },
            
            'XOR': {
                'category': self.LOGIC,
                'opcode': '31',
                'format': 'XOR dest, src',
                'description': 'Bitwise XOR',
                'example': 'XOR EAX, EBX',
                'binary_example': '00110001 11011000'
            },
            
            'NOT': {
                'category': self.LOGIC,
                'opcode': 'F7',
                'format': 'NOT dest',
                'description': 'Bitwise NOT (invert)',
                'example': 'NOT EAX',
                'binary_example': '11110111'
            },
            
            # ═══════════════════════════════════════════════
            # SÜRÜŞDÜRMƏ (Shift/Rotate)
            # ═══════════════════════════════════════════════
            'SHL': {
                'category': self.SHIFT,
                'opcode': 'D1',  # SHL reg, 1
                'format': 'SHL dest, count',
                'description': 'Sola sürüşdür (shift left)',
                'example': 'SHL EAX, 1',
                'binary_example': '11010001 11100000'
            },
            
            'SHR': {
                'category': self.SHIFT,
                'opcode': 'D1',
                'format': 'SHR dest, count',
                'description': 'Sağa sürüşdür (shift right)',
                'example': 'SHR EAX, 1',
                'binary_example': '11010001 11101000'
            },
            
            'ROL': {
                'category': self.SHIFT,
                'opcode': 'D1',
                'format': 'ROL dest, count',
                'description': 'Sola fırlat (rotate left)',
                'example': 'ROL EAX, 1',
                'binary_example': '11010001 11000000'
            },
            
            'ROR': {
                'category': self.SHIFT,
                'opcode': 'D1',
                'format': 'ROR dest, count',
                'description': 'Sağa fırlat (rotate right)',
                'example': 'ROR EAX, 1',
                'binary_example': '11010001 11001000'
            },
            
            # ═══════════════════════════════════════════════
            # İDARƏETMƏ AXINI (Control Flow)
            # ═══════════════════════════════════════════════
            'CMP': {
                'category': self.CONTROL,
                'opcode': '3D',  # CMP EAX, imm32
                'format': 'CMP op1, op2',
                'description': 'Müqayisə et (op1 - op2)',
                'example': 'CMP EAX, 16',
                'binary_example': '00111101 00010000'
            },
            
            'JMP': {
                'category': self.CONTROL,
                'opcode': 'EB',  # JMP short
                'format': 'JMP target',
                'description': 'Şərtsiz keçid',
                'example': 'JMP label',
                'binary_example': '11101011'
            },
            
            'JE': {
                'category': self.CONTROL,
                'opcode': '74',
                'format': 'JE target',
                'description': 'Bərabərdirsə keç (ZF=1)',
                'example': 'JE equal',
                'binary_example': '01110100'
            },
            
            'JNE': {
                'category': self.CONTROL,
                'opcode': '75',
                'format': 'JNE target',
                'description': 'Bərabər deyilsə keç (ZF=0)',
                'example': 'JNE not_equal',
                'binary_example': '01110101'
            },
            
            'JG': {
                'category': self.CONTROL,
                'opcode': '7F',
                'format': 'JG target',
                'description': 'Böyükdürsə keç (işarəli)',
                'example': 'JG greater',
                'binary_example': '01111111'
            },
            
            'JL': {
                'category': self.CONTROL,
                'opcode': '7C',
                'format': 'JL target',
                'description': 'Kiçikdirsə keç (işarəli)',
                'example': 'JL less',
                'binary_example': '01111100'
            },
            
            'CALL': {
                'category': self.CONTROL,
                'opcode': 'E8',
                'format': 'CALL target',
                'description': 'Funksiyanı çağır',
                'example': 'CALL function',
                'binary_example': '11101000'
            },
            
            'RET': {
                'category': self.CONTROL,
                'opcode': 'C3',
                'format': 'RET',
                'description': 'Funksiyadan çıx',
                'example': 'RET',
                'binary_example': '11000011'
            },
            
            'NOP': {
                'category': self.CONTROL,
                'opcode': '90',
                'format': 'NOP',
                'description': 'Heç nə etmə (No Operation)',
                'example': 'NOP',
                'binary_example': '10010000'
            },
            
            'INT': {
                'category': self.CONTROL,
                'opcode': 'CD',
                'format': 'INT vector',
                'description': 'Interrupt - sistem çağırışı',
                'example': 'INT 0x80',
                'binary_example': '11001101 10000000'
            }
        }
    
    def get_instruction(self, mnemonic):
        """Əmr məlumatını al"""
        return self.instructions.get(mnemonic.upper())
    
    def list_by_category(self, category):
        """Kateqoriya üzrə əmrləri göstər"""
        result = []
        for name, info in self.instructions.items():
            if info['category'] == category:
                result.append((name, info))
        return result
    
    def print_instruction_info(self, mnemonic):
        """Əmr haqqında tam məlumat"""
        info = self.get_instruction(mnemonic)
        if not info:
            print(f"❌ '{mnemonic}' əmri tapılmadı!")
            return
        
        print("\n" + "="*60)
        print(f"📋 ƏMR: {mnemonic}")
        print("="*60)
        print(f"Kateqoriya:  {info['category']}")
        print(f"Opcode:      0x{info['opcode']}")
        print(f"Format:      {info['format']}")
        print(f"İzah:        {info['description']}")
        print(f"Nümunə:      {info['example']}")
        print(f"İkili kod:   {info['binary_example']}")
        
        if 'microcode' in info:
            print("\nMikrokod:")
            for uop in info['microcode']:
                print(f"  {uop}")
        print("="*60)
    
    def print_all_instructions(self):
        """Bütün əmrləri göstər"""
        categories = [
            self.DATA_TRANSFER,
            self.ARITHMETIC,
            self.LOGIC,
            self.SHIFT,
            self.CONTROL
        ]
        
        for category in categories:
            print(f"\n{'='*60}")
            print(f"📦 {category.upper()}")
            print('='*60)
            
            instructions = self.list_by_category(category)
            for name, info in instructions:
                print(f"  {name:8s} - {info['description']}")


if __name__ == "__main__":
    # Test
    iset = InstructionSet()
    
    # Bütün əmrləri göstər
    iset.print_all_instructions()
    
    # Konkret əmr haqqında məlumat
    print("\n")
    iset.print_instruction_info('ADD')
    iset.print_instruction_info('SHL')
    iset.print_instruction_info('JE')
