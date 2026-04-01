#ifndef APPLICATION_H
#define APPLICATION_H

#include <string>
#include <memory>
#include <vector>

/**
 * @brief Əsas tətbiq sinifi
 * 
 * Bu sinif bütün modulları idarə edir və tədbiqin əsas məntiqini təşkil edir.
 * RAII prinsipi ilə yazılmış və smart pointer-lər istifadə edir.
 */
class Application {
private:
    std::string m_appName;
    std::string m_version;
    bool m_isRunning;
    
    // Modular components (forward declarations)
    class Calculator;
    class FileManager;
    class DataProcessor;
    
    std::unique_ptr<Calculator> m_calculator;
    std::unique_ptr<FileManager> m_fileManager;
    std::unique_ptr<DataProcessor> m_dataProcessor;

public:
    /**
     * @brief Constructor
     */
    Application();
    
    /**
     * @brief Destructor
     */
    ~Application();
    
    // Copy constructor və assignment operator-i silmək (RAII)
    Application(const Application&) = delete;
    Application& operator=(const Application&) = delete;
    
    // Move constructor və assignment
    Application(Application&&) = default;
    Application& operator=(Application&&) = default;
    
    /**
     * @brief Tədbiqin versiyasını qaytarır
     */
    const std::string& getVersion() const { return m_version; }
    
    /**
     * @brief Tədbiqin adını qaytarır
     */
    const std::string& getAppName() const { return m_appName; }
    
    /**
     * @brief Tədbiqin işləyib-işləmədiyini yoxlayır
     */
    bool isRunning() const { return m_isRunning; }
    
    /**
     * @brief Calculator modulunu işə salır
     * @return exit code
     */
    int runCalculator();
    
    /**
     * @brief File Manager modulunu işə salır
     * @return exit code
     */
    int runFileManager();
    
    /**
     * @brief Data Processor modulunu işə salır
     * @return exit code
     */
    int runDataProcessor();
    
    /**
     * @brief İnteraktiv rejimi başladır
     * @return exit code
     */
    int runInteractive();
    
    /**
     * @brief Tədbiqin bütün komponentlərini yoxlayır
     * @return true əgər hər şey qaydasındadırsa
     */
    bool selfTest();

private:
    /**
     * @brief Modulları initialize edir
     */
    void initializeModules();
    
    /**
     * @brief İnteraktiv menyunu göstərir
     */
    void showInteractiveMenu();
    
    /**
     * @brief İnteraktiv komandaları işləyir
     */
    bool processInteractiveCommand(const std::string& command);
};

#endif // APPLICATION_H