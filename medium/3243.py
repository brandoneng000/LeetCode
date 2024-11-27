from typing import List
from collections import deque, defaultdict

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(graph: dict):
            q = deque([0])
            visited = set()
            res = 0

            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    if node == n - 1:
                        return res
                    
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

                res += 1
            
            return res

        graph = defaultdict(list)
        res = []

        for i in range(n - 1):
            graph[i].append(i + 1)
        
        for u, v in queries:
            graph[u].append(v)
            res.append(bfs(graph))
        
        return res


def main():
    sol = Solution()
    print(sol.shortestDistanceAfterQueries(n = 5, queries = [[2,4],[0,2],[0,4]]))
    print(sol.shortestDistanceAfterQueries(n = 4, queries = [[0,3],[0,2]]))

if __name__ == '__main__':
    main()