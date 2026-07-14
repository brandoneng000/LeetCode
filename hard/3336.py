from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        m = max(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        res = 0

        for num in nums:
            ndp = [[0] * (m + 1) for _ in range(m + 1)]

            for j in range(m + 1):
                divisor1 = gcd(j, num)

                for k in range(m + 1):
                    val = dp[j][k]

                    if val == 0:
                        continue

                    divisor2 = gcd(k, num)
                    ndp[j][k] = (ndp[j][k] + val) % mod
                    ndp[divisor1][k] = (ndp[divisor1][k] + val) % mod
                    ndp[j][divisor2] = (ndp[j][divisor2] + val) % mod
            
            dp = ndp

        for j in range(1, m + 1):
            res = (res + dp[j][j]) % mod
        
        return res


def main():
    sol = Solution()
    print(sol.subsequencePairCount([1,2,3,4]))
    print(sol.subsequencePairCount([10,20,30]))
    print(sol.subsequencePairCount([1,1,1,1]))

if __name__ == '__main__':
    main()