from typing import List
from heapq import heappush, heappop
from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        dist = 0
        heap = []
        visited = set([(start[0], start[1])])
        q = deque([start])

        while q:
            size = len(q)
            
            for _ in range(size):
                cur_r, cur_c = q.popleft()

                if grid[cur_r][cur_c] != 1 and pricing[0] <= grid[cur_r][cur_c] <= pricing[1]:
                    heappush(heap, (-dist, -grid[cur_r][cur_c], -cur_r, -cur_c))

                    if len(heap) > k:
                        heappop(heap)

                for dr, dc in directions:
                    r = cur_r + dr
                    c = cur_c + dc

                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited and grid[r][c] != 0:
                        visited.add((r, c))
                        q.append((r, c))
            
            dist += 1
            if len(heap) == k:
                break
        
        res = []

        while heap:
            d, p, r, c = heappop(heap)
            res.append([-r, -c])

        return res[::-1]
        
        
def main():
    sol = Solution()
    print(sol.highestRankedKItems(grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3))
    print(sol.highestRankedKItems(grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2))
    print(sol.highestRankedKItems(grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3))

if __name__ == '__main__':
    main()