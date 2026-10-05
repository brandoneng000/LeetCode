from typing import List
from functools import cache

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @cache
        def fn(i: int, op1: int, op2: int):
            if i == n:
                return 0

            res = nums[i] + fn(i + 1, op1, op2)

            if op1:
                res = min(res, (nums[i] + 1) // 2 + fn(i + 1, op1 - 1, op2 ))

            if op2 and nums[i] >= k:
                res = min(res, nums[i] - k + fn(i + 1, op1, op2 - 1))

            if op1 and op2 and (nums[i] + 1) // 2 >= k:
                res = min(res, (nums[i] + 1) // 2 - k + fn(i + 1, op1 - 1, op2 - 1))

            if op1 and op2 and nums[i] >= k:
                res = min(res, (nums[i] - k + 1) // 2 + fn(i + 1, op1 - 1, op2 - 1))

            return res

        n = len(nums)
        return fn(0, op1, op2)
        


def main():
    sol = Solution()
    print(sol.minArraySum(nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1))
    print(sol.minArraySum(nums = [2,4,3], k = 3, op1 = 2, op2 = 1))

if __name__ == '__main__':
    main()