from typing import List
from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int, grid: List[List[int]]):
            res = 0

            if 0 <= row < m and 0 <= col < n:
                if grid[row][col] == 0:
                    return 0

                res += grid[row][col]
                grid[row][col] = 0
                res += dfs(row + 1, col, grid)
                res += dfs(row, col + 1, grid)
                res += dfs(row - 1, col, grid)
                res += dfs(row, col - 1, grid)
                
            return res

        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res = max(res, dfs(i, j, grid))
                
        return res

    # def findMaxFish(self, grid: List[List[int]]) -> int:
    #     def capture_fish(row: int, col: int):
    #         cur = 0
    #         q = deque([(row, col)])

    #         while q:
    #             row, col = q.popleft()
    #             cur += grid[row][col]

    #             for dr, dc in directions:
    #                 r = row + dr
    #                 c = col + dc

    #                 if 0 <= r < m and 0 <= c < n and (r, c) not in visited and grid[r][c] != 0:
    #                     visited.add((r, c))
    #                     q.append((r, c))
            
    #         return cur

    #     m, n = len(grid), len(grid[0])
    #     directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    #     visited = set()
    #     res = 0

    #     for i in range(m):
    #         for j in range(n):
    #             if (i, j) in visited:
    #                 continue
                
    #             visited.add((i, j))
    #             if grid[i][j] > 0:
    #                 res = max(res, capture_fish(i, j))
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
    print(sol.findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))

if __name__ == '__main__':
    main()