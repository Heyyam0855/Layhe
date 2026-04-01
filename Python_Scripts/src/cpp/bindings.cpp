#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "calculator.h"

namespace py = pybind11;

// NumPy array üçün wrapper funksiyalar
py::array_t<double> py_process_array(py::array_t<double> input) {
    auto buf = input.request();
    double* ptr = static_cast<double*>(buf.ptr);
    
    // Nəticə massivi yarat
    auto result = py::array_t<double>(buf.size);
    auto result_buf = result.request();
    double* result_ptr = static_cast<double*>(result_buf.ptr);
    
    // Kopyala və işlə
    for (size_t i = 0; i < buf.size; i++) {
        result_ptr[i] = ptr[i] * 2;
    }
    
    return result;
}

double py_array_sum(py::array_t<double> input) {
    auto buf = input.request();
    double* ptr = static_cast<double*>(buf.ptr);
    return array_sum(ptr, buf.size);
}

double py_array_average(py::array_t<double> input) {
    auto buf = input.request();
    double* ptr = static_cast<double*>(buf.ptr);
    return array_average(ptr, buf.size);
}

PYBIND11_MODULE(calculator, m) {
    m.doc() = "Python və C++ inteqrasiya modulu - Hesablama kitabxanası";
    
    // Əsas hesablama funksiyaları
    m.def("add", &add, "İki tam ədədi topla",
          py::arg("a"), py::arg("b"));
    
    m.def("subtract", &subtract, "İki tam ədədi çıx",
          py::arg("a"), py::arg("b"));
    
    m.def("multiply", &multiply, "İki onluq ədədi vur",
          py::arg("a"), py::arg("b"));
    
    m.def("divide", &divide, "İki onluq ədədi böl",
          py::arg("a"), py::arg("b"));
    
    // Array funksiyaları
    m.def("process_array", &py_process_array, 
          "Massivin hər elementini 2-yə vur",
          py::arg("arr"));
    
    m.def("array_sum", &py_array_sum,
          "Massiv elementlərinin cəmi",
          py::arg("arr"));
    
    m.def("array_average", &py_array_average,
          "Massiv elementlərinin orta qiyməti",
          py::arg("arr"));
    
    // Riyazi funksiyalar
    m.def("factorial", &factorial, 
          "n! hesabla",
          py::arg("n"));
    
    m.def("fibonacci", &fibonacci,
          "n-ci Fibonacci ədədini tap",
          py::arg("n"));
    
    m.def("is_prime", &is_prime,
          "Ədədin sadə olub-olmadığını yoxla",
          py::arg("n"));
}
