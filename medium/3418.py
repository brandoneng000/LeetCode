from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        INF = 10 ** 33
        dp = [[[-INF] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = dp[0][0][2] = 0
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + coins[i][j])
                    if i and k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
                    if j:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + coins[i][j])
                    if j and k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1])

        return max(dp[m - 1][n - 1])

        
def main():
    sol = Solution()
    print(sol.maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]]))
    print(sol.maximumAmount([[10,10,10],[10,10,10]]))

if __name__ == '__main__':
    main()