from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        heap = [(grid[0][0], 0, 0)]

        while heap:
            time, row, col = heappop(heap)

            if row == m - 1 and col == n - 1:
                return time
            
            if (row, col) in visited:
                continue

            visited.add((row, col))

            for dr, dc in direction:
                r = row + dr
                c = col + dc

                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    wait_time = 1 if (grid[r][c] - time) % 2 == 0 else 0
                    next_time = max(grid[r][c] + wait_time, time + 1)
                    heappush(heap, (next_time, r, c))
        
        return -1
        
def main():
    sol = Solution()
    print(sol.minimumTime(grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]))
    print(sol.minimumTime(grid = [[0,2,4],[3,2,1],[1,0,4]]))

if __name__ == '__main__':
    main()