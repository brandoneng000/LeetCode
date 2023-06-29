from typing import List
import collections
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(grid)
        first_island = set()
        next_to_water = set()
        cur_grid = [[float('inf') if grid[i][j] == 0 else -1 for j in range(n)] for i in range(n)]
        
        def traverse_island(cur_r: int, cur_c: int, island: set):
            island.add((cur_r, cur_c))

            for adj_r, adj_c in directions:
                r = cur_r + adj_r
                c = cur_c + adj_c
                if 0 <= r < n and 0 <= c < n and (r, c) not in island and grid[r][c] == 1:
                    traverse_island(r, c, island)
                elif 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                    next_to_water.add((cur_r, cur_c))
        
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    traverse_island(i, j, first_island)
                    found = True
                    break
            if found:
                break
        
        q = collections.deque(next_to_water)
        dist = 0
        while q:
            size = len(q)
            dist += 1
            for _ in range(size):
                cur_r, cur_c = q.popleft()
                
                for adj_r, adj_c in directions:
                    r = cur_r + adj_r
                    c = cur_c + adj_c
                    if 0 <= r < n and 0 <= c < n and (r, c) not in first_island and cur_grid[r][c] == -1:
                        return cur_grid[cur_r][cur_c]
                    elif 0 <= r < n and 0 <= c < n and (r, c) not in first_island and cur_grid[r][c] == float('inf'):
                        cur_grid[r][c] = dist
                        q.append((r, c))


def main():
    sol = Solution()
    print(sol.shortestBridge([[0,1],[1,0]]))
    print(sol.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
    print(sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))

if __name__ == '__main__':
    main()