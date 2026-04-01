"""
Python və C++ İnteqrasiya - Əsas Fayl
=====================================
Bu fayl C++ modulu ilə işləmək üçün nümunələr göstərir.
"""

import sys
import os

# Build qovluğunu path-a əlavə et
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'build'))

try:
    import calculator
    CPP_AVAILABLE = True
except ImportError:
    print("⚠️  C++ modulu tapılmadı. Əvvəlcə kompilyasiya edin.")
    CPP_AVAILABLE = False

import numpy as np
from utils import Timer, print_separator


def demo_basic_operations():
    """Əsas hesablama əməliyyatları"""
    print_separator("Əsas Hesablama Əməliyyatları")
    
    if not CPP_AVAILABLE:
        print("C++ modulu mövcud deyil!")
        return
    
    # Toplama
    a, b = 15, 7
    result = calculator.add(a, b)
    print(f"  {a} + {b} = {result}")
    
    # Çıxma
    result = calculator.subtract(a, b)
    print(f"  {a} - {b} = {result}")
    
    # Vurma
    x, y = 4.5, 3.2
    result = calculator.multiply(x, y)
    print(f"  {x} × {y} = {result}")
    
    # Bölmə
    result = calculator.divide(x, y)
    print(f"  {x} ÷ {y} = {result:.4f}")


def demo_array_operations():
    """Massiv əməliyyatları"""
    print_separator("Massiv Əməliyyatları")
    
    if not CPP_AVAILABLE:
        print("C++ modulu mövcud deyil!")
        return
    
    # NumPy massivi yarat
    arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    print(f"  Orijinal massiv: {arr}")
    
    # Massivi işlə (hər elementi 2-yə vur)
    processed = calculator.process_array(arr)
    print(f"  İşlənmiş massiv: {processed}")
    
    # Cəm
    total = calculator.array_sum(arr)
    print(f"  Cəm: {total}")
    
    # Orta
    avg = calculator.array_average(arr)
    print(f"  Orta: {avg}")


def demo_math_functions():
    """Riyazi funksiyalar"""
    print_separator("Riyazi Funksiyalar")
    
    if not CPP_AVAILABLE:
        print("C++ modulu mövcud deyil!")
        return
    
    # Faktorial
    n = 10
    result = calculator.factorial(n)
    print(f"  {n}! = {result}")
    
    # Fibonacci
    print("  Fibonacci ardıcıllığı (ilk 15):")
    fib_seq = [calculator.fibonacci(i) for i in range(15)]
    print(f"    {fib_seq}")
    
    # Sadə ədədlər
    print("  100-ə qədər sadə ədədlər:")
    primes = [i for i in range(2, 100) if calculator.is_prime(i)]
    print(f"    {primes}")


def demo_performance():
    """Performans müqayisəsi"""
    print_separator("Performans Müqayisəsi")
    
    if not CPP_AVAILABLE:
        print("C++ modulu mövcud deyil!")
        return
    
    # Python faktorial
    def py_factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    n = 20
    iterations = 100000
    
    # Python ilə
    with Timer("Python faktorial"):
        for _ in range(iterations):
            py_factorial(n)
    
    # C++ ilə
    with Timer("C++ faktorial"):
        for _ in range(iterations):
            calculator.factorial(n)
    
    # Böyük massiv testi
    print("\n  Böyük massiv testi (1,000,000 element):")
    large_arr = np.random.rand(1_000_000)
    
    with Timer("NumPy sum"):
        np.sum(large_arr)
    
    with Timer("C++ array_sum"):
        calculator.array_sum(large_arr)


def main():
    """Əsas funksiya"""
    print("\n" + "=" * 50)
    print("  Python + C++ İnteqrasiya Demo")
    print("=" * 50 + "\n")
    
    demo_basic_operations()
    demo_array_operations()
    demo_math_functions()
    demo_performance()
    
    print("\n" + "=" * 50)
    print("  Demo tamamlandı!")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
