from typing import List
from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float('inf')
        heap = []
        total_quality = 0
        ratio = [(w / q, q) for q, w in zip(quality, wage)]
        ratio.sort()

        for r, q in ratio:
            heappush(heap, -q)
            total_quality += q

            if len(heap) > k:
                total_quality += heappop(heap)

            if len(heap) == k:
                res = min(res, total_quality * r)

        return res        

        
def main():
    sol = Solution()
    print(sol.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2))
    print(sol.mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3))

if __name__ == '__main__':
    main()