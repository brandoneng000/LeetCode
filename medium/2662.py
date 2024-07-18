from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        special = [[x1, y1, x2, y2, cost] for x1, y1, x2, y2, cost in specialRoads if cost < abs(x2 - x1) + abs(y2 - y1)]
        distance = { tuple(start): 0 }
        heap = [[0, start[0], start[1]]]

        while heap:
            cur_dist, x, y = heappop(heap)

            for x1, y1, x2, y2, cost in special:
                if distance.get((x2, y2), float('inf')) > cur_dist + abs(x - x1) + abs(y - y1) + cost:
                    distance[(x2, y2)] = cur_dist + abs(x - x1) + abs(y - y1) + cost
                    heappush(heap, (distance[(x2, y2)], x2, y2))
        
        res = abs(target[0] - start[0]) + abs(target[1] - start[1])

        for x1, y1, x2, y2, cost in special:
            res = min(res, distance.get((x2, y2), float('inf')) + abs(target[0] - x2) + abs(target[1] - y2))
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.minimumCost(start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]))
    print(sol.minimumCost(start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]))
    print(sol.minimumCost(start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]))

if __name__ == '__main__':
    main()