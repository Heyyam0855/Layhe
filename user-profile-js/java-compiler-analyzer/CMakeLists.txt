cmake_minimum_required(VERSION 3.10)
project(JavaCompilerAnalyzer)

# C++ standartını təyin et
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Clang tapın (əgər mövcuddursa)
find_package(Clang QUIET)

# Include qovluqları
include_directories(include)

# Source faylları
set(SOURCES
    src/CompilerAnalyzer.cpp
    src/JavaAnalyzer.cpp
    src/OutputFormatter.cpp
)

# Header faylları
set(HEADERS
    include/CompilerAnalyzer.h
    include/JavaAnalyzer.h
    include/OutputFormatter.h
)

# Əgər Clang tapılıbsa, tam funksional versiya yarat
if(Clang_FOUND)
    message(STATUS "Clang tapıldı - tam funksional versiya yaradılır")
    
    # Clang library-lərini əlavə et
    target_link_libraries(${PROJECT_NAME} 
        clangAST
        clangBasic
        clangFrontend
        clangSerialization
        clangTooling
        clangRewrite
    )
    
    # Clang include qovluqlarını əlavə et
    target_include_directories(${PROJECT_NAME} PRIVATE
        ${CLANG_INCLUDE_DIRS}
    )
    
    # CLANG_FOUND macro-sunu təyin et
    target_compile_definitions(${PROJECT_NAME} PRIVATE CLANG_FOUND)
    
else()
    message(STATUS "Clang tapılmadı - sadələşdirilmiş versiya yaradılır")
    
    # Clang olmadan işləyən versiya üçün alternativ source faylları
    list(REMOVE_ITEM SOURCES src/JavaAnalyzer.cpp)
    set(SOURCES ${SOURCES} src/JavaAnalyzerSimple.cpp)
endif()

# Executable yarat
add_executable(${PROJECT_NAME} main.cpp ${SOURCES})

# Debug və Release konfiqurasiyaları
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -Wall -Wextra")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")

# Install qaydaları
install(TARGETS ${PROJECT_NAME} DESTINATION bin)
install(FILES ${HEADERS} DESTINATION include)

# Test faylları üçün əlavə target
add_executable(test_analyzer test/test_main.cpp ${SOURCES})
if(Clang_FOUND)
    target_link_libraries(test_analyzer 
        clangAST
        clangBasic
        clangFrontend
        clangSerialization
        clangTooling
        clangRewrite
    )
    target_include_directories(test_analyzer PRIVATE
        ${CLANG_INCLUDE_DIRS}
    )
    target_compile_definitions(test_analyzer PRIVATE CLANG_FOUND)
endif()

# CPack konfiqurasiyası (paket yaratmaq üçün)
set(CPACK_PACKAGE_NAME "JavaCompilerAnalyzer")
set(CPACK_PACKAGE_VERSION "1.0.0")
set(CPACK_PACKAGE_DESCRIPTION "Java source kodlarını analiz edən C++ alət")
set(CPACK_PACKAGE_CONTACT "developer@example.com")
include(CPack)

# Makefile target-ları əlavə et
add_custom_target(clean-all
    COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_BINARY_DIR}
    COMMENT "Bütün build fayllarını təmizləyir"
)

add_custom_target(run
    COMMAND ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}
    DEPENDS ${PROJECT_NAME}
    COMMENT "Proqramı işə salır"
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)