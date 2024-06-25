from typing import List
from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        sorted_nums = sorted(list(zip(nums1 ,nums2)), key=lambda x: -x[1])
        total = 0
        res = 0

        for a, b in sorted_nums:
            heappush(heap, a)
            total += a
        
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(res, total * b)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
    print(sol.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))

if __name__ == '__main__':
    main()