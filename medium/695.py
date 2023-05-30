from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(row: int, col: int):
            cur_area = 1
            visited.add((row, col))
            for adj_row, adj_col in directions:
                move_row = row + adj_row
                move_col = col + adj_col
                if 0 <= move_row < m and 0 <= move_col < n and grid[move_row][move_col] and (move_row, move_col) not in visited:
                    cur_area += dfs(move_row, move_col)
            return cur_area
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j]:
                    res = max(res, dfs(i, j))
        
        return res



def main():
    sol = Solution()
    print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                               [0,0,0,0,0,0,0,1,1,1,0,0,0],
                               [0,1,1,0,1,0,0,0,0,0,0,0,0],
                               [0,1,0,0,1,1,0,0,1,0,1,0,0],
                               [0,1,0,0,1,1,0,0,1,1,1,0,0],
                               [0,0,0,0,0,0,0,0,0,0,1,0,0],
                               [0,0,0,0,0,0,0,1,1,1,0,0,0],
                               [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))

if __name__ == '__main__':
    main()