from typing import DefaultDict
from heapq import heappush, heappop

class NumberContainers:

    def __init__(self):
        self.nums = {}
        self.indices = DefaultDict(list)

    def change(self, index: int, number: int) -> None:
        self.nums[index] = number
        heappush(self.indices[number], index)
        
    def find(self, number: int) -> int:
        while self.indices[number]:
            res = heappop(self.indices[number])

            if self.nums[res] == number:
                heappush(self.indices[number], res)
                return res
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)