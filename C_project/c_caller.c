#include <stdio.h>

// Assembly funksiyasının deklarasiyası (external)
extern int square(int x);

int main() {
    int num = 5;
    int result = square(num);
    
    printf("========================================\n");
    printf("  C <-> Assembly İnteqrasiya Testi\n");
    printf("========================================\n\n");
    printf("Ədəd: %d\n", num);
    printf("Kvadrat: %d^2 = %d\n", num, result);
    printf("\n========================================\n");
    printf("✓ Assembly funksiyası uğurla çağırıldı!\n");
    printf("========================================\n");
    
    return 0;
}
