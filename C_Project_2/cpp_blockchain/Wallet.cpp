#include "Wallet.hpp"
#include <iostream>
#include <random>
#include <sstream>
#include <iomanip>
#include <functional>
#include <ctime>

/**
 * Wallet constructor
 */
Wallet::Wallet(Blockchain* blockchain) : blockchain(blockchain) {
    privateKey = generatePrivateKey();
    publicKey = generatePublicKey();
}

/**
 * Gizli açarı yaradır
 */
std::string Wallet::generatePrivateKey() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 15);
    
    std::ostringstream oss;
    oss << std::hex;
    for (int i = 0; i < 64; i++) {  // 64 hex character = 32 bytes
        oss << dis(gen);
    }
    
    return oss.str();
}

/**
 * Açıq açarı yaradır (sadələşdirilmiş versiya)
 */
std::string Wallet::generatePublicKey() {
    // Real sistemdə ECDSA və ya digər kriptoqrafik üsullar istifadə olunur
    // Burada sadə hash funksiyası istifadə edirik
    std::hash<std::string> hasher;
    size_t hashValue = hasher(privateKey);
    
    std::ostringstream oss;
    oss << std::hex << hashValue;
    
    // Daha uzun açıq açar üçün
    std::string temp = oss.str();
    hashValue = hasher(temp + privateKey);
    oss.str("");
    oss << std::hex << hashValue;
    
    return oss.str();
}

/**
 * Cüzdan ünvanını qaytarır
 */
std::string Wallet::getAddress() const {
    return publicKey;
}

/**
 * Cüzdanın balansını qaytarır
 */
double Wallet::getBalance() const {
    return blockchain->getBalance(publicKey);
}

/**
 * Pul göndərir
 */
void Wallet::sendMoney(const std::string& receiverAddress, double amount) {
    Transaction transaction(publicKey, receiverAddress, amount);
    blockchain->addTransaction(transaction);
    std::cout << amount << " coin " << receiverAddress << " ünvanına göndərildi" << std::endl;
}

/**
 * Gizli açarı qaytarır
 */
std::string Wallet::getPrivateKey() const {
    return privateKey;
}

