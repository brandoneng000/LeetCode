from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        cross_index = len(grid) - 1

        for index, row in enumerate(grid):
            if grid[index][index] == 0 or grid[index][cross_index] == 0:
                return False
            if sum(row) != grid[index][index] + (grid[index][cross_index] if index != cross_index else 0):
                return False
            cross_index -= 1

        return True

def main():
    sol = Solution()
    print(sol.checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
    print(sol.checkXMatrix([[5,7,0],[0,3,1],[0,5,0]]))

if __name__ == '__main__':
    main()