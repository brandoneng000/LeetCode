from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n

        for x, y, weight in edges:
            self.graph[x].append((y, weight))
        

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))
    

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')] * self.n
        dist[node1] = 0
        heap = [(0, node1)]

        while heap:
            cur_cost, cur_node = heappop(heap)

            if cur_cost > dist[cur_node]:
                continue

            if cur_node == node2:
                return cur_cost
            
            for neighbor, weight in self.graph[cur_node]:
                new_cost = weight + dist[cur_node]

                if dist[neighbor] > new_cost:
                    dist[neighbor] = new_cost
                    heappush(heap, (new_cost, neighbor))
        
        return -1 if dist[node2] == float('inf') else dist[node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)