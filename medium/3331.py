from typing import List
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        def dfs1(u: int):
            c = ord(s[u]) - ord('a')

            prev = char_ancestor[c]

            if prev != -1:
                new_parent[u] = prev
            char_ancestor[c] = u

            for v in adj[u]:
                dfs1(v)

            char_ancestor[c] = prev

        def dfs2(u: int):
            sz = 1

            for v in new_adj[u]:
                sz += dfs2(v)
            res[u] = sz
            
            return sz

        n = len(parent)
        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = list(parent)
        char_ancestor = [-1] * 26

        dfs1(0)

        new_adj = [[] for _ in range(n)]

        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        res = [0] * n
        dfs2(0)

        return res

    # def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    #     def dfs(index: int):
    #         ch = s[index]

    #         if ch in ancestor:
    #             prev = ancestor[ch]
    #         else:
    #             prev = None
            
    #         ancestor[ch] = index

    #         for node in graph[index]:
    #             dfs(node)
    #             res[parent[node]] += res[node]

    #         ancestor[ch] = prev

    #         if prev is None:
    #             return
            
    #         parent[index] = prev

    #     n = len(parent)
    #     res = [1] * n
    #     graph = defaultdict(list)
    #     ancestor = defaultdict(int)

    #     for node, p in enumerate(parent):
    #         graph[p].append(node)
        
    #     dfs(0)

    #     return res


def main():
    sol = Solution()
    print(sol.findSubtreeSizes(parent = [-1,0,0,1,1,1], s = "abaabc"))
    print(sol.findSubtreeSizes(parent = [-1,0,4,0,1], s = "abbba"))

if __name__ == '__main__':
    main()