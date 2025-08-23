from typing import List
from sys import maxsize

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def minimum_sum2(grid: List[List[int]], u: int, d: int, l: int, r: int) -> int:
            min_i = len(grid)
            max_i = 0
            min_j = len(grid[0])
            max_j = 0

            for i in range(u, d + 1):
                for j in range(l, r + 1):
                    if grid[i][j] == 1:
                        min_i = min(min_i, i)
                        max_i = max(max_i, i)
                        min_j = min(min_j, j)
                        max_j = max(max_j, j)
            
            return (
                (max_i - min_i + 1) * (max_j - min_j + 1)
                if min_i <= max_i
                else maxsize // 3
            )

        def rotate(vec: List[List[int]]) -> List[List[int]]:
            n = len(vec)
            m = len(vec[0]) if n > 0 else 0
            ret = [[0] * n for _ in range(m)]

            for i in range(n):
                for j in range(m):
                    ret[m - j - 1][i] = vec[i][j]
            
            return ret
        
        def solve(grid: List[List[int]]):
            n = len(grid)
            m = len(grid[0]) if n > 0 else 0
            res = n * m

            for i in range(n - 1):
                for j in range(m - 1):
                    res = min(
                        res,
                        minimum_sum2(grid, 0, i, 0, m - 1)
                        + minimum_sum2(grid, i + 1, n - 1, 0, j)
                        + minimum_sum2(grid, i + 1, n - 1, j + 1, m - 1)
                    )

                    res = min(
                        res, 
                        minimum_sum2(grid, 0, i, 0, j)
                        + minimum_sum2(grid, 0, i, j + 1, m - 1)
                        + minimum_sum2(grid, i + 1, n - 1, 0, m - 1)
                    )

            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    res = min(
                        res, minimum_sum2(grid, 0, i, 0, m - 1)
                        + minimum_sum2(grid, i + 1, j, 0, m - 1)
                        + minimum_sum2(grid, j + 1, n - 1, 0, m - 1)
                    )
            
            return res
        
        rgrid = rotate(grid)
        return min(solve(grid), solve(rgrid))
        
def main():
    sol = Solution()
    print(sol.minimumSum([[0,0,0],[0,1,0],[0,1,1],[0,0,0]]))
    print(sol.minimumSum([[1,0,1],[1,1,1]]))
    print(sol.minimumSum([[1,0,1,0],[0,1,0,1]]))

if __name__ == '__main__':
    main()