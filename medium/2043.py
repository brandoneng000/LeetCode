from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance) + 1
        self.accounts = {}

        for i, money in enumerate(balance, 1):
            self.accounts[i] = money
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (0 < account1 < self.n) or not (0 < account2 < self.n) or self.accounts[account1] < money:
            return False
        self.accounts[account1] -= money
        self.accounts[account2] += money

        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if not (0 < account < self.n):
            return False
        
        self.accounts[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not (0 < account < self.n) or self.accounts[account] < money:
            return False
        
        self.accounts[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)