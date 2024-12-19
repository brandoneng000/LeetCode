from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [defaultdict(int) for i in range(k + 1)]
        res = [0] * (k + 1)
        
        for num in nums:
            for i in range(k, -1, -1):
                dp[i][num] = max(dp[i][num] + 1, res[i - 1] + 1 if i else 0)
                res[i] = max(res[i], dp[i][num])
        
        return res[k]
        

def main():
    sol = Solution()
    print(sol.maximumLength(nums = [1,2,1,1,3], k = 2))
    print(sol.maximumLength(nums = [1,2,3,4,5,1], k = 0))

if __name__ == '__main__':
    main()