from typing import List
import bisect

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0

        for i, val in enumerate(nums):
            if not stack or nums[stack[-1]] > val:
                stack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
        
        return res

    # def maxWidthRamp(self, nums: List[int]) -> int:
    #     stack = []
    #     res = 0

    #     for i in range(len(nums) - 1, -1, -1):
    #         if not stack or nums[i] > stack[-1][0]:
    #             stack.append([nums[i], i])
    #         else:
    #             j = stack[bisect.bisect(stack, [nums[i], i])][1]
    #             res = max(res, j - i)
        
    #     return res


    # def maxWidthRamp(self, nums: List[int]) -> int:
    #     res = 0

    #     for i in range(len(nums)):
    #         if res > len(nums) - i:
    #             break

    #         for j in range(len(nums) - 1, i, -1):
    #             if nums[i] <= nums[j] and res < j - i:
    #                 res = j - i
    #                 break
    #             elif res > j - i:
    #                 break

    #     return res

def main():
    sol = Solution()
    print(sol.maxWidthRamp([6,0,8,2,1,5]))
    print(sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))

if __name__ == '__main__':
    main()