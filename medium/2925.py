from typing import List
from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        def dfs(node: int, parent: int):
            if len(tree[node]) == 1 and node != 0:
                return values[node]
            
            res = 0

            for child in tree[node]:
                if child == parent:
                    continue

                res += dfs(child, node)
            
            return min(res, values[node])

        tree = defaultdict(list)
        res = sum(values)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        min_sum = dfs(0, -1)

        return res - min_sum
        
def main():
    sol = Solution()
    print(sol.maximumScoreAfterOperations(edges = [[0,1],[0,2],[0,3],[2,4],[4,5]], values = [5,2,5,2,1,1]))
    print(sol.maximumScoreAfterOperations(edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [20,10,9,7,4,3,5]))

if __name__ == '__main__':
    main()