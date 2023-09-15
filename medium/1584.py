from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_dist(p1: List[int], p2: List[int]):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        distance_dict = { 0: 0 }
        res = 0

        while heap:
            w, node = heapq.heappop(heap)

            if visited[node] or distance_dict.get(node, float('inf')) < w:
                continue

            visited[node] = True
            res += w

            for v in range(n):
                if not visited[v]:
                    dist = get_dist(points[node], points[v])

                    if dist < distance_dict.get(v, float('inf')):
                        distance_dict[v] = dist
                        heapq.heappush(heap, (dist, v))
            
        return res


def main():
    sol = Solution()
    print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
    print(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))

if __name__ == '__main__':
    main()