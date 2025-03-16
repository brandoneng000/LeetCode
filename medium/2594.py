from typing import List
from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        count = Counter(ranks)
        heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(heap)

        while cars > 0:
            time, rank, n, count = heappop(heap)

            cars -= count
            n += 1
            heappush(heap, [rank * n * n, rank, n, count])
        
        return time
    
    # def repairCars(self, ranks: List[int], cars: int) -> int:
    #     left = 1
    #     right = cars * cars * ranks[0]

    #     while left < right:
    #         middle = (left + right) // 2
    #         cars_repaired = sum((int((middle // rank) ** 0.5) for rank in ranks))

    #         if cars_repaired < cars:
    #             left = middle + 1
    #         else:
    #             right = middle

    #     return left

    # def repairCars(self, ranks: List[int], cars: int) -> int:
    #     def cars_repaired(time: int):
    #         cars = 0

    #         for r in ranks:
    #             cars += int((time // r) ** 0.5)
            
    #         return cars

    #     left, right = 1, max(ranks) * cars * cars

    #     while left < right:
    #         middle = (left + right) // 2

    #         if cars_repaired(middle) >= cars:
    #             right = middle
    #         else:
    #             left = middle + 1
        
    #     return left

        
def main():
    sol = Solution()
    print(sol.repairCars(ranks = [4,2,3,1], cars = 10))
    print(sol.repairCars(ranks = [5,1,8], cars = 6))

if __name__ == '__main__':
    main()