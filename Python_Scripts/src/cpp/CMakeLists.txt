cmake_minimum_required(VERSION 3.15)
project(calculator)

# C++ standartı
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# pybind11 tap
find_package(pybind11 REQUIRED)

# Python modulu yarat
pybind11_add_module(calculator 
    calculator.cpp
    bindings.cpp
)

# Quraşdırma yeri
install(TARGETS calculator DESTINATION .)
