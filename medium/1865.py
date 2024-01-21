from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_count = Counter(nums1)
        self.nums2_count = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        original = self.nums2[index]
        self.nums2[index] += val
        self.nums2_count[original] -= 1
        self.nums2_count[original + val] += 1

    def count(self, tot: int) -> int:
        two_sum = Counter()
        res = 0

        for val in self.nums1_count:
            two_sum[tot - val] = self.nums1_count[val]
        
        for num in self.nums2_count:
            if num in two_sum:
                res += two_sum[num] * self.nums2_count[num]
        
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)