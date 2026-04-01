/**
 * Core Module - C++ Header
 * Proqramın əsas çəkirdək kodu
 */

#ifndef CORE_H
#define CORE_H

#include <string>
#include <vector>
#include <memory>

// DLL Export macro for Windows
#ifdef _WIN32
    #ifdef CORE_EXPORTS
        #define CORE_API __declspec(dllexport)
    #else
        #define CORE_API __declspec(dllimport)
    #endif
#else
    #define CORE_API
#endif

namespace Core {

    /**
     * Application class - Proqramın əsas sinifi
     */
    class CORE_API Application {
    public:
        Application();
        ~Application();

        // Initialize the application
        bool initialize();

        // Run the main loop
        void run();

        // Shutdown the application
        void shutdown();

        // Get application version
        std::string getVersion() const;

    private:
        bool m_initialized;
        std::string m_version;
    };

    /**
     * DataManager class - Məlumat idarəetməsi
     */
    class CORE_API DataManager {
    public:
        DataManager();
        ~DataManager();

        // Connect to database
        bool connect(const std::string& connectionString);

        // Disconnect from database
        void disconnect();

        // Execute query
        bool executeQuery(const std::string& query);

        // Check connection status
        bool isConnected() const;

    private:
        bool m_connected;
        std::string m_connectionString;
    };

    /**
     * Logger class - Logging funksiyası
     */
    class CORE_API Logger {
    public:
        enum class Level {
            DEBUG,
            INFO,
            WARNING,
            ERROR
        };

        static void log(Level level, const std::string& message);
        static void setLogLevel(Level level);

    private:
        static Level s_currentLevel;
    };

} // namespace Core

// ===========================================
// C Interface for Go/CGO Integration
// ===========================================
#ifdef __cplusplus
extern "C" {
#endif

// Application functions
CORE_API void* core_app_create();
CORE_API void core_app_destroy(void* app);
CORE_API int core_app_initialize(void* app);
CORE_API void core_app_run(void* app);
CORE_API void core_app_shutdown(void* app);
CORE_API const char* core_app_get_version(void* app);

// DataManager functions
CORE_API void* core_data_create();
CORE_API void core_data_destroy(void* dm);
CORE_API int core_data_connect(void* dm, const char* connStr);
CORE_API void core_data_disconnect(void* dm);
CORE_API int core_data_execute(void* dm, const char* query);
CORE_API int core_data_is_connected(void* dm);

// Logger functions
CORE_API void core_log(int level, const char* message);

#ifdef __cplusplus
}
#endif

#endif // CORE_H
