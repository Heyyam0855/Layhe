#include "../include/JavaAnalyzer.h"
#include "../include/OutputFormatter.h"

namespace JavaAnalyzer {

// JavaASTVisitor implementations
bool JavaASTVisitor::VisitCXXRecordDecl(clang::CXXRecordDecl *Declaration) {
    if (Declaration->isCompleteDefinition()) {
        std::string className = Declaration->getNameAsString();
        Info.classes.push_back(className);
        
        // Class-ın method-larını tap
        for (auto method : Declaration->methods()) {
            std::string methodName = method->getNameAsString();
            Info.methods.push_back(methodName);
        }
    }
    return true;
}

bool JavaASTVisitor::VisitFunctionDecl(clang::FunctionDecl *Declaration) {
    std::string functionName = Declaration->getNameAsString();
    
    // Main function və constructor-ları da əlavə et
    if (functionName != "main" && !functionName.empty()) {
        Info.methods.push_back(functionName);
    }
    
    return true;
}

bool JavaASTVisitor::VisitVarDecl(clang::VarDecl *Declaration) {
    std::string varName = Declaration->getNameAsString();
    if (!varName.empty()) {
        Info.variables.push_back(varName);
    }
    return true;
}

bool JavaASTVisitor::VisitNamespaceDecl(clang::NamespaceDecl *Declaration) {
    std::string namespaceName = Declaration->getNameAsString();
    if (!namespaceName.empty()) {
        // Java-da package kimi düşün
        Info.imports.push_back("package " + namespaceName);
    }
    return true;
}

// JavaASTConsumer implementations
void JavaASTConsumer::HandleTranslationUnit(clang::ASTContext &Context) {
    // Faylın sətir sayını hesabla
    clang::SourceManager &SM = Context.getSourceManager();
    clang::FileID MainFileID = SM.getMainFileID();
    
    if (const clang::FileEntry *FileEntry = SM.getFileEntryForID(MainFileID)) {
        Info.fileName = FileEntry->getName().str();
        
        // Sətir sayını hesabla
        llvm::StringRef FileContent = SM.getBufferData(MainFileID);
        Info.lineCount = std::count(FileContent.begin(), FileContent.end(), '\n') + 1;
    }
    
    // AST-ni traverse et
    Visitor.TraverseDecl(Context.getTranslationUnitDecl());
}

// JavaAnalyzerAction implementations
std::unique_ptr<clang::ASTConsumer> 
JavaAnalyzerAction::CreateASTConsumer(clang::CompilerInstance &Compiler, llvm::StringRef InFile) {
    return std::make_unique<JavaASTConsumer>(&Compiler.getASTContext(), Info);
}

// Utility functions
void PrintCompilationInfo(const CompilationInfo &Info) {
    OutputFormatter::PrintHeader("Kompilyasiya Məlumatları");
    
    OutputFormatter::PrintListItem("Fayl", Info.fileName);
    OutputFormatter::PrintStatistics("Sətir sayı", Info.lineCount);
    OutputFormatter::PrintStatistics("Class sayı", Info.classes.size());
    OutputFormatter::PrintStatistics("Method sayı", Info.methods.size());
    OutputFormatter::PrintStatistics("Variable sayı", Info.variables.size());
    OutputFormatter::PrintStatistics("Import sayı", Info.imports.size());
}

void PrintDetailedAnalysis(const CompilationInfo &Info) {
    OutputFormatter::PrintHeader("Ətraflı Analiz");
    
    if (!Info.classes.empty()) {
        OutputFormatter::PrintList("Tapılan Class-lar", Info.classes);
    }
    
    if (!Info.methods.empty()) {
        OutputFormatter::PrintList("Tapılan Method-lar", Info.methods);
    }
    
    if (!Info.variables.empty()) {
        OutputFormatter::PrintList("Tapılan Variable-lar", Info.variables);
    }
    
    if (!Info.imports.empty()) {
        OutputFormatter::PrintList("Import-lar", Info.imports);
    }
    
    // Əlavə statistika
    OutputFormatter::PrintSeparator('-');
    OutputFormatter::PrintSubHeader("Statistika");
    
    if (!Info.classes.empty()) {
        double methodPerClass = static_cast<double>(Info.methods.size()) / Info.classes.size();
        std::cout << "Orta method sayı (class başına): " << methodPerClass << std::endl;
    }
    
    if (Info.lineCount > 0) {
        double linesPerMethod = Info.methods.empty() ? 0 : 
                               static_cast<double>(Info.lineCount) / Info.methods.size();
        std::cout << "Orta sətir sayı (method başına): " << linesPerMethod << std::endl;
    }
}

} // namespace JavaAnalyzer