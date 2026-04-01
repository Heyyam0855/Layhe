Windows çəkirdək səviyyəsində proqramlaşdırma üçün məsləhətlərim:

## Çəkirdək Səviyyə Proqramlaşdırma

### 1. **Compiler Seçimi**
- Windows Kernel Driver Development üçün **WDK (Windows Driver Kit)** və **Visual Studio** istifadə edin
- GCC/MinGW çəkirdək driver-lər üçün **tövsiyə edilmir**
- Microsoft-un rəsmi toolchain-i ilə uyğunluq və dəstək daha yaxşıdır

### 2. **Tələblər**
```powershell
# Windows SDK və WDK yükləyin
# Visual Studio 2019/2022 Enterprise/Community
# Windows Driver Kit (WDK) 10
```

### 3. **Driver İmzalama**
- Windows 10/11-də driver-lər **imzalanmalıdır**
- Test üçün: Test Signing Mode
```powershell
bcdedit /set testsigning on
```
- Production üçün: **EV Code Signing Certificate** lazımdır

### 4. **Məsləhətlər**

**✅ Tövsiyə edilir:**
- WDK + Visual Studio + MSVC
- Windows Driver Framework (WDF)
- Kernel Mode Driver Framework (KMDF)

**❌ Tövsiyə edilmir:**
- GCC/MinGW kernel driver-lər üçün
- Assembly-dən tam driver yazmaq
- İmzasız driver-ləri production-da işlətmək

### 5. **Başlanğıc Nümunə**
````c
#include <ntddk.h>

DRIVER_INITIALIZE DriverEntry;
DRIVER_UNLOAD UnloadDriver;

NTSTATUS DriverEntry(
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
)
{
    DriverObject->DriverUnload = UnloadDriver;
    KdPrint(("Driver loaded successfully\n"));
    return STATUS_SUCCESS;
}

VOID UnloadDriver(_In_ PDRIVER_OBJECT DriverObject)
{
    KdPrint(("Driver unloaded\n"));
}
````

**Əsas məsləhət:** Windows kernel development üçün Microsoft-un rəsmi toolchain-indən istifadə edin. Sertifikat alın və test signing ilə başlayın.