from typing import List
import collections

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find_root(node: int):
            if root[node] != node:
                root[node] = find_root(root[node])
            return root[node]

        n = len(edges)
        root = list(range(n + 1))

        for a, b in edges:
            root1 = find_root(a)
            root2 = find_root(b)

            if root1 == root2:
                return [a, b]
            
            root[root2] = root1
        


    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     graph = collections.defaultdict(set)

    #     def dfs(source, target):
    #         if source not in seen:
    #             seen.add(source)
    #             if source == target:
    #                 return True
    #             return any(dfs(next, target) for next in graph[source])
        
    #     for start, end in edges:
    #         seen = set()
    #         if start in graph and end in graph and dfs(start, end):
    #             return [start, end]
    #         graph[start].add(end)
    #         graph[end].add(start)

    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     self.graph = collections.defaultdict(list)

    #     for start, end in edges:
    #         self.graph[start].append(end)
    #         self.graph[end].append(start)
    #         if self.is_cycle():
    #             return [start, end]
    
    # def is_cycle(self) -> bool:
    #     visited = set()
    #     for i in self.graph:
    #         if i not in visited:
    #             if self.check_cycle(i, visited, -1):
    #                 return True
    #     return False

    # def check_cycle(self, node: int, visited: set, parent: int) -> bool:
    #     visited.add(node)

    #     for n in self.graph[node]:
    #         if n not in visited:
    #             if self.check_cycle(n, visited, node):
    #                 return True
    #         elif parent != n:
    #             return True
    #     return False



def main():
    sol = Solution()
    print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
    print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

if __name__ == '__main__':
    main()