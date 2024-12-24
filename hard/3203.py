from typing import List
from collections import defaultdict, deque
from math import ceil

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_tree(edges: List[List[int]]):
            tree = defaultdict(list)

            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            
            return tree
        
        def find_diameter(tree: defaultdict):
            farthest_node, _ = find_farthest(tree, 0)

            _, diameter = find_farthest(tree, farthest_node)

            return diameter

        def find_farthest(tree: defaultdict, root: int):
            q = deque([root])
            visited = set()
            visited.add(root)

            max_dist = 0
            farthest_node = root

            while q:

                for _ in range(len(q)):
                    node = q.popleft()
                    farthest_node = node

                    for nei in tree[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                
                if q:
                    max_dist += 1
            
            return farthest_node, max_dist

        tree1 = build_tree(edges1)
        tree2 = build_tree(edges2)

        diameter1 = find_diameter(tree1)
        diameter2 = find_diameter(tree2)

        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        return max(diameter1, diameter2, combined_diameter)

        
def main():
    sol = Solution()
    print(sol.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]))
    print(sol.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]))

if __name__ == '__main__':
    main()