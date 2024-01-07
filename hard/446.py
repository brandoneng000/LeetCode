from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                res += dp[j][diff]
        
        return res
        
def main():
    sol = Solution()
    print(sol.numberOfArithmeticSlices([2,4,6,8,10]))
    print(sol.numberOfArithmeticSlices([7,7,7,7,7]))

if __name__ == '__main__':
    main()