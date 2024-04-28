from typing import List
from collections import defaultdict, deque

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(root: int, prev: int):
            for i in tree[root]:
                if i != prev:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        
        def dfs2(root: int, prev: int):
            for i in tree[root]:
                if i != prev:
                    res[i] = res[root] - count[i] + n - count[i]
                    dfs2(i, root)
        
        tree = defaultdict(list)
        res = [0] * n
        count = [1] * n

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        dfs(0, -1)
        dfs2(0, -1)
        return res

    # def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    #     graph = defaultdict(list)
    #     res = [0] * n

    #     for a, b in edges:
    #         graph[a].append(b)
    #         graph[b].append(a)

    #     for i in range(n):
    #         q = deque([i])
    #         visited = set([i])
    #         cur = 0

    #         while q:
    #             size = len(q)
    #             res[i] += size * cur

    #             for _ in range(size):
    #                 node = q.popleft()

    #                 for next in graph[node]:
    #                     if next not in visited:
    #                         visited.add(next)
    #                         q.append(next)
                
    #             cur += 1
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    print(sol.sumOfDistancesInTree(n = 1, edges = []))
    print(sol.sumOfDistancesInTree(n = 2, edges = [[1,0]]))

if __name__ == '__main__':
    main()