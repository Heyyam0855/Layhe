# TypeScript Qurulum Planı

## 1. Tələblər və Hazırlıq

### Sistem tələbləri:
- Node.js (v14 və ya daha yeni versiya)
- npm və ya yarn paket meneceri
- Kod editoru (VS Code tövsiyə olunur)

### İlkin yoxlama:
```bash
node --version
npm --version
```

## 2. TypeScript Qurulumu

### Global TypeScript qurulumu:
```bash
npm install -g typescript
```

### TypeScript kompaylerinin yoxlanması:
```bash
tsc --version
```

## 3. Layihə Qurulumu

### Yeni layihə yaratmaq:
```bash
mkdir typescript-layihem
cd typescript-layihem
npm init -y
```

### TypeScript-i layihəyə əlavə etmək:
```bash
# Development dependency olaraq
npm install --save-dev typescript

# Type definitions (əgər lazımdırsa)
npm install --save-dev @types/node
```

## 4. TypeScript Konfiqurasiyası

### tsconfig.json faylının yaradılması:
```bash
tsc --init
```

### Əsas tsconfig.json parametrləri:
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```

## 5. Layihə Strukturu

### Tövsiyə olunan qovluq strukturu:
```
typescript-layihem/
├── src/
│   ├── index.ts
│   ├── types/
│   │   └── index.ts
│   ├── utils/
│   │   └── helpers.ts
│   └── components/
├── dist/
├── tests/
├── package.json
├── tsconfig.json
└── README.md
```

## 6. Package.json Scripts

### Faydalı npm scriptləri:
```json
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsc --watch",
    "clean": "rm -rf dist"
  }
}
```

## 7. İlk TypeScript Faylı

### src/index.ts nümunəsi:
```typescript
// Interface təyini
interface User {
  id: number;
  name: string;
  email: string;
  isActive?: boolean;
}

// Class nümunəsi
class UserManager {
  private users: User[] = [];

  addUser(user: User): void {
    this.users.push(user);
    console.log(`İstifadəçi əlavə edildi: ${user.name}`);
  }

  getUserById(id: number): User | undefined {
    return this.users.find(user => user.id === id);
  }

  getAllUsers(): User[] {
    return this.users;
  }
}

// Function nümunəsi
function createUser(name: string, email: string): User {
  return {
    id: Date.now(),
    name,
    email,
    isActive: true
  };
}

// İstifadə nümunəsi
const userManager = new UserManager();
const newUser = createUser("Əli Məmmədov", "ali@example.com");
userManager.addUser(newUser);

console.log("Bütün istifadəçilər:", userManager.getAllUsers());
```

## 8. Kompayler və İşə Salma

### TypeScript fayllarını JavaScript-ə çevirmək:
```bash
npm run build
```

### Layihəni işə salmaq:
```bash
npm start
```

### Development rejimində işləmək:
```bash
npm run dev
```

## 9. Əlavə Alətlər və Paketlər

### ESLint və Prettier qurulumu:
```bash
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin prettier
```

### Jest test framework-u:
```bash
npm install --save-dev jest @types/jest ts-jest
```

### Nodemon development üçün:
```bash
npm install --save-dev nodemon ts-node
```

## 10. VS Code Ekstensionları

### Tövsiyə olunan ekstensionlar:
- TypeScript Hero
- ESLint
- Prettier - Code formatter
- Auto Rename Tag
- Bracket Pair Colorizer
- GitLens

## 11. Ümumi TypeScript Konseptləri

### Əsas tip növləri:
- `string`, `number`, `boolean`
- `array`, `object`
- `any`, `unknown`, `never`
- `union types`: `string | number`
- `literal types`: `"red" | "green" | "blue"`

### Interfaces və Types:
```typescript
interface Person {
  name: string;
  age: number;
}

type Status = "active" | "inactive";
```

### Generics:
```typescript
function identity<T>(arg: T): T {
  return arg;
}
```

## 12. Səhvlərin Həlli

### Ümumi problemlər:
1. **Module not found**: `npm install` işə salın
2. **Type errors**: tsconfig.json-da strict rejimi yoxlayın
3. **Path resolution**: tsconfig.json-da paths konfiqurasiyasını yoxlayın

### Debugging:
```bash
# Source maps ilə debugging
tsc --sourceMap
```

## 13. Deploy və Production

### Production build:
```bash
npm run build
npm prune --production
```

### Environment variables:
```typescript
const PORT = process.env.PORT || 3000;
```

## 14. Təkmilləşdirmə

### Advanced konfiqurasiya:
- Webpack integration
- Babel setup
- Docker containerization
- CI/CD pipeline setup

Bu plan TypeScript-i sıfırdan öyrənmək və real layihələrdə istifadə etmək üçün tam bələdçidir.
