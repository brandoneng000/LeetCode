from typing import List
from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        road_vals = [0] * n
        res = 0

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        for val, r in zip(range(1, n + 1)[::-1], sorted(graph, key=lambda x: len(graph[x]), reverse=True)):
            road_vals[r] = val
        
        for a in range(n):
            for b in graph[a]:
                if a < b:
                    res += road_vals[a] + road_vals[b]
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumImportance(n = 5, roads = [[0,1]]))
    print(sol.maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
    print(sol.maximumImportance(n = 5, roads = [[0,3],[2,4],[1,3]]))

if __name__ == '__main__':
    main()