// UI Package - Go Implementation with Fyne GUI
// Proqramın dizaynı və interfeysi
// C++ çəkirdəyi ilə inteqrasiya (CGO hazır, DLL lazımdır)

package main

import (
	"fmt"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/widget"
)

// CoreApp - Go-da çəkirdək simulyasiyası
// C++ DLL hazır olduqda CGO ilə əvəz ediləcək
type CoreApp struct {
	version     string
	initialized bool
}

// NewCoreApp çəkirdək yaradır
func NewCoreApp() *CoreApp {
	return &CoreApp{
		version:     "1.0.0",
		initialized: false,
	}
}

// Initialize çəkirdəyi inisializasiya edir
func (c *CoreApp) Initialize() bool {
	fmt.Println("[INFO] Core initializing...")
	c.initialized = true
	fmt.Println("[INFO] Core initialized successfully")
	return true
}

// GetVersion versiyanı qaytarır
func (c *CoreApp) GetVersion() string {
	return c.version
}

// Shutdown çəkirdəyi bağlayır
func (c *CoreApp) Shutdown() {
	fmt.Println("[INFO] Core shutting down...")
	c.initialized = false
}

// Log log yazır
func (c *CoreApp) Log(level, message string) {
	fmt.Printf("[%s] %s\n", level, message)
}

// App represents the main UI application
type App struct {
	fyneApp    fyne.App
	mainWindow fyne.Window
	coreApp    *CoreApp
	Title      string
	Version    string
	Running    bool
	statusBar  *widget.Label
}

// NewApp creates a new application instance
func NewApp(title string) *App {
	return &App{
		Title:   title,
		Running: false,
	}
}

// Initialize prepares the UI components
func (a *App) Initialize() error {
	// Çəkirdəyi inisializasiya et
	a.coreApp = NewCoreApp()
	if !a.coreApp.Initialize() {
		return fmt.Errorf("çəkirdək inisializasiya edilə bilmədi")
	}

	// Versiyanı çəkirdəkdən al
	a.Version = a.coreApp.GetVersion()
	a.coreApp.Log("INFO", "Go UI initialized")

	// Fyne tətbiqini yarat
	a.fyneApp = app.New()

	// Əsas pəncərəni yarat - "APP" adı ilə
	a.mainWindow = a.fyneApp.NewWindow("APP")
	a.mainWindow.Resize(fyne.NewSize(800, 600))

	a.Running = true
	return nil
}

// Run starts the main UI loop
func (a *App) Run() {
	if !a.Running {
		return
	}

	// Başlıq
	titleLabel := widget.NewLabel("🚀 APP Proqramına Xoş Gəlmisiniz!")
	titleLabel.Alignment = fyne.TextAlignCenter
	titleLabel.TextStyle = fyne.TextStyle{Bold: true}

	// Versiya
	versionLabel := widget.NewLabel("Versiya: " + a.Version)
	versionLabel.Alignment = fyne.TextAlignCenter

	// Status bar
	a.statusBar = widget.NewLabel("✅ Hazır")
	a.statusBar.Alignment = fyne.TextAlignCenter

	// Düymələr
	btnNew := widget.NewButton("📄 Yeni", func() {
		a.statusBar.SetText("📄 Yeni fayl yaradıldı")
		a.coreApp.Log("INFO", "New file created")
		dialog.ShowInformation("Yeni", "Yeni fayl yaradıldı", a.mainWindow)
	})

	btnOpen := widget.NewButton("📂 Aç", func() {
		a.statusBar.SetText("📂 Fayl açılır...")
		a.coreApp.Log("INFO", "Opening file")
		dialog.ShowInformation("Aç", "Fayl açıldı", a.mainWindow)
	})

	btnSave := widget.NewButton("💾 Saxla", func() {
		a.statusBar.SetText("💾 Fayl saxlanıldı")
		a.coreApp.Log("INFO", "File saved")
		dialog.ShowInformation("Saxla", "Fayl saxlanıldı", a.mainWindow)
	})

	btnExit := widget.NewButton("🚪 Çıxış", func() {
		a.coreApp.Log("INFO", "Application exiting")
		a.Shutdown()
	})

	// Düymələri yan-yana düz
	buttonBox := container.NewHBox(btnNew, btnOpen, btnSave, btnExit)

	// Arxitektura məlumatı
	infoLabel := widget.NewLabel("🏗️ Arxitektura: Go UI + Core + SQLite")
	infoLabel.Alignment = fyne.TextAlignCenter

	// Əsas konteyner
	content := container.NewVBox(
		widget.NewLabel(""),
		titleLabel,
		versionLabel,
		widget.NewLabel(""),
		container.NewCenter(buttonBox),
		widget.NewLabel(""),
		infoLabel,
		widget.NewSeparator(),
		a.statusBar,
	)

	a.mainWindow.SetContent(container.NewCenter(content))
	a.mainWindow.ShowAndRun()
}

// Shutdown cleanly closes the application
func (a *App) Shutdown() {
	a.Running = false

	// Çəkirdəyi bağla
	if a.coreApp != nil {
		a.coreApp.Shutdown()
	}

	if a.fyneApp != nil {
		a.fyneApp.Quit()
	}
}

func main() {
	// Tətbiqi yarat
	myApp := NewApp("APP")

	// İnisializasiya et
	if err := myApp.Initialize(); err != nil {
		fmt.Printf("Xəta: %v\n", err)
		return
	}

	// Tətbiqi işə sal - "APP" pəncərəsi açılacaq
	myApp.Run()
}
