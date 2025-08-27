from typing import List
from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(cx, cy, direction, turn, target):
            nx, ny = cx + DIR[direction][0], cy + DIR[direction][1]

            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != target:
                return 0
            
            max_step = dfs(nx, ny, direction, turn, 2 - target)

            if turn:
                max_step = max(
                    max_step,
                    dfs(nx, ny, (direction + 1) % 4, False, 2 - target)
                )
            
            return max_step + 1

        DIR = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        res = max(res, dfs(i, j, direction, True, 2) + 1)
        
        return res

        
def main():
    sol = Solution()
    print(sol.lenOfVDiagonal([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))
    print(sol.lenOfVDiagonal([[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))
    print(sol.lenOfVDiagonal([[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]))
    print(sol.lenOfVDiagonal([[1]]))

if __name__ == '__main__':
    main()