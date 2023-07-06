from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heapq.heappush(heap, (x * x + y * y, x, y))
        
        return [[x, y] for d, x, y in heapq.nsmallest(k, heap)]

def main():
    sol = Solution()
    print(sol.kClosest(points = [[1,3],[-2,2]], k = 1))
    print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))

if __name__ == '__main__':
    main()