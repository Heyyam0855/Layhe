@echo off
echo Java Compiler Analyzer Build Script
echo ====================================

echo.
echo 1. Build qovlugunu yaradir...
if not exist build mkdir build

echo 2. Build qovluguna kecir...
cd build

echo 3. CMake konfiqurasiya edir...
cmake ..

if %ERRORLEVEL% NEQ 0 (
    echo XETA: CMake konfiqurasiya ugursuz!
    pause
    exit /b 1
)

echo 4. Proqrami kompilyasiya edir...
cmake --build .

if %ERRORLEVEL% NEQ 0 (
    echo XETA: Kompilyasiya ugursuz!
    pause
    exit /b 1
)

echo.
echo ✓ Build ugurlu tamamlandi!
echo.
echo Proqrami test edirik...
echo.

echo ========================================
echo Test 1: Help mesajini goster
echo ========================================
JavaCompilerAnalyzer.exe --help
echo.

echo ========================================
echo Test 2: Numune Java fayli yaradir
echo ========================================
JavaCompilerAnalyzer.exe --create-sample
echo.

echo ========================================
echo Test 3: Sample.java faylini analiz edir
echo ========================================
JavaCompilerAnalyzer.exe Sample.java
echo.

echo ========================================
echo Butun testler tamamlandi!
echo ========================================
echo.
echo Proqrami manuel isletmek ucun:
echo   cd build
echo   .\JavaCompilerAnalyzer.exe --help
echo   .\JavaCompilerAnalyzer.exe --create-sample  
echo   .\JavaCompilerAnalyzer.exe Sample.java
echo.

pause