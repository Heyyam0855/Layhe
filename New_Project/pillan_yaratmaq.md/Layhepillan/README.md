# TypeScript Öyrənmə Mərkəzi

TypeScript-i öyrənmək və işlətmək üçün hazırlanmış tam bələdçi toplusu.

## 📚 Bələdçilər

### 1. [TypeScript Qurulum Planı](./TypeScript_Qurulum_Pillani.md)
- Sistem tələbləri və hazırlıq
- Tam qurulum addımları
- Layihə konfiqurasiyası
- Advanced ayarlar və alətlər

### 2. [TypeScript Praktik Başlanğıc](./TypeScript_Praktik_Baslangic.md)
- Addım-addım praktik bələdçi
- İlk layihəni yaratmaq
- Sadə nümunələr
- Sürətli başlanğıc üçün hazır əmrlər

### 3. [TypeScript Sürətli Məlumat](./TypeScript_Surətli_Məlumat.md)
- Əsas tip sistemi
- Interface və Type alias-lar
- Class və Generic-lər
- Utility types və nümunələr

## 🚀 Sürətli Başlanğıc

Əgər dərhal başlamaq istəyirsinizsə:

```bash
# 1. TypeScript quraşdırın
npm install -g typescript

# 2. Yeni layihə yaradın
mkdir my-typescript-project && cd my-typescript-project

# 3. Package.json yaradın
npm init -y

# 4. TypeScript konfiqurasiyası
npm install --save-dev typescript @types/node
tsc --init

# 5. Src qovluğu və ilk fayl
mkdir src
echo 'console.log("Salam TypeScript!");' > src/index.ts

# 6. Kompayler və işə salın
tsc && node dist/index.js
```

## 📖 Öyrənmə Yolu

1. **Yeni başlayanlar üçün**: [Praktik Başlanğıc](./TypeScript_Praktik_Baslangic.md)
2. **Tam konfiqurasiya üçün**: [Qurulum Planı](./TypeScript_Qurulum_Pillani.md)
3. **Sürətli məlumat üçün**: [Sürətli Məlumat](./TypeScript_Surətli_Məlumat.md)

## 🛠️ Faydalı Linklər

- [TypeScript Rəsmi Saytı](https://www.typescriptlang.org/)
- [TypeScript Playground](https://www.typescriptlang.org/play)
- [VS Code TypeScript Dəstəyi](https://code.visualstudio.com/docs/languages/typescript)

## 💡 Məsləhətlər

- Həmişə type safety istifadə edin
- Interface-ləri object structure-lar üçün istifadə edin
- Generic-ləri reusable code üçün istifadə edin
- ESLint və Prettier quraşdırın
- Tests yazın (Jest tövsiyə olunur)

Bu bələdçiləri izləməklə TypeScript-də peşəkar inkişaf edə bilərsiniz!
