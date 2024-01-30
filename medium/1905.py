from typing import List
from collections import deque

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def search_island(grid: List[List[int]], visited: set, origin_r: int, origin_c: int):
            q = deque([(origin_r, origin_c)])
            island = set([(origin_r, origin_c)])

            while q:
                origin_r, origin_c = q.popleft()

                for dr, dc in directions:
                    r = origin_r + dr
                    c = origin_c + dc
                    
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        island.add((r, c))
                        visited.add((r, c))
                    elif 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                        visited.add((r, c))
            
            return island


        m, n = len(grid1), len(grid1[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        islands = set()
        visited = set()
        res = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid1[i][j] == 1:
                    visited.add((i, j))
                    islands |= search_island(grid1, visited, i, j)
                visited.add((i, j))
        
        visited.clear()

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid2[i][j] == 1:
                    visited.add((i, j))
                    if not (search_island(grid2, visited, i, j) - islands):
                        res += 1
                visited.add((i, j))
        
        return res
        

def main():
    sol = Solution()
    print(sol.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
    print(sol.countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))

if __name__ == '__main__':
    main()