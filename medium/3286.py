from typing import List
from heapq import heappush, heappop

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        goal = (m - 1, n - 1)
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        heap = []
        heappush(heap, (-(health - grid[0][0]), 0, 0))

        while heap:
            hp, row, col = heappop(heap)
            hp = -hp

            if (row, col) == goal:
                return True
            
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if 0 <= r < m and 0 <= c < n and (r, c) not in visited and hp - grid[r][c] > 0:
                    visited.add((r, c))
                    heappush(heap, (-(hp - grid[r][c]), r, c))
        
        return False

        
        
def main():
    sol = Solution()
    print(sol.findSafeWalk(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1))
    print(sol.findSafeWalk(grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3))
    print(sol.findSafeWalk(grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5))

if __name__ == '__main__':
    main()