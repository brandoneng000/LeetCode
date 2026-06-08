from typing import List
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        def dfs(index: int):
            ch = s[index]

            if ch in ancestor:
                prev = ancestor[ch]
            else:
                prev = None
            
            ancestor[ch] = index

            for node in graph[index]:
                dfs(node)
                res[parent[node]] += res[node]

            ancestor[ch] = prev

            if prev is None:
                return
            
            parent[index] = prev

        n = len(parent)
        res = [1] * n
        graph = defaultdict(list)
        ancestor = defaultdict(int)

        for node, p in enumerate(parent):
            graph[p].append(node)
        
        dfs(0)

        return res


def main():
    sol = Solution()
    print(sol.findSubtreeSizes(parent = [-1,0,0,1,1,1], s = "abaabc"))
    print(sol.findSubtreeSizes(parent = [-1,0,4,0,1], s = "abbba"))

if __name__ == '__main__':
    main()