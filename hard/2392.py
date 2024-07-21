from typing import List
from collections import defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src: int, adj: defaultdict, visited: set, path: set, order: List[int]):
            if src in path:
                return False
            
            if src in visited:
                return True
            
            visited.add(src)
            path.add(src)

            for nei in adj[src]:
                if not dfs(nei, adj, visited, path, order):
                    return False
                
            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges: List[List[int]]):
            adj = defaultdict(list)

            for u, v in edges:
                adj[u].append(v)
            
            visited = set()
            path = set()
            order = []

            for src in range(1, k + 1):
                if not dfs(src, adj, visited, path, order):
                    return []
            
            return order[::-1]
                

        res = [[0 for j in range(k)] for i in range(k)]
        rows = topo_sort(rowConditions)
        cols = topo_sort(colConditions)

        if not rows or not cols:
            return []
        
        rows_map = { num: i for i, num in enumerate(rows) }
        cols_map = { num: i for i, num in enumerate(cols) }

        for num in range(1, k + 1):
            r, c = rows_map[num], cols_map[num]
            res[r][c] = num

        return res
        

def main():
    sol = Solution()
    print(sol.buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]))
    print(sol.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]))

if __name__ == '__main__':
    main()