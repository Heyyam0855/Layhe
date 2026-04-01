#include "Blockchain.hpp"
#include <iostream>
#include <ctime>

/**
 * Blockchain constructor
 */
Blockchain::Blockchain(int difficulty) 
    : difficulty(difficulty), miningReward(50.0) {
    chain.push_back(createGenesisBlock());
}

/**
 * Genesis block yaradır (ilk blok)
 */
Block Blockchain::createGenesisBlock() {
    Transaction genesisTx("System", "Genesis", 0.0);
    std::vector<Transaction> genesisTransactions;
    genesisTransactions.push_back(genesisTx);
    
    Block genesis(0, genesisTransactions, "0", difficulty);
    return genesis;
}

/**
 * Son bloku qaytarır
 */
Block Blockchain::getLatestBlock() const {
    return chain.back();
}

/**
 * Yeni əməliyyat əlavə edir
 */
void Blockchain::addTransaction(const Transaction& transaction) {
    // Balansı yoxla
    if (transaction.getSender() != "System") {
        if (balances[transaction.getSender()] < transaction.getAmount()) {
            throw std::runtime_error("Kifayət qədər balans yoxdur!");
        }
    }
    
    pendingTransactions.push_back(transaction);
}

/**
 * Gözləyən əməliyyatları mine edir
 */
void Blockchain::minePendingTransactions(const std::string& miningRewardAddress) {
    // Mining mükafatı əlavə et
    Transaction rewardTx("System", miningRewardAddress, miningReward);
    pendingTransactions.push_back(rewardTx);
    
    // Yeni block yarat və mine et
    Block newBlock(chain.size(), pendingTransactions, getLatestBlock().getHash(), difficulty);
    newBlock.mineBlock();
    
    // Block-u chain-ə əlavə et
    chain.push_back(newBlock);
    
    // Balansları yenilə
    for (const auto& transaction : pendingTransactions) {
        if (transaction.getSender() != "System") {
            balances[transaction.getSender()] -= transaction.getAmount();
        }
        balances[transaction.getReceiver()] += transaction.getAmount();
    }
    
    // Gözləyən əməliyyatları təmizlə
    pendingTransactions.clear();
}

/**
 * Müəyyən ünvanın balansını qaytarır
 */
double Blockchain::getBalance(const std::string& address) const {
    auto it = balances.find(address);
    if (it != balances.end()) {
        return it->second;
    }
    return 0.0;
}

/**
 * Blockchain-in etibarlılığını yoxlayır
 */
bool Blockchain::isChainValid() const {
    for (size_t i = 1; i < chain.size(); i++) {
        const Block& currentBlock = chain[i];
        const Block& previousBlock = chain[i - 1];
        
        // Hash-in düzgünlüyünü yoxla
        if (!currentBlock.verifyHash()) {
            return false;
        }
        
        // Əvvəlki hash-in uyğunluğunu yoxla
        if (currentBlock.getPreviousHash() != previousBlock.getHash()) {
            return false;
        }
    }
    
    return true;
}

/**
 * Bütün blockchain-i ekranda göstərir
 */
void Blockchain::displayChain() const {
    for (const auto& block : chain) {
        block.display();
    }
}

/**
 * Bütün blokları qaytarır
 */
std::vector<Block> Blockchain::getChain() const {
    return chain;
}

