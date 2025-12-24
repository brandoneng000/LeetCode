from typing import List
from heapq import heappush, heappop

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        res = []

        for x, y in queries:
            heappush(heap, -(abs(x) + abs(y)))

            if len(heap) > k:
                heappop(heap)
            
            if len(heap) < k:
                res.append(-1)
            else:
                res.append(-heap[0])

        return res



def main():
    sol = Solution()
    print(sol.resultsArray(queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2))
    print(sol.resultsArray(queries = [[5,5],[4,4],[3,3]], k = 1))

if __name__ == '__main__':
    main()