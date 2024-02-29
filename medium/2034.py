from heapq import heappush, heappop

class StockPrice:

    def __init__(self):
        self.stock = {}
        self.cur_time = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.cur_time = max(self.cur_time, timestamp)
        self.stock[timestamp] = price

        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    
    def current(self) -> int:
        return self.stock[self.cur_time]
        
    def maximum(self) -> int:
        while -self.max_heap[0][0] != self.stock[self.max_heap[0][1]]:
            heappop(self.max_heap)
        
        return -self.max_heap[0][0]

    def minimum(self) -> int:
        while self.min_heap[0][0] != self.stock[self.min_heap[0][1]]:
            heappop(self.min_heap)
        
        return self.min_heap[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()