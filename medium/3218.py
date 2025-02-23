from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        heap = []
        vertical_slices = 1
        horizontal_slices = 1
        res = 0

        for cost in horizontalCut:
            heappush(heap, (-cost, 'H'))
        
        for cost in verticalCut:
            heappush(heap, (-cost, 'V'))
        
        while heap:
            cost, dir = heappop(heap)

            if dir == 'V':
                res += horizontal_slices * -cost
                vertical_slices += 1
            
            if dir == 'H':
                res += vertical_slices * -cost
                horizontal_slices += 1
        
        return res


def main():
    sol = Solution()
    print(sol.minimumCost(m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]))
    print(sol.minimumCost(m = 2, n = 2, horizontalCut = [7], verticalCut = [4]))

if __name__ == '__main__':
    main()