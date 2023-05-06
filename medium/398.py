from typing import List
import random
import collections

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_indices = collections.defaultdict(list)

        for index, val in enumerate(nums):
            self.nums_indices[val].append(index)
        

    def pick(self, target: int) -> int:
        return random.choice(self.nums_indices[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)