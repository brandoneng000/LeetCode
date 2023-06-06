from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        prices = [[float('inf') for i in range(k + 2)] for j in range(n)]
        heap = []

        for source, dest, price in flights:
            graph[source].append((dest, price))
        heapq.heappush(heap, (0, src, k + 1))

        while heap:
            price, cur_loc, stops = heapq.heappop(heap)

            if cur_loc == dst:
                return price

            if stops > 0:
                for travel, cost in graph[cur_loc]:
                    new_cost = price + cost
                    if prices[travel][stops] > new_cost:
                        heapq.heappush(heap, (price + cost, travel, stops - 1))
                        prices[travel][stops] = price + cost

        return -1


    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    #     graph = collections.defaultdict(list)
    #     visited = set()
    #     for source, dest, price in flights:
    #         graph[source].append((dest, price))

    #     def helper(cur_loc: int, cur_price: int, flight_remaining: int):
    #         if cur_loc == dst:
    #             return cur_price
    #         if flight_remaining < 0:
    #             return float('inf')

    #         price = float('inf')
    #         visited.add(cur_loc)
    #         for travel, cost in graph[cur_loc]:
    #             if travel not in visited:
    #                 price = min(price, helper(travel, cur_price + cost, flight_remaining - 1))
    #         visited.remove(cur_loc)

    #         return price
        
    #     min_price = helper(src, 0, k)
    #     return min_price if min_price != float('inf') else -1


def main():
    sol = Solution()
    print(sol.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
    print(sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
    print(sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))

if __name__ == '__main__':
    main()