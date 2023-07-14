from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        original_color = grid[row][col]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m, n = len(grid), len(grid[0])
        visited = set()
        shift = set()

        def dfs(row: int, col: int):
            visited.add((row, col))
            for adj_r, adj_c in directions:
                r = row + adj_r
                c = col + adj_c
                if r < 0 or r == m or c < 0 or c == n:
                    shift.add((row, col))
                elif 0 <= r < m and 0 <= c < n:
                    if grid[r][c] != original_color:
                        shift.add((row, col))
                    elif grid[r][c] == original_color and (r, c) not in visited:
                        dfs(r, c)
        
        dfs(row, col)
        for r, c in shift:
            grid[r][c] = color

        return grid
    
    # def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    #     original_color = grid[row][col]
    #     directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    #     m, n = len(grid), len(grid[0])
    #     res = [[grid[i][j] for j in range(n)] for i in range(m)]
    #     visited = set()

    #     def dfs(row: int, col: int):
    #         visited.add((row, col))
    #         for adj_r, adj_c in directions:
    #             r = row + adj_r
    #             c = col + adj_c
    #             if r < 0 or r == m or c < 0 or c == n:
    #                 res[row][col] = color
    #             elif 0 <= r < m and 0 <= c < n:
    #                 if grid[r][c] != original_color:
    #                     res[row][col] = color
    #                 elif grid[r][c] == original_color and (r, c) not in visited:
    #                     dfs(r, c)
        
    #     dfs(row, col)
    #     return res



def main():
    sol = Solution()
    print(sol.colorBorder(grid = [[1,1],[1,2]], row = 0, col = 0, color = 3))
    print(sol.colorBorder(grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3))
    print(sol.colorBorder(grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2))

if __name__ == '__main__':
    main()