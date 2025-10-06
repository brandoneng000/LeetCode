from typing import List
from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        goal = (n - 1, n - 1)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        res = grid[0][0]
        heap = []
        visited.add((0, 0))
        heappush(heap, (res, 0, 0))

        while heap:
            val, row, col = heappop(heap)
            res = max(res, val)

            if (row, col) == goal:
                return res

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if 0 <= r < n and 0 <= c < n and (r, c) not in visited:
                    visited.add((r, c))
                    heappush(heap, (grid[r][c], r, c))

        return -1


def main():
    sol = Solution()
    print(sol.swimInWater([[0,2],[1,3]]))
    print(sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))

if __name__ == '__main__':
    main()