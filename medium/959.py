from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(i, j):
            if min(i, j) < 0 or max(i, j) >= len(g) or g[i][j] != 0:
                return 0
            g[i][j] = 1
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        
        res = 0
        n = len(grid)
        g = [[0] * n * 3 for i in range(n * 3)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    g[i * 3][j * 3 + 2] = g[i * 3 + 1][j * 3 + 1] = g[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    g[i * 3][j * 3] = g[i * 3 + 1][j * 3 + 1] = g[i * 3 + 2][j * 3 + 2] = 1
        
        for i in range(n * 3):
            for j in range(n * 3):
                res += 1 if dfs(i, j) > 0 else 0
        
        return res



def main():
    sol = Solution()
    print(sol.regionsBySlashes([" /","/ "]))
    print(sol.regionsBySlashes([" /","  "]))
    print(sol.regionsBySlashes(["/\\","\\/"]))

if __name__ == '__main__':
    main()