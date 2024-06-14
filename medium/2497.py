from typing import List
from collections import defaultdict

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        graph = defaultdict(list)
        res = -float('inf')

        for a, b in edges:
            graph[a].append(vals[b])
            graph[b].append(vals[a])
        
        for node in graph:
            graph[node].sort(reverse=True)
        
        for node in range(n):
            cur = vals[node]
            res = max(res, cur)

            for nei in range(min(len(graph[node]), k)):
                cur += graph[node][nei]
                res = max(res, cur)
        
        return res


        
def main():
    sol = Solution()
    print(sol.maxStarSum(vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2))
    print(sol.maxStarSum(vals = [-5], edges = [], k = 0))

if __name__ == '__main__':
    main()