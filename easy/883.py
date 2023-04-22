from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_area = sum(len(g) for g in grid)
        xz_area = sum(max(g) for g in grid)
        yz_area = 0
        for i in range(len(grid)):
            col_max = 0
            for j in range(len(grid)):
                col_max =  max(col_max, grid[j][i])
            yz_area += col_max

        return xy_area + xz_area + yz_area - sum(grid, []).count(0)

def main():
    sol = Solution()
    print(sol.projectionArea([[1,2],[3,4]]))
    print(sol.projectionArea([[2]]))
    print(sol.projectionArea([[1,0],[0,2]]))

if __name__ == '__main__':
    main()