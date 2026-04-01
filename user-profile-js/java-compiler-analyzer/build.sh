#!/bin/bash
echo "Java Compiler Analyzer Build Script"
echo "===================================="

echo
echo "1. Build qovluğunu yaradır..."
mkdir -p build

echo "2. Build qovluğuna keçir..."
cd build

echo "3. CMake konfiqurasiya edir..."
cmake ..

if [ $? -ne 0 ]; then
    echo "XƏTA: CMake konfiqurasiya uğursuz!"
    exit 1
fi

echo "4. Proqramı kompilyasiya edir..."
make

if [ $? -ne 0 ]; then
    echo "XƏTA: Kompilyasiya uğursuz!"
    exit 1
fi

echo
echo "✓ Build uğurlu tamamlandı!"
echo
echo "Proqramı işlətmək üçün:"
echo "  cd build"
echo "  ./JavaCompilerAnalyzer --help"
echo

# İcazə verir
chmod +x JavaCompilerAnalyzer