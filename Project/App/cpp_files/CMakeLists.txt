cmake_minimum_required(VERSION 3.10)

project(AppCore VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Source files
set(SOURCES
    core.cpp
)

# Header files
set(HEADERS
    core.h
)

# Create shared library (DLL on Windows)
add_library(core SHARED ${SOURCES} ${HEADERS})

# Define CORE_EXPORTS for DLL export
target_compile_definitions(core PRIVATE CORE_EXPORTS)

# Include directories
target_include_directories(core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Also create executable for standalone testing
add_executable(${PROJECT_NAME} main.cpp ${HEADERS})
target_link_libraries(${PROJECT_NAME} PRIVATE core)

# Set output directory
set_target_properties(core PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/../"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/../"
)

# Output message
message(STATUS "Building ${PROJECT_NAME} version ${PROJECT_VERSION}")
message(STATUS "Shared library will be created: core.dll (Windows) / libcore.so (Linux)")
