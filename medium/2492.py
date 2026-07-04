from typing import List
from collections import defaultdict, deque

class Solution:
    # def minScore(self, n: int, roads: List[List[int]]) -> int:
    #     def dfs(node: int):
    #         res = INF

    #         for nei, dist in graph[node]:
    #             if (node, nei) in visited:
    #                 continue
                
    #             visited.add((node, nei))
    #             visited.add((nei, node))
    #             res = min(res, dist, dfs(nei))

    #         return res

    #     graph = defaultdict(list)
    #     INF = 10 ** 33
    #     self.res = INF
    #     visited = set()

    #     for a, b, dist in roads:
    #         graph[a].append((b, dist))
    #         graph[b].append((a, dist))

    #     return dfs(1)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        q = deque([1])
        res = float('inf')
        visited = set()

        for a, b, dist in roads:
            graph[a][b] = dist
            graph[b][a] = dist
        
        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                res = min(res, graph[node][neighbor])
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return res


def main():
    sol = Solution()
    print(sol.minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
    print(sol.minScore(n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]))

if __name__ == '__main__':
    main()