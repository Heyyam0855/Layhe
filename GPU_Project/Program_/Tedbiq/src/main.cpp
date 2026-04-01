#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include "core/Application.h"

/**
 * @brief C++ Portfolio Layihəsinin əsas giriş nöqtəsi
 * 
 * Bu layihə bir proqramçının C++ bilik və bacarıqlarını nümayiş etdirmək
 * üçün yaradılmış comprehensive bir tədbiqdir.
 * 
 * Özəlliklər:
 * - Modular arxitektura
 * - Command-line interface
 * - Calculator module
 * - File management
 * - Data processing
 * 
 * @author [Sizin adınız]
 * @version 1.0.0
 * @date 2025
 */

void printWelcome() {
    std::cout << "===============================================\n";
    std::cout << "    C++ Portfolio Layihəsinə xoş gəlmisiniz!\n";
    std::cout << "===============================================\n";
    std::cout << "Bu layihə aşağıdakı modulları dəstəkləyir:\n";
    std::cout << "1. Calculator    - Həndəsi və ədədi hesablamalar\n";
    std::cout << "2. FileManager   - Fayl əməliyyatları\n";
    std::cout << "3. DataProcessor - Məlumat emalı və analizi\n";
    std::cout << "===============================================\n\n";
}

void printUsage(const std::string& programName) {
    std::cout << "İstifadə:\n";
    std::cout << "  " << programName << " [seçim]\n\n";
    std::cout << "Seçimlər:\n";
    std::cout << "  --help, -h        Bu kömək məlumatını göstər\n";
    std::cout << "  --version, -v     Versiya məlumatını göstər\n";
    std::cout << "  --calculator, -c  Calculator modulunu işə sal\n";
    std::cout << "  --filemanager, -f File Manager modulunu işə sal\n";
    std::cout << "  --dataprocessor, -d Data Processor modulunu işə sal\n";
    std::cout << "  --interactive, -i İnteraktiv rejimi başlat\n\n";
}

void printVersion() {
    std::cout << "C++ Portfolio Layihəsi v1.0.0\n";
    std::cout << "MinGW-w64/MSYS2 ilə tərtib edilib\n";
    std::cout << "Copyright (c) 2025\n";
}

int main(int argc, char* argv[]) {
    try {
        // Application obyektini yarat
        auto app = std::make_unique<Application>();
        
        // Əgər heç bir arqument verilməyibsə, welcome mesajını göstər
        if (argc == 1) {
            printWelcome();
            printUsage(argv[0]);
            return 0;
        }
        
        // Command line arqumentlərini işlə
        std::string argument = argv[1];
        
        if (argument == "--help" || argument == "-h") {
            printUsage(argv[0]);
            return 0;
        }
        else if (argument == "--version" || argument == "-v") {
            printVersion();
            return 0;
        }
        else if (argument == "--calculator" || argument == "-c") {
            std::cout << "Calculator modulu işə düşür...\n";
            return app->runCalculator();
        }
        else if (argument == "--filemanager" || argument == "-f") {
            std::cout << "File Manager modulu işə düşür...\n";
            return app->runFileManager();
        }
        else if (argument == "--dataprocessor" || argument == "-d") {
            std::cout << "Data Processor modulu işə düşür...\n";
            return app->runDataProcessor();
        }
        else if (argument == "--interactive" || argument == "-i") {
            std::cout << "İnteraktiv rejim başlayır...\n";
            return app->runInteractive();
        }
        else {
            std::cerr << "Xəta: Naməlum arqument '" << argument << "'\n";
            printUsage(argv[0]);
            return 1;
        }
        
    } catch (const std::exception& e) {
        std::cerr << "Xəta baş verdi: " << e.what() << std::endl;
        return 1;
    } catch (...) {
        std::cerr << "Naməlum xəta baş verdi!" << std::endl;
        return 1;
    }
    
    return 0;
}