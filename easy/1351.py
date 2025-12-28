from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] < 0:
                    res += m - j
                    break
        
        return res

    # def countNegatives(self, grid: List[List[int]]) -> int:
    #     negatives = 0
    #     col_end = len(grid[0])

    #     for row in range(len(grid)):
    #         for col in range(col_end):
    #             if grid[row][col] < 0:
    #                 col_end = min(col_end, col)
    #                 negatives += (len(grid) - row)

    #     return negatives

def main():
    sol = Solution()
    print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(sol.countNegatives([[3,2],[1,0]]))

if __name__ == '__main__':
    main()