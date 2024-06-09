from typing import List
from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs(i, d0):
            visited.add(i)
            res = -float('inf')

            db = 0 if i == bob else n

            for child in graph[i]:
                if child in visited:
                    continue
                cur, kk = dfs(child, d0 + 1)
                res = max(res, cur)
                db = min(db, kk)

            if res == -float('inf'):
                res = 0
            if d0 == db:
                res += amount[i] // 2
            if d0 < db: 
                res += amount[i]
            
            return res, db + 1

        n = len(edges) + 1
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        return dfs(0, 0)[0]

        
def main():
    sol = Solution()
    # print(sol.mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]))
    print(sol.mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350]))

if __name__ == '__main__':
    main()