from typing import List
from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        def bfs(graph: defaultdict, root: int):
            q = deque([root])
            visited = set([root])

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            
            return visited

        graph = defaultdict(list)

        for x, y in invocations:
            graph[x].append(y)

        suspicious = bfs(graph, k)
        res = []

        for node in range(n):
            if node in suspicious:
                continue

            for nei in graph[node]:
                if nei in suspicious:
                    return list(range(n))
            res.append(node)
        
        return res

        
def main():
    sol = Solution()
    print(sol.remainingMethods(n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]))
    print(sol.remainingMethods(n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]))
    print(sol.remainingMethods(n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]))

if __name__ == '__main__':
    main()