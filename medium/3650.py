from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        heap = []
        distance = [float('inf')] * n
        distance[0] = 0
        heappush(heap, (0, 0))

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w * 2))

        while heap:
            dist, node = heappop(heap)

            if dist > distance[node]:
                continue

            for v, w in graph[node]:
                if distance[node] + w < distance[v]:
                    distance[v] = distance[node] + w
                    heappush(heap, (distance[v], v))
        
        return distance[n - 1] if distance[n - 1] != float('inf') else -1
        
def main():
    sol = Solution()
    print(sol.minCost(n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]))
    print(sol.minCost(n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]))

if __name__ == '__main__':
    main()