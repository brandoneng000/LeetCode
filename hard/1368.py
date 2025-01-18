from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cost_grid = [[float('inf') for j in range(n)] for i in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = []

        heappush(heap, (0, 0, 0))

        while heap:
            cur_cost, row, col = heappop(heap)

            if (row, col) == (m - 1, n - 1):
                return cur_cost
            
            for i in range(4):
                if i == grid[row][col] - 1:
                    next_cost = cur_cost
                else:
                    next_cost = cur_cost + 1
                
                r = row + directions[i][0]
                c = col + directions[i][1]

                if 0 <= r < m and 0 <= c < n and next_cost < cost_grid[r][c]:
                    cost_grid[r][c] = next_cost
                    heappush(heap, (next_cost, r, c))

        return -1

        
def main():
    sol = Solution()
    print(sol.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
    print(sol.minCost([[1,1,3],[3,2,2],[1,1,4]]))
    print(sol.minCost([[1,2],[4,3]]))

if __name__ == '__main__':
    main()