from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = -(10 ** 33)

        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == INF:
                        continue

                    if i + 1 < m:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1

                        if c + cost <= k:
                            dp[i + 1][j][c + cost] = max(dp[i + 1][j][c + cost], dp[i][j][c] + val)
                    
                    if j + 1 < n:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1

                        if c + cost <= k:
                            dp[i][j + 1][c + cost] = max(dp[i][j + 1][c + cost], dp[i][j][c] + val)
            
        res = max(dp[m - 1][n - 1])
        return -1 if res < 0 else res
        
def main():
    sol = Solution()
    print(sol.maxPathScore(grid = [[0, 1],[2, 0]], k = 1))
    print(sol.maxPathScore(grid = [[0, 1],[1, 2]], k = 1))

if __name__ == '__main__':
    main()