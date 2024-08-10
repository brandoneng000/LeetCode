from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = [-x, -x]
        dp[nums[0] & 1] = nums[0]

        for i in range(1, n):
            dp[nums[i] & 1] = max(dp[nums[i] & 1], dp[(nums[i] & 1) ^ 1] - x) + nums[i]
        
        return max(dp)
        

        
def main():
    sol = Solution()
    print(sol.maxScore(nums = [2,3,6,1,9,2], x = 5))
    print(sol.maxScore(nums = [2,4,6,8], x = 3))

if __name__ == '__main__':
    main()