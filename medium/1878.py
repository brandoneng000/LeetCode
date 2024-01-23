from typing import List
from heapq import heappush, heappop
from functools import lru_cache

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        heap = []

        def update_heap(heap: List[int], num: int):
            if num not in heap:
                heappush(heap, num)
                if len(heap) > 3:
                    heappop(heap)
            
            return heap
        
        for row in grid:
            for num in row:
                update_heap(heap, num)
        
        @lru_cache(None)
        def dp(i, j, dr):
            if not 0 <= i < n or not 0 <= j < m:
                return 0
            return dp(i - 1, j + dr, dr) + grid[j][i]
        
        for q in range(1, (1 + min(m, n)) // 2):
            for i in range(q, n - q):
                for j in range(q, m - q):
                    p1 = dp(i + q, j, -1) - dp(i, j - q, -1)
                    p2 = dp(i - 1, j + q - 1, -1) - dp(i - q - 1, j - 1, -1)
                    p3 = dp(i, j - q, 1) - dp(i - q, j, 1)
                    p4 = dp(i + q - 1, j + 1, 1) - dp(i - 1, j + q + 1, 1)
                    update_heap(heap, p1 + p2 + p3 + p4)
        
        return sorted(heap, reverse=True)


def main():
    sol = Solution()
    print(sol.getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]))
    print(sol.getBiggestThree([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.getBiggestThree([[7,7,7]]))

if __name__ == '__main__':
    main()