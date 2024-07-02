from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        res = []

        for num in nums1_count:
            if num in nums2_count:
                res.extend([num] * min(nums1_count[num], nums2_count[num]))
        
        return res


    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     res = []
    #     short = nums1 if len(nums1) <= len(nums2) else nums2
    #     long = nums1 if len(nums1) > len(nums2) else nums2

    #     for num in short:
    #         if num in long:
    #             res.append(num)
    #             long.remove(num)
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.intersect([1,2,2,1], [2,2]))
    print(sol.intersect([4,9,5], [9,4,9,8,4]))


if __name__ == '__main__':
    main()