from typing import List
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf') for j in range(n)] for i in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()

            for r, c in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if not (0 <= r < m and 0 <= c < n):
                    continue

                if dist[x][y] + grid[r][c] < dist[r][c]:
                    dist[r][c] = dist[x][y] + grid[r][c]
                    q.append((r, c))
        
        return dist[m - 1][n - 1]

        

def main():
    sol = Solution()
    print(sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
    print(sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))

if __name__ == '__main__':
    main()