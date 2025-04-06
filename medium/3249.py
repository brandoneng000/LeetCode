from typing import List
from collections import defaultdict

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        def dfs(root: int, parent: int, tree: defaultdict):
            if len(tree[root]) == 1 and parent != -1:
                self.good_nodes += 1
                return 1
            
            children = []

            for child in tree[root]:
                if child != parent:
                    children.append(dfs(child, root, tree))

            if len(set(children)) == 1:
                self.good_nodes += 1

            return 1 + sum(children)
            

        tree = defaultdict(list)
        self.good_nodes = 0

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        dfs(0, -1, tree)

        return self.good_nodes

        
def main():
    sol = Solution()
    print(sol.countGoodNodes([[2,1],[0,1]]))
    print(sol.countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))
    print(sol.countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]))
    print(sol.countGoodNodes([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]))

if __name__ == '__main__':
    main()