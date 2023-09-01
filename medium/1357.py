from typing import List

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.discount = (100 - discount) / 100
        self.prod = { prod: price for prod, price in zip(products, prices) }

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        
        bill = sum(self.prod[p] * a for p, a in zip(product, amount))
        
        if self.count == self.n:
            self.count = 0
            return bill * self.discount
        
        return bill
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)