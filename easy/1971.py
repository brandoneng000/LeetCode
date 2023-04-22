from typing import List
import collections

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            visited.add(node)
            
            for edge in graph[node]:
                if edge not in visited:
                    stack.append(edge)
        
        return False


def main():
    sol = Solution()
    print(sol.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
    print(sol.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))

if __name__ == '__main__':
    main()