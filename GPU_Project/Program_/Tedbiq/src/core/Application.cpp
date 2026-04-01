#include "../include/Application.h"
#include <iostream>
#include <string>
#include <sstream>
#include <memory>
#include <stdexcept>

// Forward declarations for modules
class Application::Calculator {
public:
    void run() {
        std::cout << "=== Calculator Modulu ===\n";
        std::cout << "Sadə hesablayıcı (+ - * / işləmləri)\n";
        std::cout << "Çıxış üçün 'quit' yazın\n\n";
        
        std::string input;
        while (true) {
            std::cout << "Hesablama daxil edin: ";
            std::getline(std::cin, input);
            
            if (input == "quit" || input == "q") {
                break;
            }
            
            if (input.empty()) {
                continue;
            }
            
            try {
                double result = parseAndCalculate(input);
                std::cout << "Nəticə: " << result << "\n\n";
            } catch (const std::exception& e) {
                std::cout << "Xəta: " << e.what() << "\n\n";
            }
        }
    }

private:
    double parseAndCalculate(const std::string& expression) {
        std::istringstream iss(expression);
        double a, b;
        char op;
        
        if (!(iss >> a >> op >> b)) {
            throw std::invalid_argument("Yanlış format. Nümunə: 5 + 3");
        }
        
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': 
                if (b == 0) throw std::invalid_argument("Sıfıra bölmə mümkün deyil");
                return a / b;
            default:
                throw std::invalid_argument("Dəstəklənməyən operator: " + std::string(1, op));
        }
    }
};

class Application::FileManager {
public:
    void run() {
        std::cout << "=== File Manager Modulu ===\n";
        std::cout << "Fayl əməliyyatları (list, create, delete)\n";
        std::cout << "Çıxış üçün 'quit' yazın\n\n";
        
        std::string command;
        while (true) {
            std::cout << "Komanda daxil edin (list/create/delete/help): ";
            std::getline(std::cin, command);
            
            if (command == "quit" || command == "q") {
                break;
            }
            
            if (command == "help") {
                printHelp();
            } else if (command == "list") {
                listFiles();
            } else if (command.substr(0, 6) == "create") {
                createFile(command);
            } else if (command.substr(0, 6) == "delete") {
                deleteFile(command);
            } else {
                std::cout << "Naməlum komanda. 'help' yazın.\n\n";
            }
        }
    }

private:
    void printHelp() {
        std::cout << "Mövcud komandalar:\n";
        std::cout << "  list                - Cari qovluqdakı faylları siyahıla\n";
        std::cout << "  create <filename>   - Yeni fayl yarat\n";
        std::cout << "  delete <filename>   - Faylı sil\n";
        std::cout << "  help                - Bu kömək məlumatını göstər\n";
        std::cout << "  quit                - Çıxış\n\n";
    }
    
    void listFiles() {
        std::cout << "Fayl siyahılanması funksiyası (TODO: filesystem implementasiyası)\n\n";
    }
    
    void createFile(const std::string& command) {
        std::cout << "Fayl yaratma funksiyası (TODO: implementasiya)\n";
        std::cout << "Komanda: " << command << "\n\n";
    }
    
    void deleteFile(const std::string& command) {
        std::cout << "Fayl silmə funksiyası (TODO: implementasiya)\n";
        std::cout << "Komanda: " << command << "\n\n";
    }
};

class Application::DataProcessor {
public:
    void run() {
        std::cout << "=== Data Processor Modulu ===\n";
        std::cout << "Məlumat emalı və analizi\n";
        std::cout << "Çıxış üçün 'quit' yazın\n\n";
        
        std::string input;
        while (true) {
            std::cout << "Məlumat daxil edin (ədədlər boşluqla ayrılmış): ";
            std::getline(std::cin, input);
            
            if (input == "quit" || input == "q") {
                break;
            }
            
            if (input.empty()) {
                continue;
            }
            
            try {
                processData(input);
            } catch (const std::exception& e) {
                std::cout << "Xəta: " << e.what() << "\n\n";
            }
        }
    }

private:
    void processData(const std::string& input) {
        std::istringstream iss(input);
        std::vector<double> data;
        double value;
        
        while (iss >> value) {
            data.push_back(value);
        }
        
        if (data.empty()) {
            throw std::invalid_argument("Heç bir ədəd tapılmadı");
        }
        
        double sum = 0;
        double min = data[0];
        double max = data[0];
        
        for (double val : data) {
            sum += val;
            if (val < min) min = val;
            if (val > max) max = val;
        }
        
        double average = sum / data.size();
        
        std::cout << "Analiz nəticələri:\n";
        std::cout << "  Element sayı: " << data.size() << "\n";
        std::cout << "  Cəm: " << sum << "\n";
        std::cout << "  Ortalama: " << average << "\n";
        std::cout << "  Minimum: " << min << "\n";
        std::cout << "  Maksimum: " << max << "\n\n";
    }
};

// Application class implementation
Application::Application() 
    : m_appName("C++ Portfolio Layihəsi")
    , m_version("1.0.0")
    , m_isRunning(false) {
    initializeModules();
}

Application::~Application() {
    // Smart pointers avtomatik olaraq sərbəst buraxılacaq
}

void Application::initializeModules() {
    try {
        m_calculator = std::make_unique<Calculator>();
        m_fileManager = std::make_unique<FileManager>();
        m_dataProcessor = std::make_unique<DataProcessor>();
        m_isRunning = true;
    } catch (const std::exception& e) {
        std::cerr << "Modulları initialize edərkən xəta: " << e.what() << std::endl;
        m_isRunning = false;
    }
}

int Application::runCalculator() {
    if (!m_calculator) {
        std::cerr << "Calculator modulu initialize edilməyib!\n";
        return 1;
    }
    
    try {
        m_calculator->run();
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Calculator xətası: " << e.what() << std::endl;
        return 1;
    }
}

int Application::runFileManager() {
    if (!m_fileManager) {
        std::cerr << "FileManager modulu initialize edilməyib!\n";
        return 1;
    }
    
    try {
        m_fileManager->run();
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "FileManager xətası: " << e.what() << std::endl;
        return 1;
    }
}

int Application::runDataProcessor() {
    if (!m_dataProcessor) {
        std::cerr << "DataProcessor modulu initialize edilməyib!\n";
        return 1;
    }
    
    try {
        m_dataProcessor->run();
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "DataProcessor xətası: " << e.what() << std::endl;
        return 1;
    }
}

int Application::runInteractive() {
    std::cout << "İnteraktiv rejim başladı!\n\n";
    
    std::string command;
    while (true) {
        showInteractiveMenu();
        std::cout << "Seçiminiz: ";
        std::getline(std::cin, command);
        
        if (!processInteractiveCommand(command)) {
            break;
        }
    }
    
    std::cout << "Təşəkkürlər!\n";
    return 0;
}

void Application::showInteractiveMenu() {
    std::cout << "\n=== İnteraktiv Menyu ===\n";
    std::cout << "1. Calculator\n";
    std::cout << "2. File Manager\n";
    std::cout << "3. Data Processor\n";
    std::cout << "4. Self Test\n";
    std::cout << "0. Çıxış\n";
    std::cout << "========================\n";
}

bool Application::processInteractiveCommand(const std::string& command) {
    if (command == "1") {
        runCalculator();
    } else if (command == "2") {
        runFileManager();
    } else if (command == "3") {
        runDataProcessor();
    } else if (command == "4") {
        if (selfTest()) {
            std::cout << "Bütün testlər uğurla keçdi! ✓\n";
        } else {
            std::cout << "Bəzi testlər uğursuz oldu! ✗\n";
        }
    } else if (command == "0" || command == "quit" || command == "q") {
        return false;
    } else {
        std::cout << "Yanlış seçim! Zəhmət olmasa 0-4 arası rəqəm daxil edin.\n";
    }
    return true;
}

bool Application::selfTest() {
    std::cout << "Self test başlayır...\n";
    
    bool allPassed = true;
    
    // Calculator test
    std::cout << "Calculator modulu test edilir... ";
    if (m_calculator) {
        std::cout << "✓\n";
    } else {
        std::cout << "✗\n";
        allPassed = false;
    }
    
    // FileManager test
    std::cout << "FileManager modulu test edilir... ";
    if (m_fileManager) {
        std::cout << "✓\n";
    } else {
        std::cout << "✗\n";
        allPassed = false;
    }
    
    // DataProcessor test
    std::cout << "DataProcessor modulu test edilir... ";
    if (m_dataProcessor) {
        std::cout << "✓\n";
    } else {
        std::cout << "✗\n";
        allPassed = false;
    }
    
    return allPassed;
}