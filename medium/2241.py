from typing import List
from collections import Counter

class ATM:

    def __init__(self):
        self.storage = Counter()
        self.denom = [20, 50, 100, 200, 500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for count, d in zip(banknotesCount, self.denom):
            self.storage[d] += count
        
    def withdraw(self, amount: int) -> List[int]:
        res = []
        back_up = self.storage.copy()

        for d in self.denom[::-1]:
            count = min(self.storage[d], amount // d)
            amount -= d * count
            self.storage[d] -= count
            res.append(count)
        
        if amount:
            self.storage = back_up
            return [-1]

        return res[::-1]
        
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)