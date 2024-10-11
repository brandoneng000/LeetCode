from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapify(nums)

        while len(nums) > 1 and nums[0] < k:
            res += 1
            x = heappop(nums)
            y = heappop(nums)

            heappush(nums, x * 2 + y)
    
        return res

        
def main():
    sol = Solution()
    print(sol.minOperations(nums = [2,11,10,1,3], k = 10))
    print(sol.minOperations(nums = [1,1,2,4,9], k = 20))

if __name__ == '__main__':
    main()