#ifndef BLOCKCHAIN_HPP
#define BLOCKCHAIN_HPP

#include "Block.hpp"
#include "Transaction.hpp"
#include <vector>
#include <string>
#include <map>
#include <stdexcept>

/**
 * Blockchain sinifi
 * Bütün blokları və əməliyyatları idarə edir
 */
class Blockchain {
private:
    std::vector<Block> chain;                           // Bloklar zənciri
    std::vector<Transaction> pendingTransactions;       // Gözləyən əməliyyatlar
    double miningReward;                                // Mining mükafatı
    int difficulty;                                     // Mining çətinliyi
    std::map<std::string, double> balances;            // Balanslar bazası

    /**
     * Genesis block yaradır (ilk blok)
     */
    Block createGenesisBlock();

public:
    // Constructor
    Blockchain(int difficulty = 2);
    
    /**
     * Son bloku qaytarır
     */
    Block getLatestBlock() const;
    
    /**
     * Yeni əməliyyat əlavə edir
     */
    void addTransaction(const Transaction& transaction);
    
    /**
     * Gözləyən əməliyyatları mine edir
     */
    void minePendingTransactions(const std::string& miningRewardAddress);
    
    /**
     * Müəyyən ünvanın balansını qaytarır
     */
    double getBalance(const std::string& address) const;
    
    /**
     * Blockchain-in etibarlılığını yoxlayır
     */
    bool isChainValid() const;
    
    /**
     * Bütün blockchain-i ekranda göstərir
     */
    void displayChain() const;
    
    /**
     * Bütün blokları qaytarır
     */
    std::vector<Block> getChain() const;
};

#endif // BLOCKCHAIN_HPP

