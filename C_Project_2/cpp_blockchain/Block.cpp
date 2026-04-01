#include "Block.hpp"
#include <sstream>
#include <iomanip>
#include <iostream>
#include <ctime>
#include <functional>

/**
 * Block constructor
 */
Block::Block(int index, const std::vector<Transaction>& transactions, 
             const std::string& previousHash, int difficulty)
    : index(index), transactions(transactions), previousHash(previousHash),
      difficulty(difficulty), nonce(0) {
    timestamp = time(nullptr);
    hash = calculateHash();
}

/**
 * Hash hesablayır (SHA-256 istifadə edir)
 */
std::string Block::calculateHash() const {
    std::ostringstream ss;
    ss << index;
    for (const auto& tx : transactions) {
        ss << tx.getSender() << tx.getReceiver() << tx.getAmount() << tx.getTimestamp();
    }
    ss << previousHash << timestamp << nonce;
    
    std::string data = ss.str();
    
    // Sadələşdirilmiş hash funksiyası (std::hash istifadə edir)
    // Real sistemdə OpenSSL və ya digər kriptoqrafik kitabxanalar istifadə olunmalıdır
    std::hash<std::string> hasher;
    size_t hashValue = hasher(data);
    
    // Hex string-ə çevir
    std::ostringstream hexHash;
    hexHash << std::hex << hashValue;
    
    // Daha uzun hash üçün bir neçə dəfə hash et
    std::string temp = hexHash.str();
    hashValue = hasher(temp + data);
    hexHash.str("");
    hexHash << std::hex << hashValue;
    
    return hexHash.str();
}

/**
 * Hash-i yeniləyir (nonce dəyişdikdən sonra)
 */
void Block::updateHash() {
    hash = calculateHash();
}

/**
 * Hash-in düzgünlüyünü yoxlayır
 */
bool Block::verifyHash() const {
    return hash == calculateHash();
}

/**
 * Mining - Proof of Work mexanizmi
 */
void Block::mineBlock() {
    std::string target(difficulty, '0');
    
    while (hash.substr(0, difficulty) != target) {
        nonce++;
        updateHash();
    }
    
    std::cout << "Block mined: " << hash << std::endl;
}

/**
 * Blok indeksini qaytarır
 */
int Block::getIndex() const {
    return index;
}

/**
 * Əməliyyatları qaytarır
 */
std::vector<Transaction> Block::getTransactions() const {
    return transactions;
}

/**
 * Əvvəlki hash-i qaytarır
 */
std::string Block::getPreviousHash() const {
    return previousHash;
}

/**
 * Timestamp qaytarır
 */
time_t Block::getTimestamp() const {
    return timestamp;
}

/**
 * Nonce qaytarır
 */
int Block::getNonce() const {
    return nonce;
}

/**
 * Hash qaytarır
 */
std::string Block::getHash() const {
    return hash;
}

/**
 * Blok məlumatlarını ekranda göstərir
 */
void Block::display() const {
    std::cout << "\n" << std::string(50, '=') << std::endl;
    std::cout << "Block #" << index << std::endl;
    std::cout << "Hash: " << hash << std::endl;
    std::cout << "Previous Hash: " << previousHash << std::endl;
    
    char timeStr[26];
    struct tm* timeinfo = localtime(&timestamp);
    strftime(timeStr, sizeof(timeStr), "%Y-%m-%d %H:%M:%S", timeinfo);
    std::cout << "Timestamp: " << timeStr << std::endl;
    std::cout << "Nonce: " << nonce << std::endl;
    std::cout << "Transactions:" << std::endl;
    
    for (const auto& tx : transactions) {
        std::cout << "  - " << tx << std::endl;
    }
    std::cout << std::string(50, '=') << std::endl;
}

