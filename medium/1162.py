from typing import List
import collections

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = collections.deque()
        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1)) 
        res = -1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        if not q or len(q) == n * n:
            return -1
        
        while q:
            size = len(q)
            res += 1

            for _ in range(size):
                cur_x, cur_y = q.popleft()

                for adj_x, adj_y in directions:
                    x = cur_x + adj_x
                    y = cur_y + adj_y
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                        visited.add((x, y))
                        q.append((x, y))
        
        return res

    # def maxDistance(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     dist = [[0 if grid[i][j] else float('inf') for j in range(n)] for i in range(n)]
    #     directions = ((1, 0), (0, 1), (-1, 0), (0, -1)) 

    #     def dfs(cur_x: int, cur_y: int, distance: int):
    #         dist[cur_x][cur_y] = distance

    #         for adj_x, adj_y in directions:
    #             x = cur_x + adj_x
    #             y = cur_y + adj_y
    #             if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and dist[x][y] > distance + 1:
    #                 dfs(x, y, distance + 1)
            
    #     for i in range(n):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 dfs(i, j, 0)
        
    #     res = max(map(max, dist))
    #     if res == 0 or res == float('inf'):
    #         return -1

    #     return res

def main():
    sol = Solution()
    print(sol.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
    print(sol.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))

if __name__ == '__main__':
    main()