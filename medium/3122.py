from typing import List
from collections import defaultdict

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = [[0 for j in range(10)] for i in range(n)]
        dp = [[float('inf') for j in range(10)] for i in range(n + 1)]

        for col in range(n):
            for val in range(10):
                for row in range(m):
                    count[col][val] += grid[row][col] != val
        
        for col in range(10):
            dp[n][col] = 0

        for col in range(n - 1, -1, -1):
            for val in range(10):
                for i in range(10):
                    if i != val:
                        dp[col][val] = min(dp[col][val], count[col][val] + dp[col + 1][i])
        
        return min(dp[0])
        
def main():
    sol = Solution()
    print(sol.minimumOperations([[1,0,2],[1,0,2]]))
    print(sol.minimumOperations([[1,1,1],[0,0,0]]))
    print(sol.minimumOperations([[1],[2],[3]]))

if __name__ == '__main__':
    main()