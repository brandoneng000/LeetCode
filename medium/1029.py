from typing import List
import heapq

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        n = len(costs) // 2
        res = 0
        for a, b in costs:
            refund.append(b - a)
            res += a
        
        refund.sort()
        for i in range(n):
            res += refund[i]
        
        return res

    # def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    #     heap = []
    #     n = len(costs) // 2

    #     for a, b in costs:
    #         heapq.heappush(heap, (-(abs(a - b)), a, b))

    #     city_a = []
    #     city_b = []
    #     temp = []

    #     while heap:
    #         _, a, b = heapq.heappop(heap)

    #         if len(city_a) < n and (a < b or len(city_b) == n):
    #             city_a.append(a)
    #         elif len(city_b) < n and (a > b or len(city_a) == n):
    #             city_b.append(b)
    #         else:
    #             temp.append(a)
        
    #     return sum(city_a) + sum(city_b) + sum(temp)
        


def main():
    sol = Solution()
    print(sol.twoCitySchedCost([[10,20],[30,200],[400,50],[20,20]]))
    print(sol.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
    print(sol.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
    print(sol.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))

if __name__ == '__main__':
    main()