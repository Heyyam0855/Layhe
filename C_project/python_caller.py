#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python <-> C İnteqrasiya Testi
ctypes istifadə edərək C shared library-ni çağırır
"""

import ctypes
import os
import sys

def main():
    print("=" * 50)
    print("  Python <-> C İnteqrasiya Testi")
    print("=" * 50)
    print()
    
    # DLL faylının yolunu təyin et
    dll_path = os.path.join(os.path.dirname(__file__), 'c_module', 'math_ops.dll')
    
    # Faylın mövcudluğunu yoxla
    if not os.path.exists(dll_path):
        print(f"❌ XƏTA: {dll_path} tapılmadı!")
        print()
        print("Əvvəlcə C modulunu kompil edin:")
        print("  gcc -shared -o c_module/math_ops.dll c_module/math_ops.c")
        print()
        sys.exit(1)
    
    try:
        # DLL-i yüklə
        lib = ctypes.CDLL(dll_path)
        print(f"✓ Library yükləndi: {dll_path}")
        print()
        
        # Funksiyanın arqument və return tiplərini təyin et
        lib.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
        lib.add_numbers.restype = ctypes.c_int
        
        # Test ədədləri
        num1 = 15
        num2 = 27
        
        # C funksiyasını çağır
        result = lib.add_numbers(num1, num2)
        
        # Nəticəni göstər
        print(f"Ədəd 1: {num1}")
        print(f"Ədəd 2: {num2}")
        print(f"Cəm: {num1} + {num2} = {result}")
        print()
        print("=" * 50)
        print("✓ C funksiyası uğurla çağırıldı!")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ XƏTA: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
