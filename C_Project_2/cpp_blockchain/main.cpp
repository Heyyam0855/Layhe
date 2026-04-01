#include <iostream>
#include "Blockchain.hpp"
#include "Wallet.hpp"

/**
 * Əsas funksiya - Demo
 */
int main() {
    std::cout << std::string(60, '=') << std::endl;
    std::cout << "BITCOIN TİPLİ KRİPTOVALYUTA SİSTEMİ (C++)" << std::endl;
    std::cout << std::string(60, '=') << std::endl;
    
    // Blockchain yarat
    Blockchain blockchain(2);
    
    // Cüzdanlar yarat
    Wallet wallet1(&blockchain);
    Wallet wallet2(&blockchain);
    Wallet wallet3(&blockchain);
    
    std::cout << "\nCüzdan 1 ünvanı: " << wallet1.getAddress() << std::endl;
    std::cout << "Cüzdan 2 ünvanı: " << wallet2.getAddress() << std::endl;
    std::cout << "Cüzdan 3 ünvanı: " << wallet3.getAddress() << std::endl;
    
    // Mining edərək pul qazan
    std::cout << "\n" << std::string(60, '=') << std::endl;
    std::cout << "MİNİNG BAŞLAYIR..." << std::endl;
    std::cout << std::string(60, '=') << std::endl;
    
    blockchain.minePendingTransactions(wallet1.getAddress());
    std::cout << "Cüzdan 1 balansı: " << wallet1.getBalance() << std::endl;
    
    blockchain.minePendingTransactions(wallet2.getAddress());
    std::cout << "Cüzdan 2 balansı: " << wallet2.getBalance() << std::endl;
    
    // Pul göndərmə əməliyyatları
    std::cout << "\n" << std::string(60, '=') << std::endl;
    std::cout << "ƏMƏLİYYATLAR" << std::endl;
    std::cout << std::string(60, '=') << std::endl;
    
    wallet1.sendMoney(wallet2.getAddress(), 25);
    wallet2.sendMoney(wallet3.getAddress(), 15);
    
    // Əməliyyatları mine et
    blockchain.minePendingTransactions(wallet3.getAddress());
    
    // Balansları göstər
    std::cout << "\n" << std::string(60, '=') << std::endl;
    std::cout << "BALANSLAR" << std::endl;
    std::cout << std::string(60, '=') << std::endl;
    std::cout << "Cüzdan 1 balansı: " << wallet1.getBalance() << std::endl;
    std::cout << "Cüzdan 2 balansı: " << wallet2.getBalance() << std::endl;
    std::cout << "Cüzdan 3 balansı: " << wallet3.getBalance() << std::endl;
    
    // Blockchain-i göstər
    std::cout << "\n" << std::string(60, '=') << std::endl;
    std::cout << "BLOCKCHAIN" << std::endl;
    std::cout << std::string(60, '=') << std::endl;
    blockchain.displayChain();
    
    // Blockchain-in etibarlılığını yoxla
    std::cout << "\n" << std::string(60, '=') << std::endl;
    std::cout << "BLOCKCHAIN ETİBARLILIĞI" << std::endl;
    std::cout << std::string(60, '=') << std::endl;
    std::cout << "Blockchain düzgündür: " << (blockchain.isChainValid() ? "Bəli" : "Xeyr") << std::endl;
    
    return 0;
}

