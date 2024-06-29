from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0

        for i in range(n):
            lower_bound = lower - nums[i]
            upper_bound = upper - nums[i]
            lower_index = bisect_left(nums, lower_bound, i + 1)
            upper_index = bisect_right(nums, upper_bound, i + 1)

            res += upper_index - lower_index
        
        return res
        
def main():
    sol = Solution()
    # print(sol.countFairPairs(nums = [0,1,7,4,4,5,7,7,7,7], lower = 3, upper = 7))
    print(sol.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
    print(sol.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))

if __name__ == '__main__':
    main()