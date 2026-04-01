@echo off
REM Batch script to check Java installation and guide user

echo ================================================
echo       OpenJDK Yoxlama ve Qurasdirma
echo ================================================
echo.

REM Check if Java is installed
where java >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Java tapildi!
    echo.
    java -version
    echo.
    javac -version 2>nul
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo [OK] JDK duzgun qurulub!
        echo.
        echoIndi Pillan-i kompilyasiya edek:
        echo   javac Pillan.java
        echo.
        echo Ve icra edek:
        echo   java Pillan
    ) else (
        echo.
        echo [XETA] JDK tapilmadi - yalniz JRE qurulub!
        echo.
        echo JDK qurasdirilmalidir. Bax: JAVA_SETUP.md
    )
) else (
    echo [XETA] Java tapilmadi!
    echo.
    echo OpenJDK qurasdirilmalidir.
    echo.
    echo Suretli qurasdirma ucun:
    echo 1. PowerShell-i Administrator olaraq acin
    echo 2. Bu emri icra edin:
    echo    .\setup_java.ps1
    echo.
    echo Ve ya manual olaraq:
    echo    https://adoptium.net/
    echo.
    echo Daha etrafli melumat: JAVA_SETUP.md
)

echo.
echo ================================================
pause
