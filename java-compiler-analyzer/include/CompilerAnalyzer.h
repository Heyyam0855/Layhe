#ifndef COMPILER_ANALYZER_H
#define COMPILER_ANALYZER_H

#include "JavaAnalyzer.h"
#include "OutputFormatter.h"
#include <string>
#include <memory>

namespace JavaAnalyzer {

/**
 * Kompilyator analiz alətinin əsas class-ı
 * Java source fayllarını analiz edib kompilyasiya məlumatlarını toplayır
 */
class CompilerAnalyzer {
private:
    std::string sourceFile;
    CompilationInfo compilationInfo;
    bool verbose;

public:
    /**
     * Constructor
     * @param file - Analiz ediləcək fayl yolu
     * @param verbose - Ətraflı output flag-ı
     */
    explicit CompilerAnalyzer(const std::string &file, bool verbose = false);
    
    /**
     * Analizi başladır
     * @return Uğurlu olarsa true, əks halda false
     */
    bool Analyze();
    
    /**
     * Analiz nəticələrini göstərir
     */
    void DisplayResults() const;
    
    /**
     * Kompilyasiya mərhələlərini göstərir
     */
    void ShowCompilationStages() const;
    
    /**
     * AST (Abstract Syntax Tree) haqqında məlumat verir
     */
    void ExplainAST() const;
    
    /**
     * Java kompilyatorunun işləmə prinsipini izah edir
     */
    static void ExplainJavaCompiler();
    
    /**
     * Kompilasiya info obyektini qaytarır
     */
    const CompilationInfo& GetCompilationInfo() const { return compilationInfo; }
};

/**
 * Kompilyator mərhələləri enum-u
 */
enum class CompilationStage {
    LEXICAL_ANALYSIS,    // Leksik analiz (tokenization)
    SYNTAX_ANALYSIS,     // Sintaktik analiz (parsing)
    SEMANTIC_ANALYSIS,   // Semantik analiz
    INTERMEDIATE_CODE,   // Ara kod yaradılması
    OPTIMIZATION,        // Optimallaşdırma
    CODE_GENERATION      // Kod generasiyası
};

/**
 * Kompilyator mərhələsi haqqında məlumat
 */
struct StageInfo {
    CompilationStage stage;
    std::string name;
    std::string description;
    std::string example;
};

/**
 * Bütün kompilyator mərhələlərini qaytarır
 */
std::vector<StageInfo> GetAllCompilationStages();

/**
 * Müəyyən mərhələ haqqında ətraflı məlumat verir
 */
void PrintStageDetails(const StageInfo &stage);

} // namespace JavaAnalyzer

#endif // COMPILER_ANALYZER_H
