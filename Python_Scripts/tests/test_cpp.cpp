/**
 * C++ Unit Testləri
 * =================
 * calculator modulu üçün testlər
 */

#include <iostream>
#include <cassert>
#include <cmath>
#include <vector>
#include "../src/cpp/calculator.h"

// Test makrosu
#define TEST(name) void test_##name()
#define RUN_TEST(name) \
    std::cout << "Test: " << #name << "... "; \
    test_##name(); \
    std::cout << "OK ✓" << std::endl;

#define ASSERT_EQ(expected, actual) \
    assert((expected) == (actual))

#define ASSERT_NEAR(expected, actual, epsilon) \
    assert(std::abs((expected) - (actual)) < (epsilon))

#define ASSERT_TRUE(condition) \
    assert(condition)

#define ASSERT_FALSE(condition) \
    assert(!(condition))

// ===============================
// Əsas hesablama testləri
// ===============================

TEST(add_positive) {
    ASSERT_EQ(8, add(5, 3));
    ASSERT_EQ(100, add(50, 50));
    ASSERT_EQ(0, add(0, 0));
}

TEST(add_negative) {
    ASSERT_EQ(-8, add(-5, -3));
    ASSERT_EQ(2, add(5, -3));
    ASSERT_EQ(-2, add(-5, 3));
}

TEST(subtract) {
    ASSERT_EQ(2, subtract(5, 3));
    ASSERT_EQ(-2, subtract(3, 5));
    ASSERT_EQ(0, subtract(5, 5));
}

TEST(multiply) {
    ASSERT_NEAR(15.0, multiply(5.0, 3.0), 0.0001);
    ASSERT_NEAR(-15.0, multiply(-5.0, 3.0), 0.0001);
    ASSERT_NEAR(0.0, multiply(0.0, 100.0), 0.0001);
}

TEST(divide) {
    ASSERT_NEAR(2.5, divide(5.0, 2.0), 0.0001);
    ASSERT_NEAR(-2.5, divide(-5.0, 2.0), 0.0001);
    ASSERT_NEAR(0.0, divide(0.0, 5.0), 0.0001);
}

TEST(divide_by_zero) {
    bool exception_thrown = false;
    try {
        divide(5.0, 0.0);
    } catch (const std::invalid_argument&) {
        exception_thrown = true;
    }
    ASSERT_TRUE(exception_thrown);
}

// ===============================
// Massiv testləri
// ===============================

TEST(array_sum) {
    double arr[] = {1.0, 2.0, 3.0, 4.0, 5.0};
    ASSERT_NEAR(15.0, array_sum(arr, 5), 0.0001);
}

TEST(array_average) {
    double arr[] = {1.0, 2.0, 3.0, 4.0, 5.0};
    ASSERT_NEAR(3.0, array_average(arr, 5), 0.0001);
}

TEST(process_array) {
    double arr[] = {1.0, 2.0, 3.0};
    process_array(arr, 3);
    ASSERT_NEAR(2.0, arr[0], 0.0001);
    ASSERT_NEAR(4.0, arr[1], 0.0001);
    ASSERT_NEAR(6.0, arr[2], 0.0001);
}

// ===============================
// Riyazi funksiya testləri
// ===============================

TEST(factorial) {
    ASSERT_EQ(1, factorial(0));
    ASSERT_EQ(1, factorial(1));
    ASSERT_EQ(120, factorial(5));
    ASSERT_EQ(3628800, factorial(10));
}

TEST(factorial_negative) {
    bool exception_thrown = false;
    try {
        factorial(-1);
    } catch (const std::invalid_argument&) {
        exception_thrown = true;
    }
    ASSERT_TRUE(exception_thrown);
}

TEST(fibonacci) {
    ASSERT_EQ(0, fibonacci(0));
    ASSERT_EQ(1, fibonacci(1));
    ASSERT_EQ(1, fibonacci(2));
    ASSERT_EQ(55, fibonacci(10));
    ASSERT_EQ(144, fibonacci(12));
}

TEST(is_prime) {
    ASSERT_FALSE(is_prime(0));
    ASSERT_FALSE(is_prime(1));
    ASSERT_TRUE(is_prime(2));
    ASSERT_TRUE(is_prime(3));
    ASSERT_FALSE(is_prime(4));
    ASSERT_TRUE(is_prime(5));
    ASSERT_TRUE(is_prime(7));
    ASSERT_TRUE(is_prime(11));
    ASSERT_TRUE(is_prime(13));
    ASSERT_FALSE(is_prime(15));
    ASSERT_TRUE(is_prime(97));
    ASSERT_FALSE(is_prime(100));
}

// ===============================
// Əsas funksiya
// ===============================

int main() {
    std::cout << "\n================================" << std::endl;
    std::cout << "  C++ Unit Testləri" << std::endl;
    std::cout << "================================\n" << std::endl;
    
    // Əsas hesablama testləri
    std::cout << "--- Əsas Hesablama ---" << std::endl;
    RUN_TEST(add_positive);
    RUN_TEST(add_negative);
    RUN_TEST(subtract);
    RUN_TEST(multiply);
    RUN_TEST(divide);
    RUN_TEST(divide_by_zero);
    
    // Massiv testləri
    std::cout << "\n--- Massiv Əməliyyatları ---" << std::endl;
    RUN_TEST(array_sum);
    RUN_TEST(array_average);
    RUN_TEST(process_array);
    
    // Riyazi funksiya testləri
    std::cout << "\n--- Riyazi Funksiyalar ---" << std::endl;
    RUN_TEST(factorial);
    RUN_TEST(factorial_negative);
    RUN_TEST(fibonacci);
    RUN_TEST(is_prime);
    
    std::cout << "\n================================" << std::endl;
    std::cout << "  Bütün testlər keçdi! ✅" << std::endl;
    std::cout << "================================\n" << std::endl;
    
    return 0;
}
