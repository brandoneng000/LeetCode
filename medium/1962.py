from typing import List
from heapq import heappop, heappush, heapify

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)

        while k:
            k -= 1
            cur = heappop(heap)
            heappush(heap, cur + (-cur // 2))
        
        return -sum(heap)
        
def main():
    sol = Solution()
    print(sol.minStoneSum(piles = [5,4,9], k = 2))
    print(sol.minStoneSum(piles = [4,3,6,7], k = 3))

if __name__ == '__main__':
    main()