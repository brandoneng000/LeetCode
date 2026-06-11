from typing import List
from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def dfs(root: int, parent: set):
            res = 0

            for node in tree[root]:
                if parent == node:
                    continue
                res = max(res, dfs(node, root) + 1)

            return res


        mod = 1_000_000_007
        tree = defaultdict(list)

        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)

        max_depth = dfs(1, 0)
        
        return pow(2, max_depth - 1, mod)
        
def main():
    sol = Solution()
    print(sol.assignEdgeWeights([[1,2]]))
    print(sol.assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]]))

if __name__ == '__main__':
    main()