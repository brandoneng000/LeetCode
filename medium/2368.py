from typing import List
from collections import deque, defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = 0
        q = deque([0])
        graph = defaultdict(list)
        visited = set([0])
        restrict = set(restricted)

        for a, b in edges:
            if a not in restrict and b not in restrict:
                graph[a].append(b)
                graph[b].append(a)
        
        while q:
            node = q.popleft()
            res += 1

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.append(child)
        
        return res
        
def main():
    sol = Solution()
    print(sol.reachableNodes(n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]))
    print(sol.reachableNodes(n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]))

if __name__ == '__main__':
    main()