from typing import List

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        
        if n <= 2:
            return True
        
        for i in range(n - 1):
            if nums[i] + nums[i + 1] >= m:
                return True
        
        return False
    
    # def canSplitArray(self, nums: List[int], m: int) -> bool:
    #     def helper(left: int, right: int, total: int):
    #         if right == left:
    #             return True
            
    #         if total < m:
    #             return False
            
    #         if (left, right, total) in dp:
    #             return dp[left, right, total]
            
    #         dp[left, right, total] = helper(left + 1, right, total - nums[left]) or helper(left, right - 1, total - nums[right])
    #         return dp[left, right, total]
        
    #     n = len(nums)
    
    #     if n <= 2:
    #         return True
        
    #     dp = {}

    #     return helper(0, n - 1, sum(nums))
        
def main():
    sol = Solution()
    print(sol.canSplitArray(nums = [2, 2, 1], m = 4))
    print(sol.canSplitArray(nums = [2, 1, 3], m = 5))
    print(sol.canSplitArray(nums = [2, 3, 3, 2, 3], m = 6))

if __name__ == '__main__':
    main()