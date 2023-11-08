from typing import List
from heapq import heappop, heappush

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []

        for i in range(n - 1):
            dist = heights[i + 1] - heights[i]
            if dist > 0:
                heappush(heap, dist)
            
            if len(heap) > ladders:
                bricks -= heappop(heap)
            
            if bricks < 0:
                return i
        
        return n - 1
        
def main():
    sol = Solution()
    print(sol.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
    print(sol.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
    print(sol.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))

if __name__ == '__main__':
    main()