from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = [[int(grid[i][j]) for j in range(n)] for i in range(m)]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        res = 0
        
        for i in range(m):
            for j in range(n):
                if islands[i][j] == 0:
                    continue

                res += 1
                islands[i][j] = 0
                q = deque([(i, j)])
                while q:
                    row, col = q.popleft()

                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if 0 <= r < m and 0 <= c < n and islands[r][c] == 1:
                            islands[r][c] = 0
                            q.append((r, c))
        
        return res

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0

    #     rows, cols = len(grid), len(grid[0])
    #     visit = set()
    #     islands = 0

    #     def bfs(r, c):
    #         q = collections.deque()
    #         visit.add((r,c))
    #         q.append((r,c))

    #         # This is BFS to turn into DFS change popleft() -> pop()
    #         while q:
    #             row, col = q.popleft()
    #             directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
    #             for dr, dc in directions:
    #                 r, c = row + dr, col + dc
    #                 if (r in range(rows) and c in range(cols) and
    #                     grid[r][c] == "1" and (r, c) not in visit):
    #                    q.append((r, c))
    #                    visit.add((r, c))


    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == "1" and (r, c) not in visit:
    #                 bfs(r, c)
    #                 islands += 1
        
    #     return islands


def main():
    sol = Solution()
    print(sol.numIslands([
                        ["1","1","1","1","0"],
                        ["1","1","0","1","0"],
                        ["1","1","0","0","0"],
                        ["0","0","0","0","0"]
                        ]))

if __name__ == '__main__':
    main()