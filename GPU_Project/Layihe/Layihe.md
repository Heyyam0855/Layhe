# Layihə - Portfolio və C++ Desktop Tətbiqi

## Ümumi Məlumat

Bu layihə iki əsas komponentdən ibarətdir:
1. **Web Portfolio Saytı** - Peşəkar profili və işləri nümayiş etdirən veb sayt
2. **C++ Desktop Tətbiqi** - Qt6 C++ ilə hazırlanmış cross-platform masaüstü GUI proqramı

## 📋 Layihə Məqsədləri

### Web Portfolio
- Peşəkar brendinqin gücləndirilməsi
- Texniki bacarıqların nümayiş edilməsi
- İş imkanlarının artırılması
- Müştərilər və işəgötürənlər üçün etibarlı profil yaratmaq

### C++ Desktop Tətbiqi
- C++ GUI proqramlaşdırma bacarıqlarının nümayiş edilməsi
- Qt6 framework ilə cross-platform development təcrübəsi
- Modern C++ və professional development tools istifadəsi
- Portfolio layihəsinə əlavə bir güclü texniki komponent əlavə etmək

## 📁 Layihə Strukturu

```
Layihe/
├── Planlama/
│   ├── ideya.md                 # Əsas layihə ideyası
│   ├── layihe_plani.md         # Web portfolio icra planı
│   ├── texniki_plan.md         # Web portfolio texniki tələbləri
│   └── tkinter_plan.md         # C++ proqramı planı (yeniləndi)
├── portfolio-project/
│   ├── frontend/               # Web saytın frontend hissəsi
│   ├── backend/               # Web saytın backend hissəsi
│   └── admin/                 # Admin panel
└── cpp-task-manager/          # C++ desktop tətbiqi (yeni)
    ├── main.cpp
    ├── CMakeLists.txt
    ├── resources/
    │   ├── icons/
    │   └── styles/
    └── build/
```

## 🎯 Mərhələlər

### MƏRHƏLƏ 1: Web Portfolio (İcra edilir)
- ✅ Layihə strukturunun yaradılması
- ✅ Backend API hazırlanması
- ✅ Frontend interfeys hazırlanması
- ⏳ Admin panel sistemi
- ⏳ Test və optimallaşdırma

### MƏRHƏLƏ 2: C++ Desktop Tətbiqi (Planlanır)
- 📋 Qt6 framework quraşdırılması
- 📋 C++ kod strukturunun hazırlanması
- 📋 GUI komponentlərinin implementasiyası
- 📋 SQLite verilənlər bazası inteqrasiyası
- 📋 CRUD əməliyyatlarının tamamlanması
- 📋 Filter və axtarış funksiyalarının əlavə edilməsi
- 📋 Export/Import modullarının hazırlanması
- 📋 Test və debugging
- 📋 Build və deployment

## 📊 Hazırkı Vəziyyət

### Web Portfolio Layihəsi
- **Status**: Aktiv inkişaf mərhələsində
- **Texnologiyalar**: HTML5, CSS3, JavaScript, Python Flask, SQLite
- **Tamamlanma dərəcəsi**: ~70%

### C++ Desktop Tətbiqi
- **Status**: Planlaşdırma tamamlandı
- **Texnologiyalar**: Qt6 C++, SQLite, CMake
- **Tamamlanma dərəcəsi**: 10% (Kod strukturu hazır)

## 🚀 Növbəti Addımlar

1. **Qt6 framework quraşdırılması və inkişaf mühitinin hazırlanması**
2. **C++ main.cpp faylının ətraflı implementasiyası**
3. **SQLite verilənlər bazası funksiyalarının tamamlanması**
4. **Task Dialog pəncərələrinin hazırlanması**
5. **GUI komponentlərinin polish və style edilməsi**
6. **Portfolio saytına C++ layihəsini əlavə etmək**

## 📝 Qeydlər

- Hər iki layihə eyni zamanda inkişaf etdirilə bilər
- C++ tətbiqi portfolio saytında ayrıca layihə kimi təqdim ediləcək
- Qt6 modern C++ GUI framework üstünlükləri istifadə ediləcək
- Cross-platform uyğunluq (Windows, Linux, macOS) təmin ediləcək
- Kodlar GitHub repozitoriyasında saxlanılacaq
- CMake build system istifadə edərək professional development approach

## 🖥️ C++ Desktop Tətbiqi - Ətraflı Plan

### Tətbiq Konsepti
**Proqram adı**: "Personal Task Manager Pro"
**Məqsəd**: Şəxsi tapşırıq idarəetməsi və məhsuldarlıq artırma vasitəsi
**Framework**: Qt6 C++ GUI Framework

### Ana Funksiyalar
1. **Tapşırıq İdarəetməsi**
   - Yeni tapşırıq əlavə etmək
   - Tapşırıqları redaktə etmək
   - Tapşırıqları silmək
   - Prioritet və termin təyin etmək

2. **Kateqoriya Sistemi**
   - İş, şəxsi, təhsil kateqoriyaları
   - Xüsusi kateqoriya yaratma
   - Rəng kodlaması

3. **Proqres İzləmə**
   - Tamamlanma statusu
   - Statistika və hesabatlar
   - Vaxt takibi

4. **Data Saxlama**
   - SQLite verilənlər bazası
   - Backup və restore funksiyası
   - Data export (JSON, CSV)

### main.cpp Kod Strukturu

### main.cpp Kod Strukturu

```cpp
/*
 * Personal Task Manager Pro - Qt C++ Desktop Application
 * Author: Portfolio Project
 * Date: September 2025
 * Framework: Qt6
 */

#include <QtWidgets>
#include <QApplication>
#include <QMainWindow>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGridLayout>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QTextEdit>
#include <QComboBox>
#include <QTableWidget>
#include <QTableWidgetItem>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QGroupBox>
#include <QMenuBar>
#include <QStatusBar>
#include <QToolBar>
#include <QAction>
#include <QMessageBox>
#include <QFileDialog>
#include <QDateEdit>
#include <QProgressBar>
#include <QSplitter>
#include <QHeaderView>
#include <QtSql>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>
#include <QDateTime>
#include <QTimer>
#include <QSystemTrayIcon>

class TaskManagerApp : public QMainWindow
{
    Q_OBJECT

public:
    TaskManagerApp(QWidget *parent = nullptr);
    ~TaskManagerApp();

private slots:
    // Task management slots
    void addNewTask();
    void editTask();
    void deleteTask();
    void markTaskCompleted();
    void filterTasks();
    
    // Category management slots
    void manageCategories();
    void loadCategories();
    
    // File operations slots
    void exportToJson();
    void exportToCsv();
    void importFromFile();
    
    // View slots
    void showStatistics();
    void showAbout();
    void onTaskSelectionChanged();
    
    // Database slots
    void refreshTaskList();

private:
    // UI Setup methods
    void setupDatabase();
    void createMenuBar();
    void createToolBar();
    void createStatusBar();
    void createMainInterface();
    void createControlPanel();
    void createTaskPanel();
    void setupStyles();
    
    // Database methods
    bool initializeDatabase();
    void loadTasks();
    void insertDefaultCategories();
    
    // Task methods
    void addTaskToDatabase(const QString &title, const QString &description,
                          const QString &category, const QString &priority,
                          const QDate &dueDate);
    void updateTaskInDatabase(int taskId, const QString &title, 
                             const QString &description, const QString &category,
                             const QString &priority, const QDate &dueDate,
                             const QString &status);
    void deleteTaskFromDatabase(int taskId);
    
    // UI Components
    QWidget *centralWidget;
    QSplitter *mainSplitter;
    
    // Control Panel Components
    QGroupBox *controlGroup;
    QPushButton *addTaskBtn;
    QPushButton *editTaskBtn;
    QPushButton *deleteTaskBtn;
    QComboBox *filterCombo;
    QComboBox *categoryCombo;
    QLineEdit *searchEdit;
    
    // Task Panel Components
    QGroupBox *taskGroup;
    QTableWidget *taskTable;
    QLabel *taskCountLabel;
    QProgressBar *completionProgress;
    
    // Menu and toolbar
    QMenuBar *menuBar;
    QToolBar *toolBar;
    QStatusBar *statusBar;
    
    // Actions
    QAction *addTaskAction;
    QAction *editTaskAction;
    QAction *deleteTaskAction;
    QAction *exportJsonAction;
    QAction *exportCsvAction;
    QAction *statisticsAction;
    QAction *aboutAction;
    QAction *exitAction;
    
    // Database
    QSqlDatabase database;
    QString dbPath;
    
    // Data members
    QStringList categories;
    QStringList priorities;
    QStringList statuses;
    int currentTaskId;
};

TaskManagerApp::TaskManagerApp(QWidget *parent)
    : QMainWindow(parent)
    , currentTaskId(-1)
{
    // Initialize data lists
    priorities << "Aşağı" << "Orta" << "Yüksək" << "Kritik";
    statuses << "Gözləyir" << "İcra edilir" << "Tamamlanıb" << "Təxirə salınıb";
    
    // Setup application
    setWindowTitle("Personal Task Manager Pro");
    setWindowIcon(QIcon(":/icons/app_icon.png"));
    resize(1200, 800);
    setMinimumSize(900, 600);
    
    // Initialize components
    setupDatabase();
    createMenuBar();
    createToolBar();
    createStatusBar();
    createMainInterface();
    setupStyles();
    
    // Load data
    loadCategories();
    loadTasks();
    
    // Connect signals
    connect(taskTable, &QTableWidget::itemSelectionChanged,
            this, &TaskManagerApp::onTaskSelectionChanged);
    
    // Setup system tray (optional)
    if (QSystemTrayIcon::isSystemTrayAvailable()) {
        QSystemTrayIcon *trayIcon = new QSystemTrayIcon(this);
        trayIcon->setIcon(QIcon(":/icons/app_icon.png"));
        trayIcon->show();
    }
}

TaskManagerApp::~TaskManagerApp()
{
    if (database.isOpen()) {
        database.close();
    }
}

void TaskManagerApp::setupDatabase()
{
    // Initialize SQLite database
    database = QSqlDatabase::addDatabase("QSQLITE");
    dbPath = QApplication::applicationDirPath() + "/tasks.db";
    database.setDatabaseName(dbPath);
    
    if (!database.open()) {
        QMessageBox::critical(this, "Verilənlər Bazası Xətası",
                             "Verilənlər bazası açıla bilmədi: " + database.lastError().text());
        return;
    }
    
    initializeDatabase();
}

bool TaskManagerApp::initializeDatabase()
{
    QSqlQuery query;
    
    // Create tasks table
    QString createTasksTable = R"(
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT,
            priority TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'Gözləyir',
            created_date TEXT,
            completed_date TEXT
        )
    )";
    
    if (!query.exec(createTasksTable)) {
        QMessageBox::critical(this, "Xəta", "Tasks cədvəli yaradıla bilmədi: " + query.lastError().text());
        return false;
    }
    
    // Create categories table
    QString createCategoriesTable = R"(
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            color TEXT,
            description TEXT
        )
    )";
    
    if (!query.exec(createCategoriesTable)) {
        QMessageBox::critical(this, "Xəta", "Categories cədvəli yaradıla bilmədi: " + query.lastError().text());
        return false;
    }
    
    insertDefaultCategories();
    return true;
}

void TaskManagerApp::insertDefaultCategories()
{
    QSqlQuery query;
    QStringList defaultCategories = {
        "('İş', '#FF6B6B', 'İş ilə bağlı tapşırıqlar')",
        "('Şəxsi', '#4ECDC4', 'Şəxsi işlər')",
        "('Təhsil', '#45B7D1', 'Təhsil və öyrənmə')",
        "('Sağlamlıq', '#96CEB4', 'Sağlamlıq və idman')"
    };
    
    for (const QString &category : defaultCategories) {
        query.exec("INSERT OR IGNORE INTO categories (name, color, description) VALUES " + category);
    }
}

void TaskManagerApp::createMenuBar()
{
    // File Menu
    QMenu *fileMenu = menuBar()->addMenu("&Fayl");
    
    addTaskAction = new QAction("&Yeni Tapşırıq", this);
    addTaskAction->setShortcut(QKeySequence::New);
    addTaskAction->setStatusTip("Yeni tapşırıq əlavə et");
    connect(addTaskAction, &QAction::triggered, this, &TaskManagerApp::addNewTask);
    fileMenu->addAction(addTaskAction);
    
    fileMenu->addSeparator();
    
    exportJsonAction = new QAction("&JSON Export", this);
    connect(exportJsonAction, &QAction::triggered, this, &TaskManagerApp::exportToJson);
    fileMenu->addAction(exportJsonAction);
    
    exportCsvAction = new QAction("&CSV Export", this);
    connect(exportCsvAction, &QAction::triggered, this, &TaskManagerApp::exportToCsv);
    fileMenu->addAction(exportCsvAction);
    
    fileMenu->addSeparator();
    
    exitAction = new QAction("Ç&ıxış", this);
    exitAction->setShortcut(QKeySequence::Quit);
    connect(exitAction, &QAction::triggered, this, &QWidget::close);
    fileMenu->addAction(exitAction);
    
    // Edit Menu
    QMenu *editMenu = menuBar()->addMenu("&Redaktə");
    
    editTaskAction = new QAction("&Redaktə et", this);
    editTaskAction->setShortcut(QKeySequence("Ctrl+E"));
    connect(editTaskAction, &QAction::triggered, this, &TaskManagerApp::editTask);
    editMenu->addAction(editTaskAction);
    
    deleteTaskAction = new QAction("&Sil", this);
    deleteTaskAction->setShortcut(QKeySequence::Delete);
    connect(deleteTaskAction, &QAction::triggered, this, &TaskManagerApp::deleteTask);
    editMenu->addAction(deleteTaskAction);
    
    // Tools Menu
    QMenu *toolsMenu = menuBar()->addMenu("&Alətlər");
    
    QAction *categoriesAction = new QAction("&Kateqoriyalar", this);
    connect(categoriesAction, &QAction::triggered, this, &TaskManagerApp::manageCategories);
    toolsMenu->addAction(categoriesAction);
    
    statisticsAction = new QAction("&Statistika", this);
    connect(statisticsAction, &QAction::triggered, this, &TaskManagerApp::showStatistics);
    toolsMenu->addAction(statisticsAction);
    
    // Help Menu
    QMenu *helpMenu = menuBar()->addMenu("&Kömək");
    
    aboutAction = new QAction("&Haqqında", this);
    connect(aboutAction, &QAction::triggered, this, &TaskManagerApp::showAbout);
    helpMenu->addAction(aboutAction);
}

void TaskManagerApp::createToolBar()
{
    toolBar = addToolBar("Əsas");
    toolBar->addAction(addTaskAction);
    toolBar->addAction(editTaskAction);
    toolBar->addAction(deleteTaskAction);
    toolBar->addSeparator();
    toolBar->addAction(statisticsAction);
}

void TaskManagerApp::createStatusBar()
{
    statusBar = QMainWindow::statusBar();
    taskCountLabel = new QLabel("Tapşırıqlar: 0");
    statusBar->addWidget(taskCountLabel);
    
    completionProgress = new QProgressBar();
    completionProgress->setMaximumWidth(200);
    statusBar->addPermanentWidget(completionProgress);
}

void TaskManagerApp::createMainInterface()
{
    centralWidget = new QWidget();
    setCentralWidget(centralWidget);
    
    mainSplitter = new QSplitter(Qt::Horizontal);
    
    createControlPanel();
    createTaskPanel();
    
    mainSplitter->addWidget(controlGroup);
    mainSplitter->addWidget(taskGroup);
    mainSplitter->setStretchFactor(0, 0);
    mainSplitter->setStretchFactor(1, 1);
    
    QHBoxLayout *mainLayout = new QHBoxLayout();
    mainLayout->addWidget(mainSplitter);
    centralWidget->setLayout(mainLayout);
}

void TaskManagerApp::createControlPanel()
{
    controlGroup = new QGroupBox("Kontrollar");
    QVBoxLayout *controlLayout = new QVBoxLayout();
    
    // Add task button
    addTaskBtn = new QPushButton("Yeni Tapşırıq");
    addTaskBtn->setMinimumHeight(40);
    connect(addTaskBtn, &QPushButton::clicked, this, &TaskManagerApp::addNewTask);
    controlLayout->addWidget(addTaskBtn);
    
    // Edit task button
    editTaskBtn = new QPushButton("Redaktə et");
    connect(editTaskBtn, &QPushButton::clicked, this, &TaskManagerApp::editTask);
    controlLayout->addWidget(editTaskBtn);
    
    // Delete task button
    deleteTaskBtn = new QPushButton("Sil");
    connect(deleteTaskBtn, &QPushButton::clicked, this, &TaskManagerApp::deleteTask);
    controlLayout->addWidget(deleteTaskBtn);
    
    controlLayout->addSpacing(20);
    
    // Filters
    QLabel *filterLabel = new QLabel("Filter:");
    filterLabel->setStyleSheet("font-weight: bold;");
    controlLayout->addWidget(filterLabel);
    
    filterCombo = new QComboBox();
    filterCombo->addItems({"Hamısı", "Gözləyir", "İcra edilir", "Tamamlanıb", "Gecikmiş"});
    connect(filterCombo, QOverload<int>::of(&QComboBox::currentIndexChanged),
            this, &TaskManagerApp::filterTasks);
    controlLayout->addWidget(filterCombo);
    
    QLabel *categoryLabel = new QLabel("Kateqoriya:");
    categoryLabel->setStyleSheet("font-weight: bold;");
    controlLayout->addWidget(categoryLabel);
    
    categoryCombo = new QComboBox();
    connect(categoryCombo, QOverload<int>::of(&QComboBox::currentIndexChanged),
            this, &TaskManagerApp::filterTasks);
    controlLayout->addWidget(categoryCombo);
    
    // Search
    QLabel *searchLabel = new QLabel("Axtarış:");
    searchLabel->setStyleSheet("font-weight: bold;");
    controlLayout->addWidget(searchLabel);
    
    searchEdit = new QLineEdit();
    searchEdit->setPlaceholderText("Tapşırıq axtar...");
    connect(searchEdit, &QLineEdit::textChanged, this, &TaskManagerApp::filterTasks);
    controlLayout->addWidget(searchEdit);
    
    controlLayout->addStretch();
    controlGroup->setLayout(controlLayout);
    controlGroup->setMaximumWidth(250);
}

void TaskManagerApp::createTaskPanel()
{
    taskGroup = new QGroupBox("Tapşırıqlar");
    QVBoxLayout *taskLayout = new QVBoxLayout();
    
    // Task table
    taskTable = new QTableWidget();
    taskTable->setColumnCount(6);
    
    QStringList headers = {"ID", "Başlıq", "Kateqoriya", "Prioritet", "Termin", "Status"};
    taskTable->setHorizontalHeaderLabels(headers);
    
    // Configure table
    taskTable->setSelectionBehavior(QAbstractItemView::SelectRows);
    taskTable->setAlternatingRowColors(true);
    taskTable->setSortingEnabled(true);
    taskTable->horizontalHeader()->setStretchLastSection(true);
    taskTable->setColumnHidden(0, true); // Hide ID column
    
    taskLayout->addWidget(taskTable);
    taskGroup->setLayout(taskLayout);
}

void TaskManagerApp::setupStyles()
{
    setStyleSheet(R"(
        QMainWindow {
            background-color: #f5f5f5;
        }
        QGroupBox {
            font-weight: bold;
            border: 2px solid #cccccc;
            border-radius: 5px;
            margin-top: 1ex;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
        }
        QPushButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 8px 16px;
            text-align: center;
            font-size: 14px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #3d8b40;
        }
        QTableWidget {
            gridline-color: #d0d0d0;
            background-color: white;
        }
        QTableWidget::item:selected {
            background-color: #0078d4;
            color: white;
        }
    )");
}

// Slot implementations
void TaskManagerApp::addNewTask()
{
    // Implementation for add task dialog
    QMessageBox::information(this, "Məlumat", "Yeni tapşırıq əlavə etmə funksiyası tezliklə əlavə ediləcək");
}

void TaskManagerApp::editTask()
{
    // Implementation for edit task
    int currentRow = taskTable->currentRow();
    if (currentRow < 0) {
        QMessageBox::warning(this, "Xəbərdarlıq", "Redaktə etmək üçün tapşırıq seçin");
        return;
    }
    QMessageBox::information(this, "Məlumat", "Tapşırıq redaktəsi funksiyası tezliklə əlavə ediləcək");
}

void TaskManagerApp::deleteTask()
{
    // Implementation for delete task
    int currentRow = taskTable->currentRow();
    if (currentRow < 0) {
        QMessageBox::warning(this, "Xəbərdarlıq", "Silmək üçün tapşırıq seçin");
        return;
    }
    
    int reply = QMessageBox::question(this, "Təsdiq", "Seçilmiş tapşırığı silmək istədiyinizə əminsiniz?",
                                      QMessageBox::Yes | QMessageBox::No);
    if (reply == QMessageBox::Yes) {
        // Delete implementation
        QMessageBox::information(this, "Məlumat", "Tapşırıq silmə funksiyası tezliklə əlavə ediləcək");
    }
}

void TaskManagerApp::markTaskCompleted()
{
    // Implementation for marking task as completed
}

void TaskManagerApp::filterTasks()
{
    // Implementation for filtering tasks
}

void TaskManagerApp::manageCategories()
{
    QMessageBox::information(this, "Məlumat", "Kateqoriya idarəetməsi funksiyası tezliklə əlavə ediləcək");
}

void TaskManagerApp::loadCategories()
{
    categoryCombo->clear();
    categoryCombo->addItem("Hamısı");
    
    QSqlQuery query("SELECT name FROM categories ORDER BY name");
    while (query.next()) {
        categoryCombo->addItem(query.value(0).toString());
    }
}

void TaskManagerApp::exportToJson()
{
    QString fileName = QFileDialog::getSaveFileName(this, "JSON Export", "", "JSON Files (*.json)");
    if (!fileName.isEmpty()) {
        QMessageBox::information(this, "Məlumat", "JSON export funksiyası tezliklə əlavə ediləcək");
    }
}

void TaskManagerApp::exportToCsv()
{
    QString fileName = QFileDialog::getSaveFileName(this, "CSV Export", "", "CSV Files (*.csv)");
    if (!fileName.isEmpty()) {
        QMessageBox::information(this, "Məlumat", "CSV export funksiyası tezliklə əlavə ediləcək");
    }
}

void TaskManagerApp::showStatistics()
{
    QMessageBox::information(this, "Məlumat", "Statistika funksiyası tezliklə əlavə ediləcək");
}

void TaskManagerApp::showAbout()
{
    QMessageBox::about(this, "Haqqında",
        "Personal Task Manager Pro v1.0\n"
        "Portfolio Layihəsi\n"
        "Qt6 C++ ilə hazırlanıb\n\n"
        "Müəllif: GitHub Copilot Assistant");
}

void TaskManagerApp::onTaskSelectionChanged()
{
    bool hasSelection = taskTable->currentRow() >= 0;
    editTaskBtn->setEnabled(hasSelection);
    deleteTaskBtn->setEnabled(hasSelection);
    editTaskAction->setEnabled(hasSelection);
    deleteTaskAction->setEnabled(hasSelection);
}

void TaskManagerApp::refreshTaskList()
{
    loadTasks();
}

void TaskManagerApp::loadTasks()
{
    taskTable->setRowCount(0);
    
    QSqlQuery query("SELECT id, title, category, priority, due_date, status FROM tasks ORDER BY created_date DESC");
    
    int row = 0;
    while (query.next()) {
        taskTable->insertRow(row);
        
        // ID (hidden)
        taskTable->setItem(row, 0, new QTableWidgetItem(query.value(0).toString()));
        
        // Title
        taskTable->setItem(row, 1, new QTableWidgetItem(query.value(1).toString()));
        
        // Category
        taskTable->setItem(row, 2, new QTableWidgetItem(query.value(2).toString()));
        
        // Priority
        QTableWidgetItem *priorityItem = new QTableWidgetItem(query.value(3).toString());
        QString priority = query.value(3).toString();
        if (priority == "Kritik") {
            priorityItem->setBackground(QColor("#ff4444"));
            priorityItem->setForeground(QColor("white"));
        } else if (priority == "Yüksək") {
            priorityItem->setBackground(QColor("#ff8800"));
            priorityItem->setForeground(QColor("white"));
        }
        taskTable->setItem(row, 3, priorityItem);
        
        // Due Date
        taskTable->setItem(row, 4, new QTableWidgetItem(query.value(4).toString()));
        
        // Status
        QTableWidgetItem *statusItem = new QTableWidgetItem(query.value(5).toString());
        QString status = query.value(5).toString();
        if (status == "Tamamlanıb") {
            statusItem->setBackground(QColor("#4CAF50"));
            statusItem->setForeground(QColor("white"));
        } else if (status == "İcra edilir") {
            statusItem->setBackground(QColor("#2196F3"));
            statusItem->setForeground(QColor("white"));
        }
        taskTable->setItem(row, 5, statusItem);
        
        row++;
    }
    
    // Update status bar
    taskCountLabel->setText(QString("Tapşırıqlar: %1").arg(row));
    
    // Update completion progress
    QSqlQuery completedQuery("SELECT COUNT(*) FROM tasks WHERE status = 'Tamamlanıb'");
    int completedCount = 0;
    if (completedQuery.next()) {
        completedCount = completedQuery.value(0).toInt();
    }
    
    if (row > 0) {
        int percentage = (completedCount * 100) / row;
        completionProgress->setValue(percentage);
        completionProgress->setFormat(QString("Tamamlanma: %1%").arg(percentage));
    } else {
        completionProgress->setValue(0);
        completionProgress->setFormat("Tamamlanma: 0%");
    }
}

// Main function
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    
    // Set application properties
    app.setApplicationName("Personal Task Manager Pro");
    app.setApplicationVersion("1.0");
    app.setOrganizationName("Portfolio Project");
    
    // Create and show main window
    TaskManagerApp window;
    window.show();
    
    return app.exec();
}

// Include the MOC file for Qt's meta-object system
#include "main.moc"
```

### CMakeLists.txt Faylı

```cmake
cmake_minimum_required(VERSION 3.16)

project(PersonalTaskManager VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Qt6 components
find_package(Qt6 REQUIRED COMPONENTS Core Widgets Sql)

# Create executable
add_executable(PersonalTaskManager
    main.cpp
)

# Link Qt6 libraries
target_link_libraries(PersonalTaskManager
    Qt6::Core
    Qt6::Widgets
    Qt6::Sql
)

# Enable Qt6 MOC (Meta-Object Compiler)
set_target_properties(PersonalTaskManager PROPERTIES
    AUTOMOC ON
)

# Windows specific settings
if(WIN32)
    set_target_properties(PersonalTaskManager PROPERTIES
        WIN32_EXECUTABLE TRUE
    )
endif()
```

### Proyektin Qurulması

```bash
# Qt6 quraşdırın
# Windows üçün: https://www.qt.io/download
# Linux üçün: sudo apt-get install qt6-base-dev qt6-tools-dev cmake

# Proyekti build edin
mkdir build
cd build
cmake ..
cmake --build .

# Windows üçün
.\PersonalTaskManager.exe

# Linux üçün
./PersonalTaskManager
```

### GUI Komponentləri

1. **Ana Pəncərə**
   - Menu bar (Fayl, Alətlər, Kömək)
   - Sol panel: kontrollar və filterlər
   - Sağ panel: tapşırıq siyahısı (TreeView)

2. **Dialog Pəncərələri**
   - Yeni tapşırıq əlavə etmə
   - Tapşırıq redaktəsi
   - Kateqoriya idarəetməsi
   - Statistika görüntüləmə

3. **Data Strukturu**
   - SQLite verilənlər bazası
   - İki cədvəl: tasks və categories
   - JSON/CSV export funksiyaları

### Texniki Xüsusiyyətlər

- **GUI Framework**: Qt6 C++
- **Verilənlər Bazası**: SQLite3 (QtSql)
- **Build System**: CMake
- **C++ Standard**: C++17
- **Fayl Formatları**: JSON, CSV export (QJsonDocument)
- **Tarih İşləmə**: QDateTime, QDate
- **Stil və Tema**: Qt StyleSheets
- **Sistem Tray**: QSystemTrayIcon dəstəyi

### Qt6 C++ Komponentləri

1. **QMainWindow** - Ana pəncərə
2. **QTableWidget** - Tapşırıq siyahısı
3. **QSplitter** - Panel ayırıcı
4. **QGroupBox** - Kontrol qrupları
5. **QComboBox** - Filter və kateqoriya seçimi
6. **QPushButton** - Əməliyyat düymələri
7. **QMenuBar** - Menu sistemi
8. **QStatusBar** - Status məlumatları
9. **QSqlDatabase** - Verilənlər bazası əlaqəsi
10. **QJsonDocument** - JSON export/import

### Layihə Faylları

```
cpp-task-manager/
├── main.cpp                    # Ana C++ faylı
├── CMakeLists.txt             # CMake build faylı
├── resources/
│   ├── icons/
│   │   ├── app_icon.png
│   │   ├── add_task.png
│   │   ├── edit_task.png
│   │   └── delete_task.png
│   └── styles/
│       └── app_styles.qss     # Qt StyleSheet
├── build/                     # Build direktory
└── tasks.db                   # SQLite verilənlər bazası
```

### İnkişaf Addımları

1. ✅ C++ kod strukturunun planlaşdırılması
2. ✅ Qt6 dependencies və CMake konfiqurasiyası
3. 📋 GUI komponentlərinin detallı implementasiyası
4. 📋 Database CRUD əməliyyatlarının tamamlanması
5. 📋 Task Dialog pəncərələrinin hazırlanması
6. 📋 Filter və axtarış funksiyalarının implementasiyası
7. 📋 JSON/CSV export funksiyalarının hazırlanması
8. 📋 Category management dialog
9. 📋 Statistics və reporting modulları
10. 📋 Qt StyleSheet və UI polish
11. 📋 Error handling və validation
12. 📋 Build və deployment test
13. 📋 Icon və resource fayllarının əlavə edilməsi
14. 📋 Documentation və kod şərhləri

### Qt6 Quraşdırma və Build

**Windows:**
```bash
# Qt6 installer endirin: https://www.qt.io/download
# Visual Studio və CMake quraşdırın
# Terminal-da:
mkdir build && cd build
cmake .. -DQt6_DIR="C:/Qt/6.5.0/msvc2019_64/lib/cmake/Qt6"
cmake --build . --config Release
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install qt6-base-dev qt6-tools-dev cmake build-essential
mkdir build && cd build
cmake ..
make -j4
```

**macOS:**
```bash
brew install qt6 cmake
mkdir build && cd build
cmake ..
make -j4
```

---

**Son yenilənmə**: 12 Sentyabr 2025
**İcraçı**: GitHub Copilot Assistant
**Layihə statusu**: Aktiv inkişaf