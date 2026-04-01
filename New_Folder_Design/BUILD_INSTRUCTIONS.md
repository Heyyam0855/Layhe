# C++ Kompilyatorları: Kompilyasiya Təlimatları

## Windows üçün

### MinGW/GCC ilə:
```bash
g++ cpp_compiler_concepts.cpp -o compiler_concepts.exe
compiler_concepts.exe
```

### MSVC ilə:
```bash
cl cpp_compiler_concepts.cpp /EHsc /Fe:compiler_concepts.exe
compiler_concepts.exe
```

## Linux üçün

```bash
g++ cpp_compiler_concepts.cpp -o compiler_concepts
./compiler_concepts
```

## Mac üçün

```bash
clang++ cpp_compiler_concepts.cpp -o compiler_concepts
./compiler_concepts
```

## Optimizasiya ilə kompilyasiya

Daha sürətli binar kod üçün:
```bash
g++ -O2 cpp_compiler_concepts.cpp -o compiler_concepts
```

## Binar kodun yoxlanılması

Kompilyasiyadan sonra binar kodun strukturunu görmək üçün:

### Windows:
```bash
dumpbin /disasm compiler_concepts.exe
```

### Linux:
```bash
objdump -d compiler_concepts
```

### Mac:
```bash
otool -tv compiler_concepts
```

