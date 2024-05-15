from typing import List
from collections import deque
from heapq import heappush, heappop

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def bfs():
            q = deque()
            min_dist = {}
            
            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0
            
            while q:
                r, c, dist = q.popleft()
                nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

                for r2, c2 in nei:
                    if (r2, c2) not in min_dist and 0 <= r2 < n and 0 <= c2 < n:
                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist + 1])
                
            return min_dist
        
        n = len(grid)
        min_dist = bfs()
        max_heap = [(-min_dist[(0, 0)], 0, 0)]
        visited = set([(0, 0)])

        while max_heap:
            dist, r, c = heappop(max_heap)
            dist = -dist

            if r == n - 1 and c == n - 1:
                return dist
            
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for r2, c2 in nei:
                if (r2, c2) not in visited and 0 <= r2 < n and 0 <= c2 < n:
                    visited.add((r2, c2))
                    dist2 = min(dist, min_dist[(r2, c2)])
                    heappush(max_heap, (-dist2, r2, c2))

        
def main():
    sol = Solution()
    print(sol.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))
    print(sol.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]))
    print(sol.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))

if __name__ == '__main__':
    main()