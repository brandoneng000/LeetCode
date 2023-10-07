from typing import List
import itertools

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007
        dp = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(n + 1)]

        for kk in range(1, m + 1):
            dp[1][1][kk] = 1
        
        for i, j, kk in itertools.product(range(1, n + 1), range(1, k + 1), range(m + 1)):
            dp[i][j][kk] += dp[i - 1][j][kk] * kk
            dp[i][j][kk] += sum(dp[i - 1][j - 1][1: kk])
        
        return sum(dp[n][k][1:]) % mod
        
        
        

def main():
    sol = Solution()
    print(sol.numOfArrays(n = 2, m = 3, k = 1))
    print(sol.numOfArrays(n = 5, m = 2, k = 3))
    print(sol.numOfArrays(n = 9, m = 1, k = 1))

if __name__ == '__main__':
    main()