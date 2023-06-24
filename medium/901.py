class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        res = 1
        while self.stock and self.stock[-1][0] <= price:
            res += self.stock.pop()[1]
        
        self.stock.append((price, res))
        return res

# class StockSpanner:

#     def __init__(self):
#         self.stock = []
#         self.span = 0

#     def next(self, price: int) -> int:
#         if not self.stock or self.stock[-1] > price:
#             self.stock.append(price)
#             self.span = 1
#             return 1
#         elif self.stock[-1] == price:
#             self.stock.append(price)
#             self.span += 1
#             return self.span
#         else:
#             self.stock.append(price)
#             for i in range(len(self.stock) - self.span - 1, -1, -1):
#                 if self.stock[i] <= price:
#                     self.span += 1
#                 else:
#                     break
            
#             return self.span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)