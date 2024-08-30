from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def dijkstra(graph: defaultdict, dist_to: List[int], heap: List[List[int]]):
            while heap:
                cur_dist, cur = heappop(heap)

                for nei in graph[cur]:
                    if graph[cur][nei] > 0:
                        if dist_to[nei] - graph[cur][nei] > dist_to[cur]:
                            dist_to[nei] = dist_to[cur] + graph[cur][nei]
                            heappush(heap, (dist_to[nei], nei))
        
        def fill(edges: List[List[int]]):
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = int(2e9)
            
            return edges

        graph = defaultdict(dict)

        for u, v, weight in edges:
            graph[u][v] = weight
            graph[v][u] = weight
        
        dist_to = [float('inf')] * n
        dist_to[source] = 0

        heap = []
        heappush(heap, (0, source))

        dijkstra(graph, dist_to, heap)

        if dist_to[destination] == target:
            return fill(edges)
        elif dist_to[destination] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1
                u, v, weight = edge
                graph[u][v] = weight
                graph[v][u] = weight

                heap = []
                heappush(heap, (dist_to[u], u))
                heappush(heap, (dist_to[v], v))

                dijkstra(graph, dist_to, heap)

                if dist_to[destination] == target:
                    return fill(edges)
                elif dist_to[destination] < target:
                    edge[2] += target - dist_to[destination]
                    graph[u][v] = edge[2]
                    graph[v][u] = edge[2]
                    return fill(edges)
        
        return []

        
def main():
    sol = Solution()
    print(sol.modifiedGraphEdges(n = 5, edges = [[1,4,1],[2,4,-1],[3,0,2],[0,4,-1],[1,3,10],[1,0,10]], source = 0, destination = 2, target = 15))
    print(sol.modifiedGraphEdges(n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5))
    print(sol.modifiedGraphEdges(n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6))
    print(sol.modifiedGraphEdges(n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6))

if __name__ == '__main__':
    main()