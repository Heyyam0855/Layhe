# Pıllan - Java-dan Python icra edən proqram

## Təsvir
Pıllan - Java proqramından Python kodunu çağırıb icra edən bir Java class-ıdır.

## Xüsusiyyətlər
- ✅ Python kodunu birbaşa icra etmək
- ✅ Python fayllarını icra etmək
- ✅ Arqumentlərlə Python fayllarını icra etmək
- ✅ Python versiyasını yoxlamaq
- ✅ Nəticələri almaq və işləmək

## İstifadə

### 1. Sadə Python kodu icra etmək

```java
Pıllan pıllan = new Pıllan();
String nəticə = pıllan.executePythonCode("print('Salam Dünya!')");
System.out.println(nəticə); // Output: Salam Dünya!
```

### 2. Python faylını icra etmək

```java
Pıllan pıllan = new Pıllan();
String nəticə = pıllan.executePythonFile("script.py");
System.out.println(nəticə);
```

### 3. Arqumentlərlə Python faylını icra etmək

```java
Pıllan pıllan = new Pıllan();
String[] args = {"arg1", "arg2", "arg3"};
String nəticə = pıllan.executePythonFile("script.py", args);
System.out.println(nəticə);
```

### 4. Xüsusi Python interpreter istifadə etmək

```java
Pıllan pıllan = new Pıllan("python3");
// və ya
Pıllan pıllan = new Pıllan("C:\\Python39\\python.exe");
```

### 5. Python versiyasını yoxlamaq

```java
Pıllan pıllan = new Pıllan();
String versiya = pıllan.getPythonVersion();
System.out.println(versiya); // Output: Python 3.x.x
```

## Kompilyasiya və İcra

### Kompilyasiya
```bash
javac Pıllan.java
```

### İcra
```bash
java Pıllan
```

## Nümunə Python fayl yaratmaq

`test_script.py` yaradın:
```python
import sys

print("Salam Python-dan!")
print(f"Arqumentlər: {sys.argv[1:]}")

# Hesablama
result = sum(range(1, 11))
print(f"1-dən 10-a qədər cəm: {result}")
```

Java-dan çağırın:
```java
Pıllan pıllan = new Pıllan();
String[] args = {"test1", "test2"};
String nəticə = pıllan.executePythonFile("test_script.py", args);
System.out.println(nəticə);
```

## Qeydlər
- Python quraşdırılmış olmalıdır və PATH-da olmalıdır
- Windows-da `python` və ya `python3` əmri işləməlidir
- Mürəkkəb Python kodları üçün xüsusi escape simvollarına diqqət edin

## Xəta işləmə
```java
try {
    Pıllan pıllan = new Pıllan();
    String nəticə = pıllan.executePythonCode("print(1/0)");
} catch (RuntimeException e) {
    System.err.println("Python xətası: " + e.getMessage());
} catch (IOException | InterruptedException e) {
    System.err.println("İcra xətası: " + e.getMessage());
}
```

## Tələblər
- Java 8 və ya daha yüksək versiya (tövsiyə: OpenJDK 17 və ya 21 LTS)
- Python 3.x quraşdırılmış olmalıdır

## ⚙️ Java Quraşdırması

### Java yoxlanışı
```bash
# Terminaldə yoxlayın
java -version
javac -version
```

### Avtomatik yoxlama
```bash
# Windows CMD-də
check_java.bat
```

### Java quraşdırılmayıbsa:

**Seçim 1: Avtomatik quraşdırma (Tövsiyə)**
```powershell
# PowerShell-i Administrator olaraq açın
.\setup_java.ps1
```

**Seçim 2: WinGet ilə**
```powershell
winget install EclipseAdoptium.Temurin.21.JDK
```

**Seçim 3: Manual quraşdırma**
1. https://adoptium.net/ səhifəsinə gedin
2. Windows x64 MSI installer yükləyin
3. Quraşdırın (PATH-a əlavə etməyi unutmayın!)

Ətraflı təlimatlar: [JAVA_SETUP.md](JAVA_SETUP.md)
