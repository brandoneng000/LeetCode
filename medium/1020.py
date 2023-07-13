from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bound = set()
        res = 0

        def traverse(cur_r: int, cur_c: int):
            bound.add((cur_r, cur_c))
            for d_r, d_c in directions:
                r = cur_r + d_r
                c = cur_c + d_c
                if 0 <= r < m and 0 <= c < n and (r, c) not in bound and grid[r][c] == 1:
                    traverse(r, c)
        
        for i in range(m):
            if (i, 0) not in bound and grid[i][0] == 1:
                traverse(i, 0)
            if (i, n - 1) not in bound and grid[i][n - 1] == 1:
                traverse(i, n - 1)
        
        for j in range(n):
            if (0, j) not in bound and grid[0][j] == 1:
                traverse(0, j)
            if (m - 1, j) not in bound and grid[m - 1][j] == 1:
                traverse(m - 1, j)
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if (i, j) not in bound and grid[i][j] == 1:
                    res += 1
        
        return res
    
    # def numEnclaves(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    #     res = 0

    #     def traverse(cur_r: int, cur_c: int):
    #         grid[cur_r][cur_c] = 2
    #         for d_r, d_c in directions:
    #             r = cur_r + d_r
    #             c = cur_c + d_c
    #             if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
    #                 traverse(r, c)
        
    #     for i in range(m):
    #         if grid[i][0] == 1:
    #             traverse(i, 0)
    #         if grid[i][n - 1] == 1:
    #             traverse(i, n - 1)
        
    #     for j in range(n):
    #         if grid[0][j] == 1:
    #             traverse(0, j)
    #         if grid[m - 1][j] == 1:
    #             traverse(m - 1, j)
        
    #     for i in range(1, m - 1):
    #         for j in range(1, n - 1):
    #             if grid[i][j] == 1:
    #                 res += 1
        
    #     return res

def main():
    sol = Solution()
    print(sol.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
    print(sol.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))

if __name__ == '__main__':
    main()