from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def get_component_cost(src: int, graph: defaultdict, visited: List[bool], components: List[int], component_id: int):
            q = deque()
            component_cost = -1

            q.append(src)
            visited[src] = True

            while q:
                node = q.popleft()

                components[node] = component_id

                for nei, weight in graph[node]:
                    component_cost &= weight

                    if visited[nei]:
                        continue

                    visited[nei] = True
                    q.append(nei)
            
            return component_cost


        graph = defaultdict(list)
        visited = [False] * n
        res = []

        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        components = [0] * n
        component_cost = []
        
        component_id = 0

        for node in range(n):
            if not visited[node]:
                component_cost.append(get_component_cost(node, graph, visited, components, component_id))
                component_id += 1

        for start, end in query:
            if components[start] == components[end]:
                res.append(component_cost[components[start]])
            else:
                res.append(-1)
        
        return res
        

        
def main():
    sol = Solution()
    print(sol.minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))
    print(sol.minimumCost(n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]))

if __name__ == '__main__':
    main()