from typing import List
from heapq import heappush, heappop, heapify
from math import isqrt
# import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapify(heap)

        for _ in range(k):
            heappush(heap, -isqrt(-heappop(heap)))
        
        return -sum(heap)

    # def pickGifts(self, gifts: List[int], k: int) -> int:
    #     gifts = [-gift for gift in gifts]
    #     heapq.heapify(gifts)
    #     for _ in range(k):
    #         temp = -heapq.heappop(gifts)
    #         heapq.heappush(gifts, -int(temp ** 0.5))
        
    #     return -sum(gifts)

        # for _ in range(k):
        #     temp = max(gifts)
        #     gifts.remove(temp)
        #     gifts.append(int(temp ** 0.5))
        
        # return sum(gifts)

def main():
    sol = Solution()
    print(sol.pickGifts(gifts = [25,64,9,4,100], k = 4))
    print(sol.pickGifts(gifts = [1,1,1,1], k = 4))

if __name__ == '__main__':
    main()