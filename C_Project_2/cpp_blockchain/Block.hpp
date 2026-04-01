#ifndef BLOCK_HPP
#define BLOCK_HPP

#include "Transaction.hpp"
#include <string>
#include <vector>
#include <ctime>

/**
 * Block (Blok) sinifi
 * Blockchain-də hər bir bloku təmsil edir
 */
class Block {
private:
    int index;                              // Blokun indeksi
    std::vector<Transaction> transactions;  // Əməliyyatlar siyahısı
    std::string previousHash;               // Əvvəlki blokun hash-i
    time_t timestamp;                       // Blokun yaranma vaxtı
    int nonce;                              // Mining üçün nonce
    int difficulty;                         // Mining çətinliyi
    std::string hash;                       // Blokun hash-i

    /**
     * Hash hesablayır
     */
    std::string calculateHash() const;

public:
    // Constructor
    Block(int index, const std::vector<Transaction>& transactions, 
          const std::string& previousHash, int difficulty = 2);
    
    // Mining funksiyası (Proof of Work)
    void mineBlock();
    
    // Getters
    int getIndex() const;
    std::vector<Transaction> getTransactions() const;
    std::string getPreviousHash() const;
    time_t getTimestamp() const;
    int getNonce() const;
    std::string getHash() const;
    
    // Hash hesablamasını yenilə (nonce dəyişdikdən sonra)
    void updateHash();
    
    // Hash-in düzgünlüyünü yoxlayır
    bool verifyHash() const;
    
    // Blok məlumatlarını göstər
    void display() const;
};

#endif // BLOCK_HPP

