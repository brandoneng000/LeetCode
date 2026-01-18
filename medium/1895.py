from typing import List
from itertools import accumulate

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # row and col sum
        rs = [[0] + list(accumulate(row)) for row in grid]
        cs = [[0] * n for _ in range(m + 1)]

        # diagonal and alt diangonal sum
        ds = [[0] * (n + 1) for _ in range(m + 1)]
        ads = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                x = grid[r][c]
                cs[r + 1][c] = cs[r][c] + x
                ds[r + 1][c + 1] = ds[r][c] + x
                ads[r + 1][c] = ads[r][c + 1] + x
        
        for k in range(min(m, n), 0, -1):
            for row in range(k, m + 1):
                for col in range(k, n + 1):
                    diag_sum = ds[row][col] - ds[row - k][col - k]

                    if ads[row][col - k] - ads[row - k][col] != diag_sum:
                        continue

                    if any(rs[r][col] - rs[r][col - k] != diag_sum for r in range(row - k, row)):
                        continue

                    if any(cs[row][c] - cs[row - k][c] != diag_sum for c in range(col - k, col)):
                        continue

                    return k
        
        return 1


    # def largestMagicSquare(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     prefix_row = [[0 for j in range(n + 1)] for i in range(m)]
    #     prefix_col = [[0 for j in range(m + 1)] for i in range(n)]

    #     for i in range(m):
    #         for j in range(n):
    #             prefix_row[i][j + 1] = prefix_row[i][j] + grid[i][j]
    #             prefix_col[j][i + 1] = prefix_col[j][i] + grid[i][j]
        
    #     def get_row_sum(row, l, r):
    #         return prefix_row[row][r + 1] - prefix_row[row][l]
        
    #     def get_col_sum(col, l, r):
    #         return prefix_col[col][r + 1] - prefix_col[col][l]

    #     def test_size(k: int):
    #         for r in range(m - k + 1):
    #             for c in range(n - k + 1):
    #                 diag, rev_diag = 0, 0

    #                 for d in range(k):
    #                     diag += grid[r + d][c + d]
    #                     rev_diag += grid[r + d][c + k - 1 - d]
                    
    #                 all_equal = diag == rev_diag
    #                 nr, nc = r, c
    #                 while nr < r + k and all_equal:
    #                     all_equal = diag == get_row_sum(nr, c, c + k - 1)
    #                     nr += 1
                    
    #                 while nc < c + k and all_equal:
    #                     all_equal = diag == get_col_sum(nc, r, r + k - 1)
    #                     nc += 1
                    
    #                 if all_equal:
    #                     return True
            
    #         return False
        
    #     for k in range(min(m, n), 1, -1):
    #         if test_size(k):
    #             return k
        
    #     return 1
        

        
def main():
    sol = Solution()
    print(sol.largestMagicSquare(grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))
    print(sol.largestMagicSquare(grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]))

if __name__ == '__main__':
    main()