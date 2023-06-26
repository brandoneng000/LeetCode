from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        
        left, right = 0, len(costs) - 1
        res = 0

        for i in range(candidates):
            left = i
            right = len(costs) - i - 1
            if left <= right:
                heapq.heappush(heap, (costs[left], left))
            if left < right:
                heapq.heappush(heap, (costs[right], right))
        
        left += 1
        right -= 1
        
        while k:
            c, i = heapq.heappop(heap)

            if left <= right:
                if i < left:
                    heapq.heappush(heap, (costs[left], left))
                    left += 1
                elif i >= right:
                    heapq.heappush(heap, (costs[right], right))
                    right -= 1
            res += c
            k -= 1
        
        return res

    # def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    #     if len(costs) == k:
    #         return sum(costs)
        
    #     res = 0

    #     while k:
    #         k -= 1
    #         left = costs[:candidates]
    #         right = costs[-candidates:]
    #         left_min = min(left)
    #         right_min = min(right)
    #         if left_min <= right_min:
    #             res += left_min
    #             costs.pop(costs.index(left_min))
    #         else:
    #             res += right_min
    #             costs.pop(costs.index(right_min, len(costs) - candidates))

    #     return res


def main():
    sol = Solution()
    print(sol.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 9, candidates = 4))
    print(sol.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))
    print(sol.totalCost(costs = [1,2,4,1], k = 3, candidates = 3))

if __name__ == '__main__':
    main()