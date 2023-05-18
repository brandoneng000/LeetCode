from typing import List
import random

class Solution:

    def __init__(self, m: int, n: int):
        self.col = n
        self.size = (m * n) - 1
        self.flipped = {}
        self.start = 0

    def flip(self) -> List[int]:
        val = random.randint(self.start, self.size)
        res = self.flipped.get(val, val)
        self.flipped[val] = self.flipped.get(self.start, self.start)
        self.start += 1
        return divmod(res, self.col)

    def reset(self) -> None:
        self.flipped.clear()
        self.start = 0
    
    # def __init__(self, m: int, n: int):
    #     self.row = m
    #     self.col = n
    #     self.flipped = set()

    # def flip(self) -> List[int]:
    #     val = random.randint(0, (self.row * self.col) - 1)
    #     r, c = val // self.col, val % self.col
        
    #     if (r, c) not in self.flipped:
    #         self.flipped.add((r, c))
    #         return [r, c]
    #     else:
    #         return self.flip()

    # def reset(self) -> None:
    #     self.flipped.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()