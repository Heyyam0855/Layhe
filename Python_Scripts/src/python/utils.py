"""
Köməkçi Funksiyalar
===================
Layihə üçün ümumi köməkçi funksiyalar və siniflər.
"""

import time
from contextlib import contextmanager
from typing import Any, Callable, List
import functools


class Timer:
    """
    Kod blokunun icra müddətini ölçmək üçün kontekst meneceri.
    
    İstifadə:
        with Timer("Əməliyyat adı"):
            # kod
    """
    
    def __init__(self, name: str = "Əməliyyat"):
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        self.end_time = time.perf_counter()
        elapsed = self.end_time - self.start_time
        print(f"    ⏱️  {self.name}: {elapsed:.6f} saniyə")
    
    @property
    def elapsed(self) -> float:
        """Keçən vaxt (saniyə)"""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0.0


def print_separator(title: str, char: str = "-", width: int = 50):
    """
    Başlıq ilə ayırıcı xətt çap et.
    
    Args:
        title: Başlıq mətni
        char: Ayırıcı simvol
        width: Xəttin eni
    """
    print(f"\n{char * width}")
    print(f"  📌 {title}")
    print(f"{char * width}")


def measure_time(func: Callable) -> Callable:
    """
    Funksiyanın icra müddətini ölçən dekorator.
    
    İstifadə:
        @measure_time
        def my_function():
            ...
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️  {func.__name__}: {end - start:.6f} saniyə")
        return result
    return wrapper


def compare_performance(funcs: List[Callable], args: tuple = (), 
                        iterations: int = 1000, names: List[str] = None):
    """
    Bir neçə funksiyanın performansını müqayisə et.
    
    Args:
        funcs: Müqayisə ediləcək funksiyalar
        args: Funksiyalara verilən arqumentlər
        iterations: Təkrar sayı
        names: Funksiya adları (optional)
    
    Returns:
        dict: Funksiya adları və icra müddətləri
    """
    results = {}
    
    if names is None:
        names = [f.__name__ for f in funcs]
    
    print_separator("Performans Müqayisəsi")
    
    for func, name in zip(funcs, names):
        start = time.perf_counter()
        for _ in range(iterations):
            func(*args)
        end = time.perf_counter()
        
        elapsed = end - start
        results[name] = elapsed
        print(f"  {name}: {elapsed:.6f} saniyə ({iterations} təkrar)")
    
    # Ən sürətlini tap
    fastest = min(results, key=results.get)
    print(f"\n  🏆 Ən sürətli: {fastest}")
    
    return results


def validate_positive(value: Any, name: str = "Dəyər"):
    """
    Dəyərin müsbət olduğunu yoxla.
    
    Args:
        value: Yoxlanılacaq dəyər
        name: Dəyərin adı (xəta mesajı üçün)
    
    Raises:
        ValueError: Dəyər müsbət deyilsə
    """
    if value <= 0:
        raise ValueError(f"{name} müsbət olmalıdır, verilən: {value}")


def validate_non_negative(value: Any, name: str = "Dəyər"):
    """
    Dəyərin mənfi olmadığını yoxla.
    
    Args:
        value: Yoxlanılacaq dəyər
        name: Dəyərin adı (xəta mesajı üçün)
    
    Raises:
        ValueError: Dəyər mənfidirsə
    """
    if value < 0:
        raise ValueError(f"{name} mənfi ola bilməz, verilən: {value}")


def format_number(num: float, precision: int = 2) -> str:
    """
    Ədədi oxunaqlı formata çevir.
    
    Args:
        num: Formatlanacaq ədəd
        precision: Onluq dəqiqliyi
    
    Returns:
        str: Formatlanmış ədəd
    """
    if abs(num) >= 1_000_000_000:
        return f"{num / 1_000_000_000:.{precision}f}B"
    elif abs(num) >= 1_000_000:
        return f"{num / 1_000_000:.{precision}f}M"
    elif abs(num) >= 1_000:
        return f"{num / 1_000:.{precision}f}K"
    else:
        return f"{num:.{precision}f}"


class ProgressBar:
    """
    Sadə progress bar.
    
    İstifadə:
        pb = ProgressBar(100)
        for i in range(100):
            pb.update(i + 1)
    """
    
    def __init__(self, total: int, width: int = 40, prefix: str = "İrəliləyiş"):
        self.total = total
        self.width = width
        self.prefix = prefix
    
    def update(self, current: int):
        """Progress bar-ı yenilə"""
        percent = current / self.total
        filled = int(self.width * percent)
        bar = "█" * filled + "░" * (self.width - filled)
        print(f"\r{self.prefix}: |{bar}| {percent*100:.1f}%", end="", flush=True)
        
        if current >= self.total:
            print()  # Yeni sətir
