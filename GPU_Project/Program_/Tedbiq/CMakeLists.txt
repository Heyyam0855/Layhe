cmake_minimum_required(VERSION 3.15)
project(CppPortfolioLayihesi VERSION 1.0.0 LANGUAGES CXX)

# C++ standartını təyin et
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Build type əgər təyin edilməyibsə Debug olaraq təyin et
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()

# Compiler flags
if(MSVC)
    set(CMAKE_CXX_FLAGS "/W4 /EHsc")
    set(CMAKE_CXX_FLAGS_DEBUG "/Od /Zi")
    set(CMAKE_CXX_FLAGS_RELEASE "/O2 /DNDEBUG")
else()
    set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wpedantic")
    set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
    set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
endif()

# Include directories
include_directories(include)
include_directories(src)

# Source files
set(SOURCES
    src/main.cpp
    src/core/Application.cpp
)

# Executable yarad
add_executable(${PROJECT_NAME} ${SOURCES})

# Target properties
set_target_properties(${PROJECT_NAME} PROPERTIES
    OUTPUT_NAME "portfolio_app"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)

# İsteğe bağlı: Əgər testing lazımdırsa
option(BUILD_TESTS "Build test programs" OFF)

if(BUILD_TESTS)
    enable_testing()
    
    # Test üçün ayrı executable
    add_executable(test_runner
        src/tests/test_main.cpp
        src/core/Application.cpp
    )
    
    target_include_directories(test_runner PRIVATE include src)
    
    add_test(NAME ApplicationTests COMMAND test_runner)
endif()

# İsteğe bağlı: Documentation
option(BUILD_DOCS "Build documentation" OFF)

if(BUILD_DOCS)
    find_package(Doxygen)
    if(DOXYGEN_FOUND)
        configure_file(${CMAKE_CURRENT_SOURCE_DIR}/docs/Doxyfile.in 
                      ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
        add_custom_target(docs
            ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
            COMMENT "Documentation yaradılır Doxygen ilə" VERBATIM
        )
    endif()
endif()

# İsteğe bağlı: Package manager kitabxanaları
# find_package(nlohmann_json QUIET)
# if(nlohmann_json_FOUND)
#     target_link_libraries(${PROJECT_NAME} PRIVATE nlohmann_json::nlohmann_json)
#     target_compile_definitions(${PROJECT_NAME} PRIVATE HAS_JSON_SUPPORT)
# endif()

# İsteğe bağlı: Logging library
# find_package(spdlog QUIET)
# if(spdlog_FOUND)
#     target_link_libraries(${PROJECT_NAME} PRIVATE spdlog::spdlog)
#     target_compile_definitions(${PROJECT_NAME} PRIVATE HAS_SPDLOG)
# endif()

# Installation rules
install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION bin
)

# İsteğe bağlı: CPack konfiqurasiyası
set(CPACK_PACKAGE_NAME "CppPortfolioLayihesi")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "C++ Portfolio Application")
set(CPACK_PACKAGE_VENDOR "Portfolio Developer")
set(CPACK_RESOURCE_FILE_README "${CMAKE_CURRENT_SOURCE_DIR}/README.md")

include(CPack)

# Məlumat mesajları
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Compiler: ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "Compiler flags: ${CMAKE_CXX_FLAGS}")

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    message(STATUS "Debug flags: ${CMAKE_CXX_FLAGS_DEBUG}")
else()
    message(STATUS "Release flags: ${CMAKE_CXX_FLAGS_RELEASE}")
endif()