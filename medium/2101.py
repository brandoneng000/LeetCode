from typing import List
from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def connected(first: List[int], second: List[int]):
            x1, y1, r1 = first
            x2, y2, r2 = second
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            return dist <= r1 * r1
        
        def dfs(node: int, visited: set):
            if node in visited:
                return 0
            
            visited.add(node)
            res = 1

            if node in graph:
                for child in graph[node]:
                    if child in visited:
                        continue
                    res += dfs(child, visited)

            return res

        n = len(bombs)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i != j:
                    if connected(bombs[i], bombs[j]):
                        graph[i].append(j)
        
        res = 1
        for b in graph:
            res = max(res, dfs(b, set()))
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumDetonation(bombs = [[2,1,3],[6,1,4]]))
    print(sol.maximumDetonation(bombs = [[1,1,5],[10,10,5]]))
    print(sol.maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))

if __name__ == '__main__':
    main()