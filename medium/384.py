from typing import List
import random

class Solution:

    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #     self.random_nums = nums.copy()

    # def reset(self) -> List[int]:
    #     self.random_nums = self.nums.copy()
    #     return self.random_nums

    # def shuffle(self) -> List[int]:
    #     random.shuffle(self.random_nums)
    #     return self.random_nums
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        res = self.nums.copy()

        for i in range(len(res)):
            swap = random.randrange(i, len(res))
            res[i], res[swap] = res[swap], res[i]

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()