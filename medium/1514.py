from typing import List
import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        heap = []
        for i, (x, y) in enumerate(edges):
            graph[x].append((y, succProb[i]))
            graph[y].append((x, succProb[i]))
        
        distance = [-float('inf')] * n
        distance[start] = 1
        heapq.heappush(heap, (0, start))
        
        while heap:
            weight, node = heapq.heappop(heap)
            weight = -weight

            for v, weight in graph[node]:
                if distance[v] < distance[node] * weight:
                    distance[v] = distance[node] * weight
                    heapq.heappush(heap, (-distance[v], v))

        return abs(distance[end]) if distance[end] != -float('inf') else 0

def main():
    sol = Solution()
    print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))
    print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
    print(sol.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))

if __name__ == '__main__':
    main()