cmake_minimum_required(VERSION 3.16)
project(QaydaProject)

# C++ standartını təyin et
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Google Test-i yüklə
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9fd7188b4b8c67d7b23b73b.zip
)
FetchContent_MakeAvailable(googletest)

# Ana proqramı yarat
add_executable(main main.cpp)

# Test-ləri aktiv et
enable_testing()

# Test faylını əlavə et
add_executable(
  test_main
  tests/test_main.cpp
)

# Test üçün Google Test-i link et
target_link_libraries(
  test_main
  gtest_main
)

# Test-i qeydiyyatdan keçir
include(GoogleTest)
gtest_discover_tests(test_main)