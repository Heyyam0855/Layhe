#ifndef JAVA_ANALYZER_H
#define JAVA_ANALYZER_H

#include "clang/AST/AST.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/AST/RecursiveASTVisitor.h"
#include "clang/Frontend/ASTConsumers.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Rewrite/Core/Rewriter.h"
#include "clang/Tooling/CommonOptionsParser.h"
#include "clang/Tooling/Tooling.h"
#include <string>
#include <vector>
#include <iostream>

namespace JavaAnalyzer {

/**
 * Java kompilyasiya prosesinin məlumatlarını saxlamaq üçün struktur
 */
struct CompilationInfo {
    std::string fileName;
    std::vector<std::string> classes;
    std::vector<std::string> methods;
    std::vector<std::string> variables;
    std::vector<std::string> imports;
    int lineCount;
    
    CompilationInfo() : lineCount(0) {}
};

/**
 * AST (Abstract Syntax Tree) visitor - Java kodunun strukturunu analiz edir
 */
class JavaASTVisitor : public clang::RecursiveASTVisitor<JavaASTVisitor> {
private:
    clang::ASTContext *Context;
    CompilationInfo &Info;

public:
    explicit JavaASTVisitor(clang::ASTContext *Context, CompilationInfo &Info)
        : Context(Context), Info(Info) {}

    // Class və struct declaration-ları ziyarət edir
    bool VisitCXXRecordDecl(clang::CXXRecordDecl *Declaration);
    
    // Function və method declaration-ları ziyarət edir
    bool VisitFunctionDecl(clang::FunctionDecl *Declaration);
    
    // Variable declaration-ları ziyarət edir
    bool VisitVarDecl(clang::VarDecl *Declaration);
    
    // Namespace və import-ları analiz edir
    bool VisitNamespaceDecl(clang::NamespaceDecl *Declaration);
};

/**
 * AST Consumer - Parser-dən gələn AST-ni qəbul edib işləyir
 */
class JavaASTConsumer : public clang::ASTConsumer {
private:
    JavaASTVisitor Visitor;
    CompilationInfo &Info;

public:
    explicit JavaASTConsumer(clang::ASTContext *Context, CompilationInfo &Info)
        : Visitor(Context, Info), Info(Info) {}

    // AST tam yarandıqdan sonra çağırılır
    virtual void HandleTranslationUnit(clang::ASTContext &Context);
};

/**
 * Frontend Action - Kompilyasiyanın frontend mərhələsini idarə edir
 */
class JavaAnalyzerAction : public clang::ASTFrontendAction {
private:
    CompilationInfo &Info;

public:
    explicit JavaAnalyzerAction(CompilationInfo &Info) : Info(Info) {}

    virtual std::unique_ptr<clang::ASTConsumer> 
    CreateASTConsumer(clang::CompilerInstance &Compiler, llvm::StringRef InFile);
};

/**
 * Nəticələri terminal-a çap edir
 */
void PrintCompilationInfo(const CompilationInfo &Info);

/**
 * Kompilyasiya prosesinin ətraflı məlumatlarını çap edir
 */
void PrintDetailedAnalysis(const CompilationInfo &Info);

} // namespace JavaAnalyzer

#endif // JAVA_ANALYZER_H
