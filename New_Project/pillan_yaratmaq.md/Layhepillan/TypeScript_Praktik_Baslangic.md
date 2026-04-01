# TypeScript Praktik Başlama Bələdçisi

## Birinci Addım: Hazırlıq

1. **Node.js yoxlanışı**
   ```bash
   node --version
   npm --version
   ```
   Əgər yoxdursa: https://nodejs.org/ saytından endirin

2. **TypeScript quraşdırması**
   ```bash
   npm install -g typescript
   tsc --version
   ```

## İkinci Addım: İlk Layihə

1. **Layihə qovluğu yaradın**
   ```bash
   mkdir ilk-typescript-layihem
   cd ilk-typescript-layihem
   ```

2. **Package.json yaradın**
   ```bash
   npm init -y
   ```

3. **TypeScript əlavə edin**
   ```bash
   npm install --save-dev typescript @types/node
   ```

4. **tsconfig.json yaradın**
   ```bash
   tsc --init
   ```

## Üçüncü Addım: Qovluq Strukturu

```
ilk-typescript-layihem/
├── src/
│   └── index.ts
├── dist/
├── package.json
└── tsconfig.json
```

1. **src qovluğu yaradın**
   ```bash
   mkdir src
   ```

2. **İlk TypeScript faylı yaradın (src/index.ts)**

## Dördüncü Addım: İlk Kod

`src/index.ts` faylında:

```typescript
// Sadə başlanğıc
console.log("Salam TypeScript!");

// Dəyişən təyinləri
let ad: string = "Əli";
let yaş: number = 25;
let aktiv: boolean = true;

// Funksiya
function salamla(ad: string): string {
    return `Salam, ${ad}!`;
}

console.log(salamla(ad));

// Interface nümunəsi
interface İstifadəçi {
    ad: string;
    yaş: number;
    email?: string; // Optional
}

const istifadəçi: İstifadəçi = {
    ad: "Leyla",
    yaş: 23
};

console.log(istifadəçi);
```

## Beşinci Addım: Kompayler və İşə Salma

1. **TypeScript-i JavaScript-ə çevirin**
   ```bash
   tsc
   ```

2. **Nəticəni işə salın**
   ```bash
   node dist/index.js
   ```

## Altıncı Addım: Script-ləri Sadələşdirin

`package.json`-a əlavə edin:

```json
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsc && node dist/index.js"
  }
}
```

İndi bunları istifadə edin:
```bash
npm run build
npm start
npm run dev
```

## Yedinci Addım: Watch Mode

Avtomatik yenidən kompayler üçün:
```bash
tsc --watch
```

## Səkkizinci Addım: VS Code Konfiqurasiyası

1. **VS Code-da layihəni açın**
2. **TypeScript ekstensionları quraşdırın**
3. **Ctrl+Shift+P → "TypeScript: Select TypeScript Version" → "Use Workspace Version"**

## Doqquzuncu Addım: Error Handling

```typescript
// Type safety nümunəsi
function hesabla(a: number, b: number): number {
    return a + b;
}

// Bu səhv olacaq:
// hesabla("5", "10"); // Error: string tipində arqument

// Düzgün:
console.log(hesabla(5, 10)); // 15
```

## Onuncu Addım: Advanced Nümunələr

```typescript
// Generic function
function arrayÇevir<T>(items: T[]): T[] {
    return items.reverse();
}

const nömrələr = arrayÇevir([1, 2, 3, 4]);
const sözlər = arrayÇevir(["a", "b", "c"]);

// Class nümunəsi
class Avtomobil {
    constructor(
        public marka: string,
        private model: string,
        protected il: number
    ) {}

    məlumatAl(): string {
        return `${this.marka} ${this.model} (${this.il})`;
    }
}

const avtomobil = new Avtomobil("BMW", "X5", 2023);
console.log(avtomobil.məlumatAl());
```

## İcra Addımları (Sürətli Başlanğıc)

1. Terminal açın
2. Bu əmrləri ardıcıl işə salın:

```bash
# 1. Layihə yaradın
mkdir typescript-test && cd typescript-test

# 2. Package.json yaradın
npm init -y

# 3. TypeScript quraşdırın
npm install -g typescript
npm install --save-dev typescript @types/node

# 4. Konfiqurasiya yaradın
tsc --init

# 5. src qovluğu yaradın
mkdir src

# 6. İlk fayl yaradın (manual olaraq src/index.ts)

# 7. Kompayler edin
tsc

# 8. İşə salın
node dist/index.js
```

Bu addımları izləməklə TypeScript-ə başlaya bilərsiniz!
