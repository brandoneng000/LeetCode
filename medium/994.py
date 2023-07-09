from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rotten = collections.deque()
        fresh = 0
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while rotten and fresh > 0:
            res += 1
            
            for _ in range(len(rotten)):
                cur_r, cur_c = rotten.popleft()

                for adj_r, adj_c in directions:
                    r, c = cur_r + adj_r, cur_c + adj_c

                    if r < 0 or r == m or c < 0 or c == n:
                        continue
                    if grid[r][c] == 0 or grid[r][c] == 2:
                        continue

                    fresh -= 1
                    grid[r][c] = 2
                    rotten.append((r, c))
        
        return res if fresh == 0 else -1

    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     rotting = [[float('inf') for i in range(n)] for j in range(m)]
    #     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    #     def dfs(cur_row: int, cur_col: int, minutes: int):
    #         for adj_r, adj_c in directions:
    #             r = cur_row + adj_r
    #             c = cur_col + adj_c
    #             if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and rotting[r][c] > minutes + 1:
    #                 rotting[r][c] = min(rotting[r][c], minutes + 1)
    #                 dfs(r, c, minutes + 1)
        
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 2:
    #                 rotting[i][j] = 0
    #                 dfs(i, j, 0)
        
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 res = max(res, rotting[i][j])
        
    #     return res if res != float('inf') else -1



def main():
    sol = Solution()
    print(sol.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))
    print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(sol.orangesRotting([[0,2]]))

if __name__ == '__main__':
    main()