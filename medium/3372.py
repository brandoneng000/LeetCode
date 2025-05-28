from typing import List
from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def traverse_tree_steps(root: int, tree: defaultdict, steps: int):
            q = deque([root])
            visited = set([root])
            res = 0

            for _ in range(steps + 1):
                size = len(q)
                res += size

                for i in range(size):
                    node = q.popleft()
                    for nei in tree[node]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                
            return res


        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        tree2_nodes = []
        tree1_nodes = []

        for a, b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)
        
        for a, b in edges2:
            tree2[a].append(b)
            tree2[b].append(a)

        n, m = len(tree1), len(tree2)

        for i in range(m):
            tree2_nodes.append(traverse_tree_steps(i, tree2, k - 1))
        
        for i in range(n):
            tree1_nodes.append(traverse_tree_steps(i, tree1, k))
        
        tree2_max = max(tree2_nodes)

        return [t1 + tree2_max for t1 in tree1_nodes]
        
        
def main():
    sol = Solution()
    print(sol.maxTargetNodes(edges1 = [[0,1]], edges2 = [[0,1]], k = 0))
    print(sol.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2))
    print(sol.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1))

if __name__ == '__main__':
    main()