from typing import List
from heapq import heappop,heappush, heapify

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        res = 0

        for _ in range(k):
            val = -heappop(heap)
            res += val
            heappush(heap, -((val + 2) // 3))
    
        return res
        
def main():
    sol = Solution()
    print(sol.maxKelements(nums = [238838724,196963851,539418658,120132686,273213807,57187185,68854249,619718192], k = 7))
    print(sol.maxKelements(nums = [10,10,10,10,10], k = 5))
    print(sol.maxKelements(nums = [1,10,3,3,3], k = 3))

if __name__ == '__main__':
    main()