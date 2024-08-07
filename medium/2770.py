from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        dp[0] = 0

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if -target <= nums[i] - nums[j] <= target and dp[j] > -1:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]
        
def main():
    sol = Solution()
    print(sol.maximumJumps(nums = [1,3,6,4,1,2], target = 2))
    print(sol.maximumJumps(nums = [1,3,6,4,1,2], target = 3))
    print(sol.maximumJumps(nums = [1,3,6,4,1,2], target = 0))

if __name__ == '__main__':
    main()