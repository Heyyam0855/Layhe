#include "Transaction.hpp"
#include <iostream>
#include <sstream>
#include <iomanip>

/**
 * Transaction constructor
 */
Transaction::Transaction(const std::string& sender, const std::string& receiver, 
                        double amount, const std::string& signature)
    : sender(sender), receiver(receiver), amount(amount), signature(signature) {
    timestamp = time(nullptr);
}

/**
 * Göndərən ünvanı qaytarır
 */
std::string Transaction::getSender() const {
    return sender;
}

/**
 * Alıcı ünvanı qaytarır
 */
std::string Transaction::getReceiver() const {
    return receiver;
}

/**
 * Məbləği qaytarır
 */
double Transaction::getAmount() const {
    return amount;
}

/**
 * Vaxtı qaytarır
 */
time_t Transaction::getTimestamp() const {
    return timestamp;
}

/**
 * İmzanı qaytarır
 */
std::string Transaction::getSignature() const {
    return signature;
}

/**
 * Transaction-ı string formatına çevirir
 */
std::string Transaction::toString() const {
    std::ostringstream oss;
    oss << "Transaction(" << sender << " -> " << receiver << ": " 
        << std::fixed << std::setprecision(2) << amount << ")";
    return oss.str();
}

/**
 * Output operator
 */
std::ostream& operator<<(std::ostream& os, const Transaction& tx) {
    os << tx.toString();
    return os;
}

