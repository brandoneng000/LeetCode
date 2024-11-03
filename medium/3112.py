from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        def dijkstra(n: int, graph: dict, disappear: List[int]):
            heap = []
            heappush(heap, [0, 0])
            dist = [float('inf')] * n
            visited = set()
            dist[0] = 0

            while heap:
                weight, node = heappop(heap)

                if node in visited:
                    continue
                visited.add(node)
                
                for nei, nei_weight in graph[node]:
                    if weight + nei_weight >= disappear[nei]:
                        continue
                    if dist[nei] > dist[node] + nei_weight:
                        dist[nei] = dist[node] + nei_weight
                        heappush(heap, [dist[nei], nei])
            
            return dist

        graph = defaultdict(list)

        for u, v, weight in edges:
            graph[u].append([v, weight])
            graph[v].append([u, weight])
        
        res = dijkstra(n, graph, disappear)
        return [dist if dist != float('inf') else -1 for dist in res]

        
def main():
    sol = Solution()
    print(sol.minimumTime(n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]))
    print(sol.minimumTime(n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]))
    print(sol.minimumTime(n = 2, edges = [[0,1,1]], disappear = [1,1]))

if __name__ == '__main__':
    main()