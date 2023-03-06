from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])

        for col in range(1, col_size):
            grid[0][col] += grid[0][col - 1]

        for row in range(1, row_size):
            grid[row][0] += grid[row - 1][0]

        for row in range(1, row_size):
            for col in range(1, col_size):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        
        return grid[row_size - 1][col_size - 1]

def main():
    sol = Solution()
    print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(sol.minPathSum([[1,2,3],[4,5,6]]))

if __name__ == '__main__':
    main()