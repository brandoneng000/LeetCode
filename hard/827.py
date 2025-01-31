from typing import List
from collections import deque

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(row: int, col: int, island_id: List[List[int]], grid: List[List[int]], m: int, n: int, directions: List[tuple], id: int):
            q = deque([(row, col)])
            res = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and island_id[r][c] == 0:
                        island_id[r][c] = id
                        q.append((r, c))
                        res += 1
            
            return res


        m, n = len(grid), len(grid[0])
        island_size = {}
        island_id = [[0 for j in range(n)] for i in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cur_id = 1
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and island_id[i][j] == 0:
                    island_id[i][j] = cur_id
                    island_size[cur_id] = bfs(i, j, island_id, grid, m, n, directions, cur_id)
                    res = max(res, island_size[cur_id])
                    cur_id += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    islands = set()

                    for dr, dc in directions:
                        r = i + dr
                        c = j + dc

                        if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                            islands.add(island_id[r][c])
                    
                    new_island = sum(island_size[id] for id in islands) + 1
                    res = max(res, new_island)
        
        return res

        
def main():
    sol = Solution()
    print(sol.largestIsland([[1,0],[0,1]]))
    print(sol.largestIsland([[1,1],[1,0]]))
    print(sol.largestIsland([[1,1],[1,1]]))

if __name__ == '__main__':
    main()