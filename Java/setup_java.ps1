# PowerShell Script to Install OpenJDK using WinGet
# Run as Administrator

Write-Host "=== OpenJDK Quraşdırma Skripti ===" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "⚠️  Bu skript Administrator hüquqları ilə işə salınmalıdır!" -ForegroundColor Red
    Write-Host "PowerShell-i sağ klik edib 'Run as Administrator' seçin" -ForegroundColor Yellow
    pause
    exit
}

Write-Host "✅ Administrator hüquqları təsdiqləndi" -ForegroundColor Green
Write-Host ""

# Check if WinGet is available
$wingetPath = Get-Command winget -ErrorAction SilentlyContinue

if ($wingetPath) {
    Write-Host "✅ WinGet tapıldı" -ForegroundColor Green
    Write-Host ""
    
    Write-Host "📥 OpenJDK (Temurin 21 LTS) quraşdırılır..." -ForegroundColor Cyan
    Write-Host ""
    
    # Install OpenJDK
    winget install EclipseAdoptium.Temurin.21.JDK --silent --accept-package-agreements --accept-source-agreements
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ OpenJDK uğurla quraşdırıldı!" -ForegroundColor Green
        Write-Host ""
        
        # Try to find Java installation
        $javaPath = "C:\Program Files\Eclipse Adoptium\jdk-21.*-hotspot"
        $javaDirs = Get-ChildItem -Path "C:\Program Files\Eclipse Adoptium" -Directory -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "jdk-21*" }
        
        if ($javaDirs) {
            $javaHome = $javaDirs[0].FullName
            Write-Host "📁 Java quraşdırma yolu: $javaHome" -ForegroundColor Cyan
            
            # Set JAVA_HOME
            [System.Environment]::SetEnvironmentVariable("JAVA_HOME", $javaHome, "Machine")
            Write-Host "✅ JAVA_HOME təyin edildi" -ForegroundColor Green
            
            # Add to PATH
            $currentPath = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
            if ($currentPath -notlike "*$javaHome\bin*") {
                $newPath = $currentPath + ";$javaHome\bin"
                [System.Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
                Write-Host "✅ PATH yeniləndi" -ForegroundColor Green
            }
        }
        
        Write-Host ""
        Write-Host "🎉 Quraşdırma tamamlandı!" -ForegroundColor Green
        Write-Host ""
        Write-Host "⚠️  ÖNƏMLI: Bütün açıq terminalları bağlayıb yenidən açın!" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Yoxlamaq üçün yeni terminalde bu əmrləri icra edin:" -ForegroundColor Cyan
        Write-Host "  java -version" -ForegroundColor White
        Write-Host "  javac -version" -ForegroundColor White
        
    } else {
        Write-Host ""
        Write-Host "❌ Quraşdırma xətası!" -ForegroundColor Red
        Write-Host "Manual olaraq quraşdırın: https://adoptium.net/" -ForegroundColor Yellow
    }
    
} else {
    Write-Host "❌ WinGet tapılmadı!" -ForegroundColor Red
    Write-Host ""
    Write-Host "WinGet yükləmək üçün:" -ForegroundColor Yellow
    Write-Host "1. Microsoft Store-dan 'App Installer' yükləyin" -ForegroundColor White
    Write-Host "2. Və ya bu linke keçid edin:" -ForegroundColor White
    Write-Host "   https://aka.ms/getwinget" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Alternativ: Manual olaraq OpenJDK quraşdırın" -ForegroundColor Yellow
    Write-Host "   https://adoptium.net/" -ForegroundColor Cyan
}

Write-Host ""
pause
