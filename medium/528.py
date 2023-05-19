from typing import List
import random

class Solution:
    def __init__(self, w: List[int]):
        self.weight = [0] * len(w)
        total = sum(w)
        for i in range(len(w)):
            self.weight[i] = w[i] / total

        for i in range(1, len(w)):
            self.weight[i] += self.weight[i - 1]

    def pickIndex(self) -> int:
        choose = random.uniform(0, 1)

        for index, weight in enumerate(self.weight):
            if choose <= weight:
                return index

    # def __init__(self, w: List[int]):
    #     self.weight = w
    #     self.choices = list(range(len(self.weight)))

    # def pickIndex(self) -> int:
    #     return random.choices(self.choices, self.weight).pop()


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()