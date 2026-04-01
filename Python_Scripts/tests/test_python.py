"""
Python Unit Testləri
====================
calculator modulu və wrapper üçün testlər
"""

import pytest
import sys
import os
import numpy as np

# Layihə yollarını əlavə et
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'python'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))

from wrapper import Calculator, ArrayProcessor, MathFunctions, is_cpp_available


class TestCalculator:
    """Calculator sinfi üçün testlər"""
    
    def test_add_positive(self):
        """Müsbət ədədlərin toplanması"""
        assert Calculator.add(5, 3) == 8
        assert Calculator.add(100, 200) == 300
        assert Calculator.add(0, 0) == 0
    
    def test_add_negative(self):
        """Mənfi ədədlərlə toplama"""
        assert Calculator.add(-5, -3) == -8
        assert Calculator.add(5, -3) == 2
        assert Calculator.add(-5, 3) == -2
    
    def test_subtract(self):
        """Çıxma əməliyyatı"""
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(3, 5) == -2
        assert Calculator.subtract(5, 5) == 0
    
    def test_multiply(self):
        """Vurma əməliyyatı"""
        assert Calculator.multiply(5.0, 3.0) == pytest.approx(15.0)
        assert Calculator.multiply(-5.0, 3.0) == pytest.approx(-15.0)
        assert Calculator.multiply(0.0, 100.0) == pytest.approx(0.0)
    
    def test_divide(self):
        """Bölmə əməliyyatı"""
        assert Calculator.divide(6.0, 2.0) == pytest.approx(3.0)
        assert Calculator.divide(-6.0, 2.0) == pytest.approx(-3.0)
        assert Calculator.divide(5.0, 2.0) == pytest.approx(2.5)
    
    def test_divide_by_zero(self):
        """Sıfıra bölmə xətası"""
        with pytest.raises(ValueError):
            Calculator.divide(5.0, 0.0)


class TestArrayProcessor:
    """ArrayProcessor sinfi üçün testlər"""
    
    def test_process(self):
        """Massivi işləmə"""
        arr = [1.0, 2.0, 3.0]
        result = ArrayProcessor.process(arr)
        expected = np.array([2.0, 4.0, 6.0])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_sum(self):
        """Massiv cəmi"""
        arr = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert ArrayProcessor.sum(arr) == pytest.approx(15.0)
    
    def test_average(self):
        """Massiv ortası"""
        arr = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert ArrayProcessor.average(arr) == pytest.approx(3.0)
    
    def test_average_empty(self):
        """Boş massiv xətası"""
        with pytest.raises(ValueError):
            ArrayProcessor.average([])
    
    def test_min_max(self):
        """Minimum və maksimum"""
        arr = [3.0, 1.0, 4.0, 1.0, 5.0, 9.0, 2.0]
        assert ArrayProcessor.min(arr) == pytest.approx(1.0)
        assert ArrayProcessor.max(arr) == pytest.approx(9.0)
    
    def test_numpy_array(self):
        """NumPy massivi ilə işləmə"""
        arr = np.array([1.0, 2.0, 3.0])
        result = ArrayProcessor.process(arr)
        assert isinstance(result, np.ndarray)


class TestMathFunctions:
    """MathFunctions sinfi üçün testlər"""
    
    def test_factorial(self):
        """Faktorial hesablama"""
        assert MathFunctions.factorial(0) == 1
        assert MathFunctions.factorial(1) == 1
        assert MathFunctions.factorial(5) == 120
        assert MathFunctions.factorial(10) == 3628800
    
    def test_factorial_negative(self):
        """Mənfi faktorial xətası"""
        with pytest.raises(ValueError):
            MathFunctions.factorial(-1)
    
    def test_fibonacci(self):
        """Fibonacci ədədləri"""
        assert MathFunctions.fibonacci(0) == 0
        assert MathFunctions.fibonacci(1) == 1
        assert MathFunctions.fibonacci(2) == 1
        assert MathFunctions.fibonacci(10) == 55
        assert MathFunctions.fibonacci(12) == 144
    
    def test_fibonacci_negative(self):
        """Mənfi Fibonacci indeksi xətası"""
        with pytest.raises(ValueError):
            MathFunctions.fibonacci(-1)
    
    def test_fibonacci_sequence(self):
        """Fibonacci ardıcıllığı"""
        seq = MathFunctions.fibonacci_sequence(8)
        assert seq == [0, 1, 1, 2, 3, 5, 8, 13]
    
    def test_is_prime(self):
        """Sadə ədəd yoxlaması"""
        assert MathFunctions.is_prime(2) == True
        assert MathFunctions.is_prime(3) == True
        assert MathFunctions.is_prime(4) == False
        assert MathFunctions.is_prime(5) == True
        assert MathFunctions.is_prime(97) == True
        assert MathFunctions.is_prime(100) == False
    
    def test_is_prime_edge_cases(self):
        """Sadə ədəd - kənar hallar"""
        assert MathFunctions.is_prime(0) == False
        assert MathFunctions.is_prime(1) == False
        assert MathFunctions.is_prime(-5) == False
    
    def test_primes_up_to(self):
        """Müəyyən ədədə qədər sadə ədədlər"""
        primes = MathFunctions.primes_up_to(20)
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
    
    def test_gcd(self):
        """Ən böyük ortaq bölən"""
        assert MathFunctions.gcd(12, 8) == 4
        assert MathFunctions.gcd(17, 13) == 1
        assert MathFunctions.gcd(100, 25) == 25
    
    def test_lcm(self):
        """Ən kiçik ortaq bölünən"""
        assert MathFunctions.lcm(4, 6) == 12
        assert MathFunctions.lcm(3, 5) == 15
        assert MathFunctions.lcm(12, 18) == 36


class TestIntegration:
    """İnteqrasiya testləri"""
    
    def test_cpp_availability(self):
        """C++ modulu yoxlaması"""
        # Bu test sadəcə funksiyanın işlədiyini yoxlayır
        result = is_cpp_available()
        assert isinstance(result, bool)
    
    def test_large_array(self):
        """Böyük massiv testi"""
        arr = np.random.rand(10000)
        total = ArrayProcessor.sum(arr)
        assert total > 0
    
    def test_combined_operations(self):
        """Birləşdirilmiş əməliyyatlar"""
        # Faktorialları topla
        factorials = [MathFunctions.factorial(i) for i in range(6)]
        total = sum(factorials)  # 1 + 1 + 2 + 6 + 24 + 120 = 154
        assert total == 154


# Performans testləri (markers ilə)
@pytest.mark.performance
class TestPerformance:
    """Performans testləri"""
    
    def test_factorial_speed(self):
        """Faktorial sürəti"""
        import time
        start = time.perf_counter()
        for _ in range(10000):
            MathFunctions.factorial(20)
        elapsed = time.perf_counter() - start
        assert elapsed < 1.0  # 1 saniyədən az olmalı
    
    def test_fibonacci_speed(self):
        """Fibonacci sürəti"""
        import time
        start = time.perf_counter()
        for _ in range(10000):
            MathFunctions.fibonacci(30)
        elapsed = time.perf_counter() - start
        assert elapsed < 1.0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
