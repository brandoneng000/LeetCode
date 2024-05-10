from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.cur_val = 1
        self.added_back = set()
        self.heap = []

    def popSmallest(self) -> int:
        if self.added_back:
            cur = heappop(self.heap)
            self.added_back.discard(cur)
            return cur
            
        self.cur_val += 1
        return self.cur_val - 1

    def addBack(self, num: int) -> None:
        if num < self.cur_val and num not in self.added_back:
            self.added_back.add(num)
            heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)