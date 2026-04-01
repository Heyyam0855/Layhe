#include "include/CompilerAnalyzer.h"
#include "include/OutputFormatter.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

void printUsage(const std::string& programName) {
    JavaAnalyzer::OutputFormatter::PrintHeader("Java Compiler Analyzer");
    
    std::cout << "İstifadə:" << std::endl;
    std::cout << "  " << programName << " [seçimlər] <java_faylı>" << std::endl;
    std::cout << std::endl;
    
    std::cout << "Seçimlər:" << std::endl;
    std::cout << "  -v, --verbose    Ətraflı output" << std::endl;
    std::cout << "  -h, --help       Bu yardım mesajını göstər" << std::endl;
    std::cout << "  -s, --stages     Kompilyasiya mərhələlərini izah et" << std::endl;
    std::cout << "  -a, --ast        AST haqqında məlumat ver" << std::endl;
    std::cout << "  -e, --explain    Java kompilyatorunu izah et" << std::endl;
    std::cout << std::endl;
    
    std::cout << "Nümunələr:" << std::endl;
    std::cout << "  " << programName << " MyClass.java" << std::endl;
    std::cout << "  " << programName << " -v MyClass.java" << std::endl;
    std::cout << "  " << programName << " --stages" << std::endl;
    std::cout << "  " << programName << " --explain" << std::endl;
}

void createSampleJavaFile() {
    JavaAnalyzer::OutputFormatter::PrintInfo("Nümunə Java faylı yaradılır...");
    
    std::ofstream file("Sample.java");
    if (file.is_open()) {
        file << "import java.util.ArrayList;\n";
        file << "import java.util.List;\n";
        file << "\n";
        file << "public class Sample {\n";
        file << "    private String name;\n";
        file << "    private int age;\n";
        file << "    private List<String> hobbies;\n";
        file << "\n";
        file << "    public Sample(String name, int age) {\n";
        file << "        this.name = name;\n";
        file << "        this.age = age;\n";
        file << "        this.hobbies = new ArrayList<>();\n";
        file << "    }\n";
        file << "\n";
        file << "    public String getName() {\n";
        file << "        return name;\n";
        file << "    }\n";
        file << "\n";
        file << "    public void setName(String name) {\n";
        file << "        this.name = name;\n";
        file << "    }\n";
        file << "\n";
        file << "    public int getAge() {\n";
        file << "        return age;\n";
        file << "    }\n";
        file << "\n";
        file << "    public void addHobby(String hobby) {\n";
        file << "        hobbies.add(hobby);\n";
        file << "    }\n";
        file << "\n";
        file << "    public void displayInfo() {\n";
        file << "        System.out.println(\"Ad: \" + name);\n";
        file << "        System.out.println(\"Yaş: \" + age);\n";
        file << "        System.out.println(\"Hobbilər: \" + hobbies);\n";
        file << "    }\n";
        file << "\n";
        file << "    public static void main(String[] args) {\n";
        file << "        Sample person = new Sample(\"Ali\", 25);\n";
        file << "        person.addHobby(\"Oxumaq\");\n";
        file << "        person.addHobby(\"Proqramlaşdırma\");\n";
        file << "        person.displayInfo();\n";
        file << "    }\n";
        file << "}\n";
        file.close();
        
        JavaAnalyzer::OutputFormatter::PrintSuccess("Sample.java faylı yaradıldı!");
    } else {
        JavaAnalyzer::OutputFormatter::PrintError("Sample.java faylı yaradıla bilmədi!");
    }
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args(argv, argv + argc);
    bool verbose = false;
    std::string inputFile;
    
    // Command line argument-lərini parse et
    for (size_t i = 1; i < args.size(); ++i) {
        if (args[i] == "-h" || args[i] == "--help") {
            printUsage(args[0]);
            return 0;
        }
        else if (args[i] == "-v" || args[i] == "--verbose") {
            verbose = true;
        }
        else if (args[i] == "-s" || args[i] == "--stages") {
            JavaAnalyzer::CompilerAnalyzer::ExplainJavaCompiler();
            return 0;
        }
        else if (args[i] == "-a" || args[i] == "--ast") {
            JavaAnalyzer::CompilerAnalyzer analyzer("", verbose);
            analyzer.ExplainAST();
            return 0;
        }
        else if (args[i] == "-e" || args[i] == "--explain") {
            JavaAnalyzer::CompilerAnalyzer::ExplainJavaCompiler();
            return 0;
        }
        else if (args[i] == "--create-sample") {
            createSampleJavaFile();
            return 0;
        }
        else if (args[i][0] != '-') {
            inputFile = args[i];
        }
        else {
            std::cerr << "Naməlum seçim: " << args[i] << std::endl;
            printUsage(args[0]);
            return 1;
        }
    }
    
    // Əgər fayl verilməyibsə, nümunə yaradaq
    if (inputFile.empty()) {
        JavaAnalyzer::OutputFormatter::PrintInfo("Java faylı verilməyib. Nümunə fayl yaradılır...");
        createSampleJavaFile();
        inputFile = "Sample.java";
    }
    
    try {
        // Analyzer yaradıb analizi başlat
        JavaAnalyzer::CompilerAnalyzer analyzer(inputFile, verbose);
        
        if (analyzer.Analyze()) {
            analyzer.DisplayResults();
            
            if (verbose) {
                analyzer.ShowCompilationStages();
                analyzer.ExplainAST();
            }
        } else {
            return 1;
        }
        
    } catch (const std::exception& e) {
        JavaAnalyzer::OutputFormatter::PrintError("Xəta baş verdi: " + std::string(e.what()));
        return 1;
    }
    
    return 0;
}