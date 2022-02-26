from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island_perimeter = 0

        for row_index, row in enumerate(grid):
            for column_index, column in enumerate(row):
                if column == 1:
                    perimeter = 4

                    if column_index - 1 >= 0:
                        perimeter -= row[column_index - 1]
                    if column_index + 1 < len(row):
                        perimeter -= row[column_index + 1]
                    if row_index - 1 >= 0:
                        perimeter -= grid[row_index - 1][column_index]
                    if row_index + 1 < len(grid):
                        perimeter -= grid[row_index + 1][column_index]
                    
                    island_perimeter += perimeter

        return island_perimeter

def main():
    sol = Solution()
    print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

if __name__ == '__main__':
    main()