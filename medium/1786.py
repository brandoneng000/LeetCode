from typing import List
from functools import lru_cache
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        def dijkstra():
            heap = [(0, n)]
            dist = [float('inf')] * (n + 1)
            dist[n] = 0

            while heap:
                d, u = heappop(heap)

                if d != dist[u]:
                    continue
                for w, v in graph[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heappush(heap, (dist[v], v))
            
            return dist

        @lru_cache(None)
        def dfs(src: int):
            if src == n:
                return 1
            
            res = 0
            for _, neighbor in graph[src]:
                if dist[src] > dist[neighbor]:
                    res = (res + dfs(neighbor)) % mod
            
            return res
        
        if n == 1:
            return 0
        
        graph = defaultdict(list)
        mod = 1000000007

        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        dist = dijkstra()
        return dfs(1)
        
def main():
    sol = Solution()
    print(sol.countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))
    print(sol.countRestrictedPaths(n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))

if __name__ == '__main__':
    main()