#ifndef CALCULATOR_H
#define CALCULATOR_H

// Sadə hesablama funksiyaları
int add(int a, int b);
double multiply(double a, double b);
double divide(double a, double b);
int subtract(int a, int b);

// Array əməliyyatları
void process_array(double* arr, int size);
double array_sum(double* arr, int size);
double array_average(double* arr, int size);

// Riyazi funksiyalar
long long factorial(int n);
int fibonacci(int n);
bool is_prime(int n);

#endif // CALCULATOR_H
