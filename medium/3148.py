from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for j in range(n)] for i in range(m)]
        res = -float('inf')

        for i in range(m):
            for j in range(n):
                cur = min(dp[i - 1][j] if i > 0 else float('inf'), dp[i][j - 1] if j > 0 else float('inf'))
                res = max(res, grid[i][j] - cur)
                dp[i][j] = min(grid[i][j], cur)
            
        return res


        
def main():
    sol = Solution()
    print(sol.maxScore([[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]))
    print(sol.maxScore([[4,3,2],[3,2,1]]))

if __name__ == '__main__':
    main()