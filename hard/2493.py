from typing import List
from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def is_bipartite(root: int, graph: defaultdict, colors: List[int]):
            for nei in graph[root]:
                if colors[nei] == colors[root]:
                    return False
                
                if colors[nei] != -1:
                    continue

                colors[nei] = (colors[root] + 1) % 2

                if not is_bipartite(nei, graph, colors):
                    return False
            
            return True

        def get_longest_shortest_path(root: int, n: int, graph: defaultdict):
            q = deque([root])
            visited = [False] * n
            visited[root] = True
            dist = 0

            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    for nei in graph[node]:
                        if visited[nei]:
                            continue

                        visited[nei] = True
                        q.append(nei)
                dist += 1
            
            return dist

        def get_groups(root: int, distance: List[int], graph: defaultdict, visited: List[bool]):
            max_groups = distance[root]
            visited[root] = True

            for nei in graph[root]:
                if visited[nei]:
                    continue

                max_groups = max(max_groups, get_groups(nei, distance, graph, visited))
            
            return max_groups


        colors = [-1] * n
        graph = defaultdict(list)

        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        for node in range(n):
            if colors[node] != -1:
                continue

            colors[node] = 0

            if not is_bipartite(node, graph, colors):
                return -1
            
        distance = [get_longest_shortest_path(node, n, graph) for node in range(n)]
        res = 0
        visited = [False] * n
        
        for node in range(n):
            if visited[node]:
                continue

            res += get_groups(node, distance, graph, visited)
        
        return res


        
def main():
    sol = Solution()
    print(sol.magnificentSets(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
    print(sol.magnificentSets(n = 3, edges = [[1,2],[2,3],[3,1]]))

if __name__ == '__main__':
    main()