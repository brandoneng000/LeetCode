from typing import List
from heapq import heappush, heappop

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        res = 0
        i = 0
        heap = []

        while i < n or heap:
            if i < n and apples[i] > 0:
                heappush(heap, [i + days[i], apples[i]])

            while heap and (heap[0][0] <= i or heap[0][1] <= 0):
                heappop(heap)
            
            if heap:
                heap[0][1] -= 1
                res += 1
            i += 1
        
        return res
        

    # def eatenApples(self, apples: List[int], days: List[int]) -> int:
    #     heap = []
    #     cur_day = 0
    #     res = 0

    #     for apple, rot in zip(apples, days):
    #         rotten = cur_day + rot
    #         heappush(heap, (rotten, apple))

    #         while heap:
    #             rotten, a = heappop(heap)

    #             if cur_day >= rotten:
    #                 continue

    #             a -= 1
    #             res += 1
    #             if a > 0:
    #                 heappush(heap, (rotten, a))
    #             break

    #         cur_day += 1
        
    #     while heap:
    #         rotten, a = heappop(heap)

    #         if cur_day >= rotten:
    #             continue

    #         next_days = min(rotten, cur_day + a)
    #         res += next_days - cur_day
    #         cur_day = next_days

    #     return res

        
def main():
    sol = Solution()
    print(sol.eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2]))
    print(sol.eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]))

if __name__ == '__main__':
    main()