from typing import List
from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        res = 0

        heap_boundary = []

        for i in range(m):
            heappush(heap_boundary, (heightMap[i][0], i, 0))
            heappush(heap_boundary, (heightMap[i][n - 1], i, n - 1))
            visited.add((i, 0))
            visited.add((i, n - 1))

        for i in range(n):
            heappush(heap_boundary, (heightMap[0][i], 0, i))
            heappush(heap_boundary, (heightMap[m - 1][i], m - 1, i))
            visited.add((0, i))
            visited.add((m - 1, i))
        
        while heap_boundary:
            min_boundary_height, cur_row, cur_col = heappop(heap_boundary)

            for dr, dc in directions:
                r = cur_row + dr
                c = cur_col + dc

                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    neighbor_height = heightMap[r][c]

                    if neighbor_height < min_boundary_height:
                        res += min_boundary_height - neighbor_height
                    
                    heappush(heap_boundary, (max(neighbor_height, min_boundary_height), r, c))
                    visited.add((r, c))
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
    print(sol.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))

if __name__ == '__main__':
    main()