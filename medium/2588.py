from typing import List
from collections import Counter

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        dp = Counter()
        dp[0] = 1
        res = prefix = 0

        for num in nums:
            prefix ^= num
            res += dp[prefix]
            dp[prefix] += 1

        return res
        
def main():
    sol = Solution()
    print(sol.beautifulSubarrays([4,3,1,2,4]))
    print(sol.beautifulSubarrays([1,10,4]))

if __name__ == '__main__':
    main()