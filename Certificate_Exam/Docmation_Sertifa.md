# Windows Çəkirdək Səviyyə Proqramlaşdırma - Ətraflı Təlim Planı

## 📋 Giriş

Bu plan Windows kernel driver development öyrənmək üçün addım-addım təlimat təqdim edir. Meslehet.md faylında verilən məsləhətlərə əsaslanaraq hazırlanmışdır.

---

## 🎯 Məqsəd
Windows çəkirdək səviyyəsində driver yazmaq və imzalamaq bacarığını əldə etmək.

---

## 📚 Faza 1: Hazırlıq və Mühit Qurulması (1 həftə)

### 1.1 Tələb olunan proqram təminatının quraşdırılması

#### Addım 1: Visual Studio quraşdırılması
- **Visual Studio 2022 Community/Enterprise** yükləyin
- İşləmə yükləri (workloads):
  - Desktop development with C++
  - .NET desktop development
  
```powershell
# Visual Studio installer ilə yükləmə
# https://visualstudio.microsoft.com/downloads/
```

#### Addım 2: Windows SDK quraşdırılması
- **Windows 10/11 SDK** yükləyin
- En son versiyasını seçin
- Debugging Tools for Windows seçin

#### Addım 3: Windows Driver Kit (WDK) quraşdırılması
- **WDK 10** yükləyin (Visual Studio ilə uyğun versiya)
- Installation location default saxlayın
- WDK Visual Studio extension install olmalıdır

```powershell
# WDK download linki:
# https://docs.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk
```

### 1.2 Təqdimat və Nəzəri Bilik

#### Nəzəri Bilik Mövzuları:
1. **Windows Kernel Architecture**
   - User Mode vs Kernel Mode
   - Ring 0, Ring 3 konsepsiyaları
   - System calls və interrupt handling

2. **Driver Növləri**
   - Kernel Mode Driver Framework (KMDF)
   - User Mode Driver Framework (UMDF)
   - Legacy WDM Drivers

3. **Driver Lifecycle**
   - DriverEntry
   - AddDevice
   - IRP handling
   - Driver Unload

---

## 🔧 Faza 2: Test Mühitinin Qurulması (3-5 gün)

### 2.1 Test Signing Mode aktivləşdirilməsi

```powershell
# Administrator PowerShell-də çalışdırın:
bcdedit /set testsigning on

# Reboot edin
shutdown /r /t 0

# Yoxlama:
bcdedit | findstr testsigning
```

⚠️ **Qeyd:** Test signing yalnız development məqsədlər üçündür!

### 2.2 Virtual Machine Setup (Tövsiyə edilir)
- **Hyper-V** və ya **VMware** istifadə edin
- Windows 10/11 test VM quraşdırın
- Network debugging setup edin
- VM snapshot-lar yaradın

```powershell
# Hyper-V aktivləşdirilməsi:
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

### 2.3 Debugging Setup
- **WinDbg** (yeni: WinDbg Preview)
- Kernel debugging connection (Local və ya Network)
- Symbol server konfiqurasiyası

```powershell
# Symbol server environment variable:
setx _NT_SYMBOL_PATH "SRV*C:\Symbols*https://msdl.microsoft.com/download/symbols"
```

---

## 💻 Faza 3: İlk Driver Proyektinin Yaradılması (1 həftə)

### 3.1 "Hello World" Kernel Driver

#### Addım 1: Yeni Proyekt Yaratmaq
1. Visual Studio açın
2. **File → New → Project**
3. **Kernel Mode Driver, Empty (KMDF)** seçin
4. Proyekt adı: `HelloKernelDriver`

#### Addım 2: Driver Kodunun Yazılması

**HelloKernelDriver.c:**
```c
#include <ntddk.h>

// Forward declarations
DRIVER_INITIALIZE DriverEntry;
DRIVER_UNLOAD UnloadDriver;

// Driver Entry Point
NTSTATUS DriverEntry(
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
)
{
    UNREFERENCED_PARAMETER(RegistryPath);
    
    // Set unload routine
    DriverObject->DriverUnload = UnloadDriver;
    
    // Log message
    KdPrint(("HelloKernelDriver: Driver loaded successfully!\n"));
    KdPrint(("HelloKernelDriver: DriverObject = 0x%p\n", DriverObject));
    
    return STATUS_SUCCESS;
}

// Driver Unload Routine
VOID UnloadDriver(_In_ PDRIVER_OBJECT DriverObject)
{
    UNREFERENCED_PARAMETER(DriverObject);
    KdPrint(("HelloKernelDriver: Driver unloaded\n"));
}
```

#### Addım 3: Build və Test

```powershell
# Visual Studio-da build edin (F7 və ya Ctrl+Shift+B)
# Debug x64 konfiqurasiyasını seçin

# Driver yükləmə:
sc create HelloKernelDriver type= kernel binPath= "C:\path\to\HelloKernelDriver.sys"
sc start HelloKernelDriver

# Log-ları görmək:
# DebugView və ya WinDbg istifadə edin

# Driver dayandırma və silinməsi:
sc stop HelloKernelDriver
sc delete HelloKernelDriver
```

### 3.2 DebugView ilə Output Görmək
1. **DebugView** (Sysinternals) yükləyin
2. Administrator kimi çalışdırın
3. **Capture → Capture Kernel** aktivləşdirin
4. Driver yükləyin və log mesajlarını görün

---

## 🔐 Faza 4: Driver İmzalama (2 həftə)

### 4.1 Test İmzalama (Development)

#### Self-Signed Certificate yaratmaq:
```powershell
# MakeCert ilə test sertifikat yaratma:
makecert -r -pe -ss PrivateCertStore -n "CN=TestDriverCert" TestDriverCert.cer

# Certificate-i Trusted Root-a əlavə edin:
certmgr.exe /add TestDriverCert.cer /s /r localMachine root
certmgr.exe /add TestDriverCert.cer /s /r localMachine trustedpublisher
```

#### Driver-i İmzalamaq:
```powershell
# SignTool istifadə edərək:
signtool sign /v /s PrivateCertStore /n "TestDriverCert" /t http://timestamp.digicert.com HelloKernelDriver.sys

# İmza yoxlama:
signtool verify /v /pa HelloKernelDriver.sys
```

### 4.2 Production İmzalama

#### EV Code Signing Certificate almaq:
1. **SSL.com**, **DigiCert**, və ya **Sectigo** kimi CA-dan sertifikat alın
2. **EV (Extended Validation)** sertifikat lazımdır (USB token)
3. Qiymət: ~$300-500/il

#### WHQL (Windows Hardware Quality Labs) Test
1. Driver-i Microsoft-a göndərin
2. HLK (Hardware Lab Kit) testlərini keçin
3. Rəsmi imza alın

⚠️ **Mühüm:** Windows 10/11 (64-bit) üçün yalnız EV-signed driver-lər yüklənə bilər (test mode olmadan).

---

## 🚀 Faza 5: Ətraflı Driver Development (4-6 həftə)

### 5.1 I/O Request Packet (IRP) Handling

**Mövzular:**
- IRP nədir və necə işləyir
- Major və Minor Function Codes
- IRP completion
- Asynchronous I/O

**Nümunə Kod:**
```c
NTSTATUS CreateCloseDispatch(
    _In_ PDEVICE_OBJECT DeviceObject,
    _In_ PIRP Irp
)
{
    UNREFERENCED_PARAMETER(DeviceObject);
    
    KdPrint(("CreateCloseDispatch called\n"));
    
    Irp->IoStatus.Status = STATUS_SUCCESS;
    Irp->IoStatus.Information = 0;
    IoCompleteRequest(Irp, IO_NO_INCREMENT);
    
    return STATUS_SUCCESS;
}

// DriverEntry-də:
DriverObject->MajorFunction[IRP_MJ_CREATE] = CreateCloseDispatch;
DriverObject->MajorFunction[IRP_MJ_CLOSE] = CreateCloseDispatch;
```

### 5.2 Device Object Yaratmaq

```c
NTSTATUS CreateDevice(_In_ PDRIVER_OBJECT DriverObject)
{
    NTSTATUS status;
    PDEVICE_OBJECT deviceObject = NULL;
    UNICODE_STRING deviceName = RTL_CONSTANT_STRING(L"\\Device\\MyDevice");
    UNICODE_STRING symLink = RTL_CONSTANT_STRING(L"\\??\\MyDeviceLink");
    
    // Create device
    status = IoCreateDevice(
        DriverObject,
        0,
        &deviceName,
        FILE_DEVICE_UNKNOWN,
        FILE_DEVICE_SECURE_OPEN,
        FALSE,
        &deviceObject
    );
    
    if (!NT_SUCCESS(status)) {
        return status;
    }
    
    // Create symbolic link
    status = IoCreateSymbolicLink(&symLink, &deviceName);
    if (!NT_SUCCESS(status)) {
        IoDeleteDevice(deviceObject);
        return status;
    }
    
    return STATUS_SUCCESS;
}
```

### 5.3 IOCTL (I/O Control) Implementation

```c
#define IOCTL_CUSTOM_OPERATION CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS)

NTSTATUS DeviceControlDispatch(
    _In_ PDEVICE_OBJECT DeviceObject,
    _In_ PIRP Irp
)
{
    PIO_STACK_LOCATION stackLocation;
    ULONG controlCode;
    NTSTATUS status = STATUS_SUCCESS;
    
    UNREFERENCED_PARAMETER(DeviceObject);
    
    stackLocation = IoGetCurrentIrpStackLocation(Irp);
    controlCode = stackLocation->Parameters.DeviceIoControl.IoControlCode;
    
    switch (controlCode) {
        case IOCTL_CUSTOM_OPERATION:
            KdPrint(("Custom operation requested\n"));
            // İşləm həyata keçirin
            break;
        default:
            status = STATUS_INVALID_DEVICE_REQUEST;
            break;
    }
    
    Irp->IoStatus.Status = status;
    Irp->IoStatus.Information = 0;
    IoCompleteRequest(Irp, IO_NO_INCREMENT);
    
    return status;
}
```

### 5.4 User Mode Application ilə Qarşılıqlı əlaqə

**UserApp.cpp:**
```cpp
#include <Windows.h>
#include <iostream>

int main()
{
    HANDLE hDevice = CreateFileW(
        L"\\\\.\\MyDeviceLink",
        GENERIC_READ | GENERIC_WRITE,
        0,
        NULL,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        NULL
    );
    
    if (hDevice == INVALID_HANDLE_VALUE) {
        std::cout << "Failed to open device: " << GetLastError() << std::endl;
        return 1;
    }
    
    std::cout << "Device opened successfully!" << std::endl;
    
    DWORD bytesReturned;
    BOOL result = DeviceIoControl(
        hDevice,
        IOCTL_CUSTOM_OPERATION,
        NULL, 0,
        NULL, 0,
        &bytesReturned,
        NULL
    );
    
    if (result) {
        std::cout << "IOCTL succeeded!" << std::endl;
    }
    
    CloseHandle(hDevice);
    return 0;
}
```

---

## 🔍 Faza 6: Debugging və Troubleshooting (Davamlı)

### 6.1 WinDbg istifadəsi

```powershell
# Kernel debugging başlatmaq:
# 1. Test VM-də:
bcdedit /debug on
bcdedit /dbgsettings serial debugport:1 baudrate:115200

# 2. Host sistemdə WinDbg:
# File → Kernel Debug → COM
# Port: COM1, Baud Rate: 115200
```

**Əsas WinDbg əmrləri:**
```
!analyze -v          // Crash analizi
lm                   // Yüklənmiş modullar
bp DriverEntry       // Breakpoint qoymaq
g                    // Davam et
k                    // Stack trace
dd [address]         // Memory dump
!process 0 0         // Bütün proseslər
```

### 6.2 Common Issues və Həll yolları

| Problem | Səbəb | Həll |
|---------|-------|------|
| DRIVER_IRQL_NOT_LESS_OR_EQUAL | Paged memory access yüksək IRQL-də | NonPagedPool istifadə edin |
| PAGE_FAULT_IN_NONPAGED_AREA | NULL pointer dereference | Pointer validation əlavə edin |
| Driver yüklənmir | İmza problemi | Test signing yoxlayın |
| Blue Screen (BSOD) | Driver crash | WinDbg ilə crash dump analiz edin |

---

## 📖 Faza 7: İrəliləyən Mövzular (2-3 ay)

### 7.1 Filter Drivers
- Minifilter Framework
- File System Filter Drivers
- Network Filter Drivers

### 7.2 Memory Management
- Paged vs Non-Paged Pool
- MDL (Memory Descriptor List)
- DMA (Direct Memory Access)

### 7.3 Synchronization
- Spinlocks
- Mutexes
- Events və Semaphores
- IRQL levels

### 7.4 Interrupt Handling
- ISR (Interrupt Service Routine)
- DPC (Deferred Procedure Call)
- Interrupt synchronization

---

## 📚 Tövsiyə olunan Mənbələr

### Kitablar:
1. **"Windows Kernel Programming"** - Pavel Yosifovich
2. **"Windows Internals"** - Mark Russinovich
3. **"Developing Drivers with the Windows Driver Foundation"** - Penny Orwick

### Online Resurslat:
- Microsoft Docs: https://docs.microsoft.com/en-us/windows-hardware/drivers/
- OSR Online: https://www.osronline.com/
- Windows Driver Samples: https://github.com/microsoft/Windows-driver-samples

### Alətlər:
- WinDbg Preview (Microsoft Store)
- DebugView (Sysinternals)
- OSR Driver Loader
- Process Monitor (Sysinternals)

---

## ✅ Nəticə və Məsləhətlər

### ✅ **TÖVSİYƏ EDİLİR:**
1. ✅ WDK + Visual Studio + MSVC toolchain
2. ✅ KMDF (Kernel Mode Driver Framework) istifadəsi
3. ✅ Virtual Machine-də test
4. ✅ WinDbg ilə debugging
5. ✅ Test signing ilə başlamaq
6. ✅ Kod review və best practices

### ❌ **TÖVSİYƏ EDİLMİR:**
1. ❌ GCC/MinGW kernel driver development üçün
2. ❌ Legacy WDM driver-lər (yeni proyektlər üçün)
3. ❌ Production sistemdə test etmək
4. ❌ İmzasız driver-ləri deploy etmək
5. ❌ Physical machine-də ilk testlər
6. ❌ Error handling olmadan kod yazmaq

---

## 📅 Təxmini Timeline

| Faza | Müddət | Təsvir |
|------|--------|--------|
| Faza 1 | 1 həftə | Mühit qurulması və nəzəriyyə |
| Faza 2 | 3-5 gün | Test mühiti |
| Faza 3 | 1 həftə | İlk driver proyekti |
| Faza 4 | 2 həftə | İmzalama öyrənmə |
| Faza 5 | 4-6 həftə | Ətraflı driver development |
| Faza 6 | Davamlı | Debugging skills |
| Faza 7 | 2-3 ay | İrəliləyən mövzular |

**Cəmi:** ~3-4 ay əsas bacarıqlar üçün, 6-12 ay professional səviyyə üçün

---

## 🎓 Son Məsləhət

**Microsoft-un rəsmi toolchain-indən istifadə edin!** Windows kernel development üçün bu, ən etibarlı və dəstəklənən yoldur. Sertifikat alın, test signing ilə başlayın və addım-addım irəliləyin. Tələsməyin və hər mərhələni yaxşı başa düşün.

**Uğurlar! 🚀**

---

*Bu plan Meslehet.md faylındaki məsləhətlərə əsasən hazırlanmışdır.*
*Son yenilənmə: 2026*
