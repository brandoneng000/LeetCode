from typing import List
from heapq import heappush, heappushpop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for i in range(len(nums)):
            if k:
                heappush(self.heap, nums[i])
                k -= 1
            else:
                heappushpop(self.heap, nums[i])
        
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)
        return self.heap[0]

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = sorted(nums)
        

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort()
#         return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)