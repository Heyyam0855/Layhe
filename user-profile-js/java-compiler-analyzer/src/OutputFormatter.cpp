#include "../include/OutputFormatter.h"
#include <iomanip>
#include <algorithm>

namespace JavaAnalyzer {

void OutputFormatter::PrintHeader(const std::string &title) {
    std::cout << Colors::BOLD << Colors::CYAN;
    PrintSeparator('=');
    std::cout << std::setw(30 + title.length()/2) << title << std::endl;
    PrintSeparator('=');
    std::cout << Colors::RESET << std::endl;
}

void OutputFormatter::PrintSeparator(char symbol, int length) {
    std::cout << std::string(length, symbol) << std::endl;
}

void OutputFormatter::PrintSubHeader(const std::string &subtitle) {
    std::cout << Colors::BOLD << Colors::YELLOW 
              << ">>> " << subtitle << " <<<" 
              << Colors::RESET << std::endl;
}

void OutputFormatter::PrintListItem(const std::string &label, const std::string &value) {
    std::cout << Colors::BLUE << std::setw(20) << std::left << label << ": " 
              << Colors::RESET << value << std::endl;
}

void OutputFormatter::PrintList(const std::string &title, const std::vector<std::string> &items) {
    if (items.empty()) {
        return;
    }
    
    PrintSubHeader(title);
    for (size_t i = 0; i < items.size(); ++i) {
        std::cout << Colors::GREEN << "  " << (i + 1) << ". " 
                  << Colors::RESET << items[i] << std::endl;
    }
    std::cout << std::endl;
}

void OutputFormatter::PrintSuccess(const std::string &message) {
    std::cout << Colors::GREEN << Colors::BOLD 
              << "[✓] " << message 
              << Colors::RESET << std::endl;
}

void OutputFormatter::PrintError(const std::string &message) {
    std::cout << Colors::RED << Colors::BOLD 
              << "[✗] " << message 
              << Colors::RESET << std::endl;
}

void OutputFormatter::PrintInfo(const std::string &message) {
    std::cout << Colors::CYAN 
              << "[ℹ] " << message 
              << Colors::RESET << std::endl;
}

void OutputFormatter::PrintTable(const std::vector<std::string> &headers, 
                                 const std::vector<std::vector<std::string>> &rows) {
    if (headers.empty() || rows.empty()) {
        return;
    }
    
    // Sütun genişliklərini hesabla
    std::vector<size_t> columnWidths(headers.size(), 0);
    
    for (size_t i = 0; i < headers.size(); ++i) {
        columnWidths[i] = std::max(columnWidths[i], headers[i].length());
    }
    
    for (const auto &row : rows) {
        for (size_t i = 0; i < std::min(row.size(), columnWidths.size()); ++i) {
            columnWidths[i] = std::max(columnWidths[i], row[i].length());
        }
    }
    
    // Header çap et
    std::cout << Colors::BOLD << Colors::BLUE;
    for (size_t i = 0; i < headers.size(); ++i) {
        std::cout << "| " << std::setw(columnWidths[i]) << std::left << headers[i] << " ";
    }
    std::cout << "|" << Colors::RESET << std::endl;
    
    // Separator çap et
    for (size_t i = 0; i < headers.size(); ++i) {
        std::cout << "+" << std::string(columnWidths[i] + 2, '-');
    }
    std::cout << "+" << std::endl;
    
    // Sətirləri çap et
    for (const auto &row : rows) {
        for (size_t i = 0; i < headers.size(); ++i) {
            std::string value = (i < row.size()) ? row[i] : "";
            std::cout << "| " << std::setw(columnWidths[i]) << std::left << value << " ";
        }
        std::cout << "|" << std::endl;
    }
}

void OutputFormatter::PrintStatistics(const std::string &label, int value) {
    std::cout << Colors::MAGENTA << "📊 " 
              << Colors::BOLD << label << ": " 
              << Colors::YELLOW << value 
              << Colors::RESET << std::endl;
}

} // namespace JavaAnalyzer