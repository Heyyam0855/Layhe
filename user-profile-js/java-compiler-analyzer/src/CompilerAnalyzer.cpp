#include "../include/CompilerAnalyzer.h"
#include "../include/OutputFormatter.h"
#include <iostream>
#include <fstream>
#include <regex>
#include <sstream>

namespace JavaAnalyzer {

CompilerAnalyzer::CompilerAnalyzer(const std::string &file, bool verbose)
    : sourceFile(file), verbose(verbose) {
    compilationInfo.fileName = file;
}

bool CompilerAnalyzer::Analyze() {
    OutputFormatter::PrintHeader("Java Compiler Analyzer");
    OutputFormatter::PrintInfo("Analiz başlayır: " + sourceFile);
    
    // Faylın mövcudluğunu yoxla
    std::ifstream file(sourceFile);
    if (!file.is_open()) {
        OutputFormatter::PrintError("Fayl açıla bilmədi: " + sourceFile);
        return false;
    }
    
    std::string line;
    int lineNumber = 0;
    std::regex classPattern(R"((?:public\s+)?class\s+(\w+))");
    std::regex methodPattern(R"((?:public|private|protected)?\s*(?:static\s+)?(?:\w+\s+)*(\w+)\s*\([^)]*\)\s*\{)");
    std::regex variablePattern(R"((?:public|private|protected)?\s*(?:static\s+)?(\w+)\s+(\w+)\s*[=;])");
    std::regex importPattern(R"(import\s+([^;]+);)");
    
    while (std::getline(file, line)) {
        lineNumber++;
        
        // Class-ları tap
        std::smatch match;
        if (std::regex_search(line, match, classPattern)) {
            compilationInfo.classes.push_back(match[1].str());
            if (verbose) {
                OutputFormatter::PrintInfo("Class tapıldı: " + match[1].str());
            }
        }
        
        // Method-ları tap
        if (std::regex_search(line, match, methodPattern)) {
            compilationInfo.methods.push_back(match[1].str());
            if (verbose) {
                OutputFormatter::PrintInfo("Method tapıldı: " + match[1].str());
            }
        }
        
        // Variable-ları tap
        if (std::regex_search(line, match, variablePattern)) {
            compilationInfo.variables.push_back(match[2].str());
            if (verbose) {
                OutputFormatter::PrintInfo("Variable tapıldı: " + match[2].str());
            }
        }
        
        // Import-ları tap
        if (std::regex_search(line, match, importPattern)) {
            compilationInfo.imports.push_back(match[1].str());
            if (verbose) {
                OutputFormatter::PrintInfo("Import tapıldı: " + match[1].str());
            }
        }
    }
    
    compilationInfo.lineCount = lineNumber;
    OutputFormatter::PrintSuccess("Analiz tamamlandı!");
    return true;
}

void CompilerAnalyzer::DisplayResults() const {
    OutputFormatter::PrintHeader("Analiz Nəticələri");
    
    OutputFormatter::PrintListItem("Fayl adı", compilationInfo.fileName);
    OutputFormatter::PrintStatistics("Sətir sayı", compilationInfo.lineCount);
    
    OutputFormatter::PrintList("Class-lar", compilationInfo.classes);
    OutputFormatter::PrintList("Method-lar", compilationInfo.methods);
    OutputFormatter::PrintList("Variable-lar", compilationInfo.variables);
    OutputFormatter::PrintList("Import-lar", compilationInfo.imports);
}

void CompilerAnalyzer::ShowCompilationStages() const {
    OutputFormatter::PrintHeader("Java Kompilyasiya Mərhələləri");
    
    auto stages = GetAllCompilationStages();
    for (const auto& stage : stages) {
        PrintStageDetails(stage);
    }
}

void CompilerAnalyzer::ExplainAST() const {
    OutputFormatter::PrintHeader("Abstract Syntax Tree (AST)");
    
    OutputFormatter::PrintInfo("AST - mənbə kodun iyerarxik təqdimatıdır");
    OutputFormatter::PrintSeparator('-');
    
    std::cout << "AST aşağıdakı komponentlərdən ibarətdir:\n\n";
    std::cout << "1. Root Node - Əsas fayl\n";
    std::cout << "2. Class Node-ları - Hər class üçün\n";
    std::cout << "3. Method Node-ları - Hər method üçün\n";
    std::cout << "4. Statement Node-ları - Hər ifadə üçün\n";
    std::cout << "5. Expression Node-ları - Hər expression üçün\n\n";
    
    if (!compilationInfo.classes.empty()) {
        OutputFormatter::PrintSubHeader("Bu fayldakı AST strukturu:");
        for (const auto& className : compilationInfo.classes) {
            std::cout << "├── Class: " << className << "\n";
            for (const auto& method : compilationInfo.methods) {
                std::cout << "│   ├── Method: " << method << "\n";
            }
        }
    }
}

void CompilerAnalyzer::ExplainJavaCompiler() {
    OutputFormatter::PrintHeader("Java Kompilyatorunun İşləmə Prinsipi");
    
    std::cout << "Java kompilyatoru (javac) aşağıdakı mərhələləri yerinə yetirir:\n\n";
    
    std::cout << "1. Leksik Analiz (Lexical Analysis)\n";
    std::cout << "   - Mənbə kodu token-lərə bölür\n";
    std::cout << "   - Keyword-lər, identifikatorlar, operator-lar tanınır\n\n";
    
    std::cout << "2. Sintaktik Analiz (Syntax Analysis)\n";
    std::cout << "   - Token-lərdən AST yaradılır\n";
    std::cout << "   - Qrammatik qaydalar yoxlanır\n\n";
    
    std::cout << "3. Semantik Analiz (Semantic Analysis)\n";
    std::cout << "   - Tip yoxlaması\n";
    std::cout << "   - Variable-ların təyin edilməsi\n";
    std::cout << "   - Method çağırışlarının yoxlanması\n\n";
    
    std::cout << "4. Bytecode Generasiyası\n";
    std::cout << "   - Java Virtual Machine üçün bytecode yaradılır\n";
    std::cout << "   - .class faylları yaradılır\n\n";
}

std::vector<StageInfo> GetAllCompilationStages() {
    return {
        {CompilationStage::LEXICAL_ANALYSIS, 
         "Leksik Analiz", 
         "Mənbə kodu token-lərə bölmə",
         "String s = \"hello\" → [String] [s] [=] [\"hello\"]"},
        
        {CompilationStage::SYNTAX_ANALYSIS,
         "Sintaktik Analiz",
         "Token-lərdən AST yaradılması",
         "Variable Declaration Node: Type=String, Name=s, Value=\"hello\""},
        
        {CompilationStage::SEMANTIC_ANALYSIS,
         "Semantik Analiz",
         "Tip yoxlaması və semantik qaydalar",
         "String tipinin mətn literal-ı ilə uyğunluğu yoxlanır"},
        
        {CompilationStage::INTERMEDIATE_CODE,
         "Ara Kod",
         "Platform-müstəqil ara kodun yaradılması",
         "Three-address code və ya bytecode"},
        
        {CompilationStage::OPTIMIZATION,
         "Optimallaşdırma",
         "Kodun performansının artırılması",
         "Dead code elimination, constant folding"},
        
        {CompilationStage::CODE_GENERATION,
         "Kod Generasiyası",
         "Final bytecode-un yaradılması",
         "JVM bytecode instructions"}
    };
}

void PrintStageDetails(const StageInfo &stage) {
    OutputFormatter::PrintSubHeader(stage.name);
    OutputFormatter::PrintListItem("Təsvir", stage.description);
    OutputFormatter::PrintListItem("Nümunə", stage.example);
    std::cout << "\n";
}

} // namespace JavaAnalyzer