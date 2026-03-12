#ifndef OUTPUT_FORMATTER_H
#define OUTPUT_FORMATTER_H

#include <string>
#include <vector>
#include <iostream>

namespace JavaAnalyzer {

/**
 * Terminal output-u üçün rəng kodları (ANSI)
 */
namespace Colors {
    const std::string RESET   = "\033[0m";
    const std::string RED     = "\033[31m";
    const std::string GREEN   = "\033[32m";
    const std::string YELLOW  = "\033[33m";
    const std::string BLUE    = "\033[34m";
    const std::string MAGENTA = "\033[35m";
    const std::string CYAN    = "\033[36m";
    const std::string BOLD    = "\033[1m";
}

/**
 * Output formatlaşdırma utility class-ı
 */
class OutputFormatter {
public:
    // Header çap edir
    static void PrintHeader(const std::string &title);
    
    // Bölmə xətti çap edir
    static void PrintSeparator(char symbol = '=', int length = 60);
    
    // Alt başlıq çap edir
    static void PrintSubHeader(const std::string &subtitle);
    
    // Siyahı elementi çap edir
    static void PrintListItem(const std::string &label, const std::string &value);
    
    // Vektordan siyahı çap edir
    static void PrintList(const std::string &title, const std::vector<std::string> &items);
    
    // Uğur mesajı çap edir
    static void PrintSuccess(const std::string &message);
    
    // Xəta mesajı çap edir
    static void PrintError(const std::string &message);
    
    // Məlumat mesajı çap edir
    static void PrintInfo(const std::string &message);
    
    // Cədvəl formatında məlumat çap edir
    static void PrintTable(const std::vector<std::string> &headers, 
                           const std::vector<std::vector<std::string>> &rows);
    
    // İstatistika çap edir
    static void PrintStatistics(const std::string &label, int value);
};

} // namespace JavaAnalyzer

#endif // OUTPUT_FORMATTER_H