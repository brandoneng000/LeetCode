from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # self.surface_area = 0
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         blocks = grid[i][j]
        #         if blocks == 0:
        #             continue
        #         elif blocks == 1:
        #             cur_area = 6
        #         elif blocks == 2:
        #             cur_area = 10
        #         else:
        #             cur_area = 10 + ((blocks - 2) * 4)
        #         for dx, dy in directions:
        #             i_dx = i + dx
        #             j_dy = j + dy
        #             if 0 <= i_dx < len(grid) and 0 <= j_dy < len(grid[0]) and grid[i_dx][j_dy] != 0:
        #                 cur_area -= min(grid[i][j], grid[i_dx][j_dy])
        #         self.surface_area += cur_area

        # return self.surface_area
        self.surface_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                blocks = grid[i][j]
                if blocks == 0:
                    continue
                else:
                    cur_area = 6 * grid[i][j] - 2 * (grid[i][j] - 1)
                if i > 0:
                    cur_area -= 2 * min(grid[i][j], grid[i - 1][j])
                if j > 0:
                    cur_area -= 2 * min(grid[i][j], grid[i][j - 1])
                self.surface_area += cur_area

        return self.surface_area

def main():
    sol = Solution()
    # print(sol.surfaceArea([[5]]))
    # print(sol.surfaceArea([[1], [1]]))

    print(sol.surfaceArea([[1,2],[3,4]]))
    print(sol.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
    print(sol.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))

if __name__ == '__main__':
    main()