from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = { -1: True }
        
        def helper(index: int):
            if index in dp:
                return dp[index]
            
            res = False
            
            if index > 0 and nums[index] == nums[index - 1]:
                res |= helper(index - 2)
            if index > 1 and nums[index] == nums[index - 1] == nums[index - 2]:
                res |= helper(index - 3)
            if index > 1 and nums[index] == nums[index - 1] + 1 == nums[index - 2] + 2:
                res |= helper(index - 3)
            
            dp[index] = res
            return res
        
        return helper(n - 1)

def main():
    sol = Solution()
    print(sol.validPartition([5,6]))
    print(sol.validPartition([4,4,4,5,6]))
    print(sol.validPartition([1,1,1,2]))

if __name__ == '__main__':
    main()