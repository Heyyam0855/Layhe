#ifndef WALLET_HPP
#define WALLET_HPP

#include "Blockchain.hpp"
#include <string>
#include <random>
#include <sstream>
#include <iomanip>
#include <functional>

/**
 * Wallet (Cüzdan) sinifi
 * İstifadəçinin cüzdanını təmsil edir
 */
class Wallet {
private:
    std::string privateKey;     // Gizli açar
    std::string publicKey;      // Açıq açar/ünvan
    Blockchain* blockchain;      // Blockchain-ə istinad

    /**
     * Gizli açarı yaradır
     */
    std::string generatePrivateKey();
    
    /**
     * Açıq açarı yaradır (sadələşdirilmiş versiya)
     */
    std::string generatePublicKey();

public:
    // Constructor
    Wallet(Blockchain* blockchain);
    
    /**
     * Cüzdan ünvanını qaytarır
     */
    std::string getAddress() const;
    
    /**
     * Cüzdanın balansını qaytarır
     */
    double getBalance() const;
    
    /**
     * Pul göndərir
     */
    void sendMoney(const std::string& receiverAddress, double amount);
    
    /**
     * Gizli açarı qaytarır (diqqətli istifadə!)
     */
    std::string getPrivateKey() const;
};

#endif // WALLET_HPP

