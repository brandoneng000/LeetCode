from typing import List
from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def bfs(source: int, graph: defaultdict, visited: set):
            q = deque([source])
            visited[source] = True
            nodes = []

            while q:
                node = q.popleft()
                nodes.append(node)
                
                for nei in graph[node]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
            
            size = len(nodes) - 1

            return all(len(graph[node]) == size for node in nodes)


        graph = defaultdict(list)
        visited = [False] * n
        res = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            if not visited[node]:
                if bfs(node, graph, visited):
                    res += 1
        
        return res

    # def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    #     def dfs(node: int, seen: set):
    #         if node in seen:
    #             return 0
            
    #         res = 1
    #         seen.add(node)

    #         for nei in graph[node]:
    #             res += dfs(nei, seen)
            
    #         return res


    #     def check(start: int):
    #         size = dfs(start, set()) - 1
    #         visited.add(start)
    #         res = True

    #         for nei in graph[start] + [start]:
    #             visited.add(nei)
    #             res = res and len(graph[nei]) == size
            
    #         return res

    #     visited = set()
    #     graph = defaultdict(list)
    #     res = 0

    #     for u, v in edges:
    #         graph[u].append(v)
    #         graph[v].append(u)
        
    #     for i in range(n):
    #         if i in visited:
    #             continue

    #         res += check(i)
        
    #     return res
        

def main():
    sol = Solution()
    print(sol.countCompleteComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]]))
    print(sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
    print(sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))

if __name__ == '__main__':
    main()