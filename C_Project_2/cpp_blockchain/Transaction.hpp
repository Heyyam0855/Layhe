#ifndef TRANSACTION_HPP
#define TRANSACTION_HPP

#include <string>
#include <ctime>

/**
 * Əməliyyat (Transaction) sinifi
 * Blockchain-də pul göndərmə əməliyyatlarını təmsil edir
 */
class Transaction {
private:
    std::string sender;      // Göndərən ünvan
    std::string receiver;     // Alıcı ünvan
    double amount;           // Göndərilən məbləğ
    time_t timestamp;        // Əməliyyat vaxtı
    std::string signature;    // İmza (gələcək üçün)

public:
    // Constructor
    Transaction(const std::string& sender, const std::string& receiver, 
                double amount, const std::string& signature = "");
    
    // Getters
    std::string getSender() const;
    std::string getReceiver() const;
    double getAmount() const;
    time_t getTimestamp() const;
    std::string getSignature() const;
    
    // JSON formatına çevir (göstərmə üçün)
    std::string toString() const;
    
    // Operator overloading
    friend std::ostream& operator<<(std::ostream& os, const Transaction& tx);
};

#endif // TRANSACTION_HPP

