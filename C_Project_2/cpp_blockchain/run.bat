@echo off
REM C++ proqramını kompilyasiya edir və icra edir
REM Python-da "python main.py" kimi sadə istifadə

echo ============================================
echo C++ Blockchain Proqramı Kompilyasiya Edilir...
echo ============================================

REM Kompilyasiya
g++ -std=c++11 -Wall -Wextra -O2 -o blockchain.exe main.cpp Transaction.cpp Block.cpp Blockchain.cpp Wallet.cpp

REM Kompilyasiya uğurlu oldusa icra et
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================
    echo Kompilyasiya Uğurlu! Proqram İcra Olunur...
    echo ============================================
    echo.
    blockchain.exe
) else (
    echo.
    echo XETA: Kompilyasiya zamanı xəta baş verdi!
    echo GCC kompilyatorunun quraşdırıldığından əmin olun.
    pause
)

