from typing import List
from collections import defaultdict, deque

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        
        res = 0
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        q = deque(node for node, nei in graph.items() if len(nei) == 1)

        while q:
            cur_node = q.popleft()
            nei_node = next(iter(graph[cur_node])) if graph[cur_node] else -1

            if nei_node >= 0:
                graph[nei_node].remove(cur_node)

            if values[cur_node] % k == 0:
                res += 1
            else:
                values[nei_node] += values[cur_node]
            
            if nei_node >= 0 and len(graph[nei_node]) == 1:
                q.append(nei_node)
        
        return res


    # def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    #     def dfs(root: int, parent: int, values: List[int], tree: defaultdict):
    #         cur = values[root]

    #         for nei in tree[root]:
    #             if nei == parent:
    #                 continue

    #             cur += dfs(nei, root, values, tree)
            
    #         if cur % k == 0:
    #             self.res += 1
    #             return 0

    #         return cur
        
    #     tree = defaultdict(list)
    #     self.res = 0

    #     for u, v in edges:
    #         tree[u].append(v)
    #         tree[v].append(u)

    #     dfs(0, -1, values, tree)

    #     return self.res
        
        
def main():
    sol = Solution()
    print(sol.maxKDivisibleComponents(n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6))
    print(sol.maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3))

if __name__ == '__main__':
    main()