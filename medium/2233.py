from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        heap = nums.copy()
        heapify(heap)
        res = 1

        while k:
            cur = heappop(heap)
            heappush(heap, cur + 1)
            k -= 1
        
        for val in heap:
            res = (res * val) % mod
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.maximumProduct(nums = [0,4], k = 5))
    print(sol.maximumProduct(nums = [6,3,3,2], k = 2))

if __name__ == '__main__':
    main()