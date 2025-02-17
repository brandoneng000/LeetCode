from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        x = [[0 for j in range(n + 1)] for i in range(m + 1)]
        y = [[0 for j in range(n + 1)] for i in range(m + 1)]
        res = 0

        for i in range(m):
            for j in range(n):
                x[i][j] = x[i - 1][j] + x[i][j - 1] - x[i - 1][j - 1] + (grid[i][j] == 'X')
                y[i][j] = y[i - 1][j] + y[i][j - 1] - y[i - 1][j - 1] + (grid[i][j] == 'Y')

                if x[i][j] == y[i][j] and x[i][j] > 0:
                    res += 1
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))
    print(sol.numberOfSubmatrices([["X","X"],["X","Y"]]))
    print(sol.numberOfSubmatrices([[".","."],[".","."]]))
    print(sol.numberOfSubmatrices([["X", "Y"], ["X", "Y"], ["X", "Y"]]))

if __name__ == '__main__':
    main()