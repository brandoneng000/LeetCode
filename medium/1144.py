from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        adjust = [0, 0]

        for i in range(n):
            cur = 0
            if i == 0:
                if i < n - 1 and nums[i] >= nums[i + 1]:
                    cur = nums[i] - nums[i + 1] + 1
            elif i == n - 1:
                if i > 0 and nums[i] >= nums[i - 1]:
                    cur = nums[i] - nums[i - 1] + 1
            elif nums[i] >= nums[i + 1] or nums[i] >= nums[i - 1]:
                cur = nums[i] - min(nums[i + 1], nums[i - 1]) + 1
            adjust[i % 2] += cur
        
        return min(adjust)
    
    # def movesToMakeZigzag(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     prefix = [0] * n

    #     for i in range(n):
    #         if i == 0:
    #             if i < n - 1 and nums[i] >= nums[i + 1]:
    #                 prefix[i] = nums[i] - nums[i + 1] + 1
    #         elif i == n - 1:
    #             if i > 0 and nums[i] >= nums[i - 1]:
    #                 prefix[i] = nums[i] - nums[i - 1] + 1
    #         elif nums[i] >= nums[i + 1] or nums[i] >= nums[i - 1]:
    #             prefix[i] = nums[i] - min(nums[i + 1], nums[i - 1]) + 1
        
    #     evens = 0
    #     odds = 0

    #     for i in range(n):
    #         if i % 2:
    #             odds += prefix[i]
    #         else:
    #             evens += prefix[i]
        
    #     return min(evens, odds)

def main():
    sol = Solution()
    print(sol.movesToMakeZigzag([10,4,4,10,10,6,2,3]))
    print(sol.movesToMakeZigzag([1,2,3]))
    print(sol.movesToMakeZigzag([9,6,1,6,2]))

if __name__ == '__main__':
    main()