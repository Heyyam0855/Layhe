# TypeScript Sürətli Məlumat Bələdçisi

## Əsas Tiplər

### Primitiv Tiplər
```typescript
let ad: string = "Əli";
let yaş: number = 25;
let evli: boolean = true;
let nəticə: any = "istənilən tip";
let naməlum: unknown = 42;
let heçnə: undefined = undefined;
let boş: null = null;
```

### Array Tiplər
```typescript
let nömrələr: number[] = [1, 2, 3];
let adlar: Array<string> = ["Əli", "Leyla"];
let qarışıq: (string | number)[] = ["Əli", 25];
```

### Object Tiplər
```typescript
let şəxs: { ad: string; yaş: number } = {
    ad: "Əli",
    yaş: 25
};
```

## Interface-lər

### Sadə Interface
```typescript
interface İstifadəçi {
    id: number;
    ad: string;
    email: string;
    yaş?: number; // Optional
    readonly yaradılma: Date; // Read-only
}

const istifadəçi: İstifadəçi = {
    id: 1,
    ad: "Əli",
    email: "ali@example.com",
    yaradılma: new Date()
};
```

### Interface Genişləndirmə
```typescript
interface Əsas {
    id: number;
    ad: string;
}

interface İşçi extends Əsas {
    vəzifə: string;
    maaş: number;
}
```

## Type Aliases

```typescript
type Status = "aktiv" | "qeyri-aktiv" | "gözləmədə";
type ID = string | number;

type İstifadəçiMəlumatı = {
    ad: string;
    status: Status;
    id: ID;
};
```

## Union və Intersection

### Union Types
```typescript
function çap(dəyər: string | number): void {
    console.log(dəyər);
}
```

### Intersection Types
```typescript
type A = { a: number };
type B = { b: string };
type C = A & B; // { a: number; b: string }
```

## Function Tiplər

### Sadə Function
```typescript
function topla(a: number, b: number): number {
    return a + b;
}

// Arrow function
const çıxma = (a: number, b: number): number => a - b;
```

### Optional və Default Parameters
```typescript
function salamla(ad: string, soyad?: string, yaş: number = 18): string {
    return `Salam ${ad} ${soyad || ''} (${yaş})`;
}
```

### Function Type
```typescript
type CalculatorFunc = (a: number, b: number) => number;

const hesabla: CalculatorFunc = (x, y) => x * y;
```

## Class-lar

### Sadə Class
```typescript
class Avtomobil {
    // Properties
    public marka: string;
    private model: string;
    protected il: number;
    
    constructor(marka: string, model: string, il: number) {
        this.marka = marka;
        this.model = model;
        this.il = il;
    }
    
    // Method
    məlumatAl(): string {
        return `${this.marka} ${this.model} (${this.il})`;
    }
}
```

### Abstract Class
```typescript
abstract class Heyvan {
    abstract səsÇıxar(): string;
    
    hərəkətEt(): string {
        return "Heyvan hərəkət edir";
    }
}

class İt extends Heyvan {
    səsÇıxar(): string {
        return "Hav hav!";
    }
}
```

## Generics

### Generic Function
```typescript
function identityFunc<T>(arg: T): T {
    return arg;
}

const nəticə1 = identityFunc<string>("salam");
const nəticə2 = identityFunc<number>(42);
```

### Generic Interface
```typescript
interface Cavab<T> {
    data: T;
    uğur: boolean;
    mesaj?: string;
}

const istifadəçiCavabı: Cavab<İstifadəçi> = {
    data: { id: 1, ad: "Əli", email: "ali@test.com" },
    uğur: true
};
```

### Generic Class
```typescript
class DataSaxlayıcı<T> {
    private məlumatlar: T[] = [];
    
    əlavəEt(element: T): void {
        this.məlumatlar.push(element);
    }
    
    al(index: number): T | undefined {
        return this.məlumatlar[index];
    }
}
```

## Enums

```typescript
enum Rəng {
    Qırmızı = "qırmızı",
    Yaşıl = "yaşıl",
    Göy = "göy"
}

enum Status {
    Yeni,        // 0
    İşlənir,     // 1
    Bitmiş       // 2
}
```

## Type Guards

```typescript
function mətndir(dəyər: any): dəyər is string {
    return typeof dəyər === "string";
}

function prosesEt(dəyər: string | number): string {
    if (mətndir(dəyər)) {
        return dəyər.toUpperCase(); // string method
    }
    return dəyər.toString(); // number method
}
```

## Utility Types

```typescript
interface İstifadəçi {
    id: number;
    ad: string;
    email: string;
    yaş: number;
}

// Partial - bütün xüsusiyyətləri optional edir
type Yenilənəcəkİstifadəçi = Partial<İstifadəçi>;

// Pick - müəyyən xüsusiyyətləri seçir
type İstifadəçiÖzəti = Pick<İstifadəçi, "id" | "ad">;

// Omit - müəyyən xüsusiyyətləri çıxarır
type Yeniİstifadəçi = Omit<İstifadəçi, "id">;

// Required - bütün xüsusiyyətləri məcburi edir
type Tamİstifadəçi = Required<İstifadəçi>;
```

## Module System

### Export
```typescript
// utils.ts
export interface Config {
    apiUrl: string;
    timeout: number;
}

export const defaultConfig: Config = {
    apiUrl: "https://api.example.com",
    timeout: 5000
};

export default function logger(message: string): void {
    console.log(message);
}
```

### Import
```typescript
// main.ts
import logger, { Config, defaultConfig } from './utils';
import * as Utils from './utils';

logger("Başladı");
console.log(defaultConfig.apiUrl);
```

## Çox İstifadə Olunan Nümunələr

### API Response Type
```typescript
interface ApiCavab<T> {
    data: T;
    status: number;
    message: string;
    timestamp: string;
}

interface İstifadəçiAPI {
    id: number;
    username: string;
    profile: {
        firstName: string;
        lastName: string;
    };
}

const cavab: ApiCavab<İstifadəçiAPI[]> = {
    data: [],
    status: 200,
    message: "Uğurlu",
    timestamp: new Date().toISOString()
};
```

### Event Handler Type
```typescript
type EventHandler<T = HTMLElement> = (event: Event & { target: T }) => void;

const buttonClick: EventHandler<HTMLButtonElement> = (event) => {
    console.log(event.target.textContent);
};
```

Bu bələdçi TypeScript-in ən çox istifadə olunan xüsusiyyətlərini əhatə edir!
