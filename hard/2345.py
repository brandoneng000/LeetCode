from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 1_000_000_007
        m, n = len(grid), len(grid[0])

        dp = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[i][j][grid[0][0] % k] = 1
                    continue

                value = grid[i - 1][j - 1] % k
                for r in range(k):
                    prev_mod = (r - value + k) % k
                    dp[i][j][r] = (
                        dp[i - 1][j][prev_mod] + dp[i][j - 1][prev_mod]
                    ) % mod
        
        return dp[m][n][0]

def main():
    sol = Solution()
    print(sol.numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3))
    print(sol.numberOfPaths(grid = [[0,0]], k = 5))
    print(sol.numberOfPaths(grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1))

if __name__ == '__main__':
    main()