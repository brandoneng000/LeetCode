from typing import List
import collections

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        last_index = len(nums) - 1
        total = sum(index * val for index, val in enumerate(nums))
        total_nums_val = sum(nums)
        res = total

        for i in range(len(nums) - 1, -1, -1):
            total = total + total_nums_val - nums[i] - (last_index * nums[i])
            res = max(res, total)
        
        return res
            

def main():
    sol = Solution()
    print(sol.maxRotateFunction([4,3,2,6]))
    print(sol.maxRotateFunction([100]))

if __name__ == '__main__':
    main()