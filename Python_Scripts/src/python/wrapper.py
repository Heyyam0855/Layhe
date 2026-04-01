"""
C++ Wrapper Modulu
==================
C++ funksiyalarını Python-friendly şəkildə təqdim edir.
"""

import sys
import os
from typing import List, Union, Optional
import numpy as np

# Build qovluğunu path-a əlavə et
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'build'))

try:
    import calculator as _cpp
    CPP_AVAILABLE = True
except ImportError:
    CPP_AVAILABLE = False
    print("⚠️  C++ modulu yüklənmədi. Python implementasiyası istifadə olunacaq.")


class Calculator:
    """
    C++ hesablama modulunun Python wrapper-i.
    C++ mövcud deyilsə, Python implementasiyasına keçir.
    """
    
    @staticmethod
    def add(a: int, b: int) -> int:
        """İki tam ədədi topla"""
        if CPP_AVAILABLE:
            return _cpp.add(a, b)
        return a + b
    
    @staticmethod
    def subtract(a: int, b: int) -> int:
        """İki tam ədədi çıx"""
        if CPP_AVAILABLE:
            return _cpp.subtract(a, b)
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """İki ədədi vur"""
        if CPP_AVAILABLE:
            return _cpp.multiply(a, b)
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """İki ədədi böl"""
        if b == 0:
            raise ValueError("Sıfıra bölmək olmaz!")
        if CPP_AVAILABLE:
            return _cpp.divide(a, b)
        return a / b


class ArrayProcessor:
    """
    Massiv əməliyyatları üçün wrapper.
    """
    
    @staticmethod
    def process(arr: Union[List[float], np.ndarray]) -> np.ndarray:
        """Massivin hər elementini 2-yə vur"""
        arr = np.asarray(arr, dtype=np.float64)
        if CPP_AVAILABLE:
            return _cpp.process_array(arr)
        return arr * 2
    
    @staticmethod
    def sum(arr: Union[List[float], np.ndarray]) -> float:
        """Massiv elementlərinin cəmi"""
        arr = np.asarray(arr, dtype=np.float64)
        if CPP_AVAILABLE:
            return _cpp.array_sum(arr)
        return np.sum(arr)
    
    @staticmethod
    def average(arr: Union[List[float], np.ndarray]) -> float:
        """Massiv elementlərinin orta qiyməti"""
        arr = np.asarray(arr, dtype=np.float64)
        if len(arr) == 0:
            raise ValueError("Boş massiv!")
        if CPP_AVAILABLE:
            return _cpp.array_average(arr)
        return np.mean(arr)
    
    @staticmethod
    def min(arr: Union[List[float], np.ndarray]) -> float:
        """Massivin minimum elementi"""
        arr = np.asarray(arr, dtype=np.float64)
        return np.min(arr)
    
    @staticmethod
    def max(arr: Union[List[float], np.ndarray]) -> float:
        """Massivin maksimum elementi"""
        arr = np.asarray(arr, dtype=np.float64)
        return np.max(arr)


class MathFunctions:
    """
    Riyazi funksiyalar üçün wrapper.
    """
    
    @staticmethod
    def factorial(n: int) -> int:
        """n! hesabla"""
        if n < 0:
            raise ValueError("Mənfi ədədin faktorialı yoxdur!")
        if CPP_AVAILABLE:
            return _cpp.factorial(n)
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """n-ci Fibonacci ədədini tap"""
        if n < 0:
            raise ValueError("Mənfi indeks!")
        if CPP_AVAILABLE:
            return _cpp.fibonacci(n)
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def fibonacci_sequence(n: int) -> List[int]:
        """İlk n Fibonacci ədədini qaytarır"""
        return [MathFunctions.fibonacci(i) for i in range(n)]
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Ədədin sadə olub-olmadığını yoxla"""
        if CPP_AVAILABLE:
            return _cpp.is_prime(n)
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    @staticmethod
    def primes_up_to(n: int) -> List[int]:
        """n-ə qədər bütün sadə ədədləri tap"""
        return [i for i in range(2, n + 1) if MathFunctions.is_prime(i)]
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Ən böyük ortaq bölən"""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Ən kiçik ortaq bölünən"""
        return abs(a * b) // MathFunctions.gcd(a, b)


def is_cpp_available() -> bool:
    """C++ modulunun mövcud olub-olmadığını yoxla"""
    return CPP_AVAILABLE


def get_version() -> str:
    """Modul versiyasını qaytarır"""
    return "1.0.0"


# Modul yükləndikdə məlumat ver
if __name__ == "__main__":
    print(f"Calculator Wrapper v{get_version()}")
    print(f"C++ modulu: {'Mövcud ✅' if CPP_AVAILABLE else 'Mövcud deyil ❌'}")
    
    # Test
    calc = Calculator()
    print(f"\nTest: 5 + 3 = {calc.add(5, 3)}")
    
    math_funcs = MathFunctions()
    print(f"Test: 10! = {math_funcs.factorial(10)}")
    print(f"Test: Fib(10) = {math_funcs.fibonacci(10)}")
