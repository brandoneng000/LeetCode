from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])
        
        return res

def main():
    sol = Solution()
    print(sol.minimumDifference(nums = [90], k = 1))
    print(sol.minimumDifference(nums = [9,4,1,7], k = 2))

if __name__ == '__main__':
    main()