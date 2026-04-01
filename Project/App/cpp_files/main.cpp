/**
 * Main Entry Point
 * Proqramın giriş nöqtəsi
 */

#include "core.h"
#include <iostream>

int main(int argc, char* argv[]) {
    Core::Logger::log(Core::Logger::Level::INFO, "Starting application...");

    // Create application instance
    Core::Application app;

    // Initialize application
    if (!app.initialize()) {
        Core::Logger::log(Core::Logger::Level::ERROR, "Failed to initialize application");
        return 1;
    }

    // Create data manager
    Core::DataManager dataManager;
    
    // Connect to database
    if (!dataManager.connect("host=localhost;dbname=appdb;user=admin")) {
        Core::Logger::log(Core::Logger::Level::WARNING, "Failed to connect to database");
    }

    // Run application
    app.run();

    // Cleanup
    dataManager.disconnect();
    app.shutdown();

    Core::Logger::log(Core::Logger::Level::INFO, "Application exited successfully");
    return 0;
}
