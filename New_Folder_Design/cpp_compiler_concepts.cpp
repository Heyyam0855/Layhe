/*
 * C++ Kompilyatorları: Bayt Kodu və Binar Kod
 * 
 * Bu fayl C++ kompilyatorlarının necə işlədiyini və 
 * bayt kodu ilə binar kod arasındakı fərqləri izah edir.
 */

#include <iostream>
#include <iomanip>
#include <bitset>
#include <cstring>

// ============================================
// 1. BİNAR KOD (Binary Code) - CPU üçün
// ============================================
// Binar kod birbaşa CPU tərəfindən icra olunan maşın kodudur.
// Bu kod 0 və 1-lərdən ibarətdir və CPU-nun başa düşdüyü formatdadır.

void binaryCodeExample() {
    std::cout << "\n=== BİNAR KOD NÜMUNƏSİ ===\n";
    
    int sayi = 42;
    char herf = 'A';
    
    std::cout << "\n1. Tam ədəd (int) binar formatda:\n";
    std::cout << "   Sayı: " << sayi << "\n";
    std::cout << "   Binar: " << std::bitset<32>(sayi) << "\n";
    
    std::cout << "\n2. Simvol (char) binar formatda:\n";
    std::cout << "   Simvol: " << herf << "\n";
    std::cout << "   Binar: " << std::bitset<8>((unsigned char)herf) << "\n";
    
    std::cout << "\n3. RAM-də saxlanılan binar kod:\n";
    unsigned char* ram_ptr = (unsigned char*)&sayi;
    std::cout << "   RAM-dəki baytlar (little-endian):\n";
    for (size_t i = 0; i < sizeof(sayi); i++) {
        std::cout << "   [" << i << "] = " << std::bitset<8>(ram_ptr[i]) 
                  << " (0x" << std::hex << std::setw(2) << std::setfill('0') 
                  << (int)ram_ptr[i] << std::dec << ")\n";
    }
}

// ============================================
// 2. BAYT KODU (Bytecode) - Virtual Maşın üçün
// ============================================
// Bayt kodu virtual maşın (VM) tərəfindən icra olunan ara formatdır.
// C++ adətən birbaşa binar kod yaradır, lakin bəzi kompilyatorlar 
// (məsələn, LLVM IR) ara formatdan istifadə edir.

void bytecodeConcept() {
    std::cout << "\n=== BAYT KODU KONSEPSİYASI ===\n";
    
    std::cout << "\nC++ Kompilyator Prosesi:\n";
    std::cout << "1. C++ Mənbə Kodu (.cpp)\n";
    std::cout << "   ↓\n";
    std::cout << "2. Kompilyator (g++, clang++, MSVC)\n";
    std::cout << "   ↓\n";
    std::cout << "3. Binar Kod (.exe, .o, .obj)\n";
    std::cout << "   ↓\n";
    std::cout << "4. CPU tərəfindən icra\n";
    
    std::cout << "\nLLVM Kompilyator Prosesi (Bayt Kodu ilə):\n";
    std::cout << "1. C++ Mənbə Kodu (.cpp)\n";
    std::cout << "   ↓\n";
    std::cout << "2. LLVM Frontend\n";
    std::cout << "   ↓\n";
    std::cout << "3. LLVM IR (Intermediate Representation - Bayt Kodu)\n";
    std::cout << "   ↓\n";
    std::cout << "4. LLVM Backend\n";
    std::cout << "   ↓\n";
    std::cout << "5. Binar Kod (CPU üçün)\n";
}

// ============================================
// 3. CPU VƏ RAM İLƏ İŞLƏMƏ
// ============================================

void cpuAndRamExample() {
    std::cout << "\n=== CPU VƏ RAM İLƏ İŞLƏMƏ ===\n";
    
    // RAM-də məlumat saxlanılır (binar formatda)
    int a = 10;
    int b = 20;
    int c;
    
    std::cout << "\n1. RAM-də məlumatlar:\n";
    std::cout << "   a = " << a << " (RAM ünvanı: " << &a << ")\n";
    std::cout << "   b = " << b << " (RAM ünvanı: " << &b << ")\n";
    
    // CPU hesablamaları aparır (binar əməliyyatlar)
    c = a + b;  // CPU bu əməliyyatı binar kodda icra edir
    
    std::cout << "\n2. CPU hesablaması:\n";
    std::cout << "   c = a + b = " << c << "\n";
    
    std::cout << "\n3. Binar əməliyyatlar:\n";
    std::cout << "   a (binar): " << std::bitset<32>(a) << "\n";
    std::cout << "   b (binar): " << std::bitset<32>(b) << "\n";
    std::cout << "   c (binar): " << std::bitset<32>(c) << "\n";
    
    // Bitwise əməliyyatlar (CPU-nun birbaşa binar əməliyyatları)
    std::cout << "\n4. Bitwise əməliyyatlar (CPU-nun birbaşa binar əməliyyatları):\n";
    std::cout << "   a AND b: " << std::bitset<32>(a & b) << "\n";
    std::cout << "   a OR b:  " << std::bitset<32>(a | b) << "\n";
    std::cout << "   a XOR b: " << std::bitset<32>(a ^ b) << "\n";
}

// ============================================
// 4. KOMPİLYATOR NÖVLƏRİ
// ============================================

void compilerTypes() {
    std::cout << "\n=== KOMPİLYATOR NÖVLƏRİ ===\n";
    
    std::cout << "\n1. Native Kompilyatorlar (Birbaşa Binar Kod):\n";
    std::cout << "   - GCC (GNU Compiler Collection)\n";
    std::cout << "   - Clang/LLVM\n";
    std::cout << "   - MSVC (Microsoft Visual C++)\n";
    std::cout << "   → Birbaşa CPU üçün binar kod yaradır\n";
    
    std::cout << "\n2. Bayt Kodu Kompilyatorları:\n";
    std::cout << "   - Java (JVM bytecode)\n";
    std::cout << "   - C# (.NET IL - Intermediate Language)\n";
    std::cout << "   - LLVM IR (C++ üçün ara format)\n";
    std::cout << "   → Virtual maşın üçün bayt kodu yaradır\n";
    
    std::cout << "\n3. C++ və Bayt Kodu:\n";
    std::cout << "   - C++ adətən birbaşa binar kod yaradır\n";
    std::cout << "   - LLVM kompilyatoru IR (ara format) istifadə edir\n";
    std::cout << "   - Bu IR sonra müxtəlif platformalar üçün binar kod yaradır\n";
}

// ============================================
// 5. FƏRQLƏR
// ============================================

void differences() {
    std::cout << "\n=== BAYT KODU VƏ BİNAR KOD FƏRQLƏRİ ===\n";
    
    std::cout << "\nBİNAR KOD:\n";
    std::cout << "✓ CPU tərəfindən birbaşa icra olunur\n";
    std::cout << "✓ Platforma-spesifikdir (Windows/Linux/Mac)\n";
    std::cout << "✓ Daha sürətlidir (tərcümə lazım deyil)\n";
    std::cout << "✓ RAM-də və CPU-da 0 və 1 formatında\n";
    std::cout << "✓ C++ kompilyatorları adətən bunu yaradır\n";
    
    std::cout << "\nBAYT KODU:\n";
    std::cout << "✓ Virtual maşın tərəfindən icra olunur\n";
    std::cout << "✓ Platforma-müstəqildir\n";
    std::cout << "✓ Tərcümə lazımdır (JIT və ya interpretasiya)\n";
    std::cout << "✓ Daha yavaş ola bilər\n";
    std::cout << "✓ Java, C# kimi dillər bunu istifadə edir\n";
    
    std::cout << "\nCPU VƏ RAM:\n";
    std::cout << "✓ RAM: Məlumatları binar formatda (0 və 1) saxlayır\n";
    std::cout << "✓ CPU: Binar kodları birbaşa icra edir\n";
    std::cout << "✓ CPU və RAM binar kodla işləyir (qismən yaxındır)\n";
    std::cout << "✓ CPU RAM-dən məlumat oxuyur və icra edir\n";
}

// ============================================
// 6. PRAKTİK NÜMUNƏ
// ============================================

void practicalExample() {
    std::cout << "\n=== PRAKTİK NÜMUNƏ ===\n";
    
    // Bu kod kompilyasiya zamanı binar kod yaradılır
    int x = 5;
    int y = 3;
    int netice = x * y + 2;
    
    std::cout << "\nKod: int netice = x * y + 2;\n";
    std::cout << "x = " << x << ", y = " << y << "\n";
    std::cout << "netice = " << netice << "\n";
    
    std::cout << "\nKompilyasiya zamanı:\n";
    std::cout << "1. Kompilyator bu kodu binar əməliyyatlara çevirir\n";
    std::cout << "2. Binar kod faylı yaradılır (.exe və ya .o)\n";
    std::cout << "3. İcra zamanı:\n";
    std::cout << "   - Kod RAM-ə yüklənir (binar formatda)\n";
    std::cout << "   - CPU binar kodları oxuyur və icra edir\n";
    std::cout << "   - Nəticə RAM-də saxlanılır\n";
    
    // Binar təsvir
    std::cout << "\nBinar təsvir:\n";
    std::cout << "x (binar):      " << std::bitset<32>(x) << "\n";
    std::cout << "y (binar):      " << std::bitset<32>(y) << "\n";
    std::cout << "netice (binar): " << std::bitset<32>(netice) << "\n";
}

// ============================================
// ƏSAS FUNKSİYA
// ============================================

int main() {
    std::cout << "╔══════════════════════════════════════════════════════════╗\n";
    std::cout << "║  C++ KOMPİLYATORLARI: BAYT KODU VƏ BİNAR KOD             ║\n";
    std::cout << "║  CPU, RAM VƏ BİNAR KOD İLƏ İŞLƏMƏ                       ║\n";
    std::cout << "╚══════════════════════════════════════════════════════════╝\n";
    
    binaryCodeExample();
    bytecodeConcept();
    cpuAndRamExample();
    compilerTypes();
    differences();
    practicalExample();
    
    std::cout << "\n╔══════════════════════════════════════════════════════════╗\n";
    std::cout << "║  XÜLASƏ:                                                 ║\n";
    std::cout << "║  • C++ kompilyatorları adətən binar kod yaradır         ║\n";
    std::cout << "║  • Binar kod CPU tərəfindən birbaşa icra olunur         ║\n";
    std::cout << "║  • RAM və CPU binar kodla (0 və 1) işləyir             ║\n";
    std::cout << "║  • Bayt kodu virtual maşın üçün ara formatdır           ║\n";
    std::cout << "║  • CPU və RAM binar kodla işlədiyi üçün qismən yaxındır ║\n";
    std::cout << "╚══════════════════════════════════════════════════════════╝\n";
    
    return 0;
}

