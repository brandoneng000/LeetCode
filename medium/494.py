from typing import List
from collections import Counter

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cur_dp = Counter([0])
        
        for num in nums:
            next_dp = Counter()

            for cur in cur_dp:
                next_dp[cur + num] += cur_dp[cur]
                next_dp[cur - num] += cur_dp[cur]
            
            cur_dp = next_dp
        
        return cur_dp[target]

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     total = sum(nums)
    #     dp = { i:[0] * (2 * total + 1) for i in range(len(nums)) }
    #     dp[0][nums[0] + total] = 1
    #     dp[0][-nums[0] + total] += 1

    #     for i in range(1, len(nums)):
    #         for j in range(-total, total + 1):
    #             val = j + total
    #             if dp[i - 1][j + total] > 0:
    #                 dp[i][j + nums[i] + total] += dp[i - 1][j + total]
    #                 dp[i][j - nums[i] + total] += dp[i - 1][j + total]
        
    #     return 0 if abs(target) > total else dp[len(nums) - 1][target + total]

def main():
    sol = Solution()
    print(sol.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
    print(sol.findTargetSumWays(nums = [1], target = 1))

if __name__ == '__main__':
    main()