from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        inner_islands = set()
        border_island = set()
        res = 0

        def traverse_island(cur_r: int, cur_c: int, islands: set):
            islands.add((cur_r, cur_c))
            for dr, dc in directions:
                r = cur_r + dr
                c = cur_c + dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in islands and grid[r][c] == 0:
                    traverse_island(r, c, islands)
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in inner_islands:
                    traverse_island(i, j, inner_islands)
                    res += 1

        for i in range(m):
            if grid[i][0] == 0 and (i, 0) not in border_island:
                traverse_island(i, 0, border_island)
                res -= 1
            if grid[i][n - 1] == 0 and (i, n - 1) not in border_island:
                traverse_island(i, n - 1, border_island)
                res -= 1
        
        for j in range(n):
            if grid[0][j] == 0 and (0, j) not in border_island:
                traverse_island(0, j, border_island)
                res -= 1
            if grid[m - 1][j] == 0 and (m - 1, j) not in border_island:
                traverse_island(m - 1, j, border_island)
                res -= 1

        return res

def main():
    sol = Solution()
    print(sol.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
    print(sol.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
    print(sol.closedIsland([[1,1,1,1,1,1,1],
                            [1,0,0,0,0,0,1],
                            [1,0,1,1,1,0,1],
                            [1,0,1,0,1,0,1],
                            [1,0,1,1,1,0,1],
                            [1,0,0,0,0,0,1],
                            [1,1,1,1,1,1,1]]))
    print(sol.closedIsland([[0,0,1,1,0,1,0,0,1,0],
                            [1,1,0,1,1,0,1,1,1,0],
                            [1,0,1,1,1,0,0,1,1,0],
                            [0,1,1,0,0,0,0,1,0,1],
                            [0,0,0,0,0,0,1,1,1,0],
                            [0,1,0,1,0,1,0,1,1,1],
                            [1,0,1,0,1,1,0,0,0,1],
                            [1,1,1,1,1,1,0,0,0,0],
                            [1,1,1,0,0,1,0,1,0,1],
                            [1,1,1,0,1,1,0,1,1,0]]))
    

if __name__ == '__main__':
    main()