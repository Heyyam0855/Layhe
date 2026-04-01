"""
Bitcoin tipli Kriptovalyuta Sistemi
Bu sistem blockchain texnologiyası ilə işləyir
"""

import hashlib
import json
import time
from typing import List, Dict, Optional
from datetime import datetime
import secrets
import binascii
from collections import defaultdict


class Transaction:
    """Əməliyyat (Transaction) sinifi"""
    
    def __init__(self, sender: str, receiver: str, amount: float, signature: str = None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.signature = signature
    
    def to_dict(self) -> Dict:
        """Əməliyyatı dictionary-yə çevirir"""
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'timestamp': self.timestamp
        }
    
    def __repr__(self):
        return f"Transaction({self.sender} -> {self.receiver}: {self.amount})"


class Block:
    """Block (Blok) sinifi"""
    
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str, difficulty: int = 2):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Block-un hash-ni hesablayır"""
        block_string = json.dumps({
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self):
        """Proof of Work - Block-u mine edir"""
        target = '0' * self.difficulty
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
    
    def to_dict(self) -> Dict:
        """Block-u dictionary-yə çevirir"""
        return {
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce,
            'hash': self.hash
        }


class Blockchain:
    """Blockchain sinifi"""
    
    def __init__(self, difficulty: int = 2):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.pending_transactions: List[Transaction] = []
        self.mining_reward = 50
        self.difficulty = difficulty
        self.balances: Dict[str, float] = defaultdict(float)
    
    def create_genesis_block(self) -> Block:
        """İlk block-u (Genesis Block) yaradır"""
        genesis_transaction = Transaction("System", "Genesis", 0)
        return Block(0, [genesis_transaction], "0")
    
    def get_latest_block(self) -> Block:
        """Son block-u qaytarır"""
        return self.chain[-1]
    
    def add_transaction(self, transaction: Transaction):
        """Yeni əməliyyat əlavə edir"""
        # Balansı yoxla
        if transaction.sender != "System":
            if self.balances[transaction.sender] < transaction.amount:
                raise Exception("Kifayət qədər balans yoxdur!")
        
        self.pending_transactions.append(transaction)
    
    def mine_pending_transactions(self, mining_reward_address: str):
        """Gözləyən əməliyyatları mine edir"""
        # Mining mükafatı əlavə et
        reward_transaction = Transaction("System", mining_reward_address, self.mining_reward)
        self.pending_transactions.append(reward_transaction)
        
        # Yeni block yarat və mine et
        block = Block(
            len(self.chain),
            self.pending_transactions,
            self.get_latest_block().hash,
            self.difficulty
        )
        block.mine_block()
        
        # Block-u chain-ə əlavə et
        self.chain.append(block)
        
        # Balansları yenilə
        for transaction in self.pending_transactions:
            if transaction.sender != "System":
                self.balances[transaction.sender] -= transaction.amount
            self.balances[transaction.receiver] += transaction.amount
        
        # Gözləyən əməliyyatları təmizlə
        self.pending_transactions = []
    
    def get_balance(self, address: str) -> float:
        """Müəyyən ünvanın balansını qaytarır"""
        return self.balances[address]
    
    def is_chain_valid(self) -> bool:
        """Blockchain-in etibarlılığını yoxlayır"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Hash-in düzgünlüyünü yoxla
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Əvvəlki hash-in uyğunluğunu yoxla
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def display_chain(self):
        """Blockchain-i ekranda göstərir"""
        for block in self.chain:
            print(f"\n{'='*50}")
            print(f"Block #{block.index}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {datetime.fromtimestamp(block.timestamp)}")
            print(f"Nonce: {block.nonce}")
            print(f"Transactions:")
            for tx in block.transactions:
                print(f"  - {tx}")
            print(f"{'='*50}")


class Wallet:
    """Cüzdan (Wallet) sinifi"""
    
    def __init__(self, blockchain: Blockchain):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()
        self.blockchain = blockchain
    
    def generate_private_key(self) -> str:
        """Gizli açarı yaradır"""
        return secrets.token_hex(32)
    
    def generate_public_key(self) -> str:
        """Açıq açarı yaradır (sadələşdirilmiş versiya)"""
        return hashlib.sha256(self.private_key.encode()).hexdigest()
    
    def get_address(self) -> str:
        """Cüzdan ünvanını qaytarır"""
        return self.public_key
    
    def get_balance(self) -> float:
        """Cüzdanın balansını qaytarır"""
        return self.blockchain.get_balance(self.get_address())
    
    def send_money(self, receiver_address: str, amount: float):
        """Pul göndərir"""
        transaction = Transaction(self.get_address(), receiver_address, amount)
        self.blockchain.add_transaction(transaction)
        print(f"{amount} coin {receiver_address} ünvanına göndərildi")


def main():
    """Əsas funksiya - Demo"""
    print("=" * 60)
    print("BITCOIN TİPLİ KRİPTOVALYUTA SİSTEMİ")
    print("=" * 60)
    
    # Blockchain yarat
    blockchain = Blockchain(difficulty=2)
    
    # Cüzdanlar yarat
    wallet1 = Wallet(blockchain)
    wallet2 = Wallet(blockchain)
    wallet3 = Wallet(blockchain)
    
    print(f"\nCüzdan 1 ünvanı: {wallet1.get_address()}")
    print(f"Cüzdan 2 ünvanı: {wallet2.get_address()}")
    print(f"Cüzdan 3 ünvanı: {wallet3.get_address()}")
    
    # Mining edərək pul qazan
    print("\n" + "="*60)
    print("MİNİNG BAŞLAYIR...")
    print("="*60)
    
    blockchain.mine_pending_transactions(wallet1.get_address())
    print(f"Cüzdan 1 balansı: {wallet1.get_balance()}")
    
    blockchain.mine_pending_transactions(wallet2.get_address())
    print(f"Cüzdan 2 balansı: {wallet2.get_balance()}")
    
    # Pul göndərmə əməliyyatları
    print("\n" + "="*60)
    print("ƏMƏLİYYATLAR")
    print("="*60)
    
    wallet1.send_money(wallet2.get_address(), 25)
    wallet2.send_money(wallet3.get_address(), 15)
    
    # Əməliyyatları mine et
    blockchain.mine_pending_transactions(wallet3.get_address())
    
    # Balansları göstər
    print("\n" + "="*60)
    print("BALANSLAR")
    print("="*60)
    print(f"Cüzdan 1 balansı: {wallet1.get_balance()}")
    print(f"Cüzdan 2 balansı: {wallet2.get_balance()}")
    print(f"Cüzdan 3 balansı: {wallet3.get_balance()}")
    
    # Blockchain-i göstər
    print("\n" + "="*60)
    print("BLOCKCHAIN")
    print("="*60)
    blockchain.display_chain()
    
    # Blockchain-in etibarlılığını yoxla
    print("\n" + "="*60)
    print("BLOCKCHAIN ETİBARLILIĞI")
    print("="*60)
    print(f"Blockchain düzgündür: {blockchain.is_chain_valid()}")


if __name__ == "__main__":
    main()

