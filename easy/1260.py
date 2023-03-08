from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift_one(grid):
            temp = grid[-1][-1]
            for row in grid:
                row.insert(0, temp)
                temp = row.pop()
            return grid
        
        for _ in range(k):
            shift_one(grid)

        return grid

def main():
    sol = Solution()
    print(sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
    print(sol.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
    print(sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))

if __name__ == '__main__':
    main()