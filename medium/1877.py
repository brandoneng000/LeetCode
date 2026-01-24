from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            res = max(res, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return res

    # def minPairSum(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums.sort()
    #     res = 0

    #     for i in range(n // 2):
    #         if nums[i] + nums[n - i - 1] > res:
    #             res = nums[i] + nums[n - i - 1]
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.minPairSum([3,5,2,3]))
    print(sol.minPairSum([3,5,4,2,4,6]))

if __name__ == '__main__':
    main()