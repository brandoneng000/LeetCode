from typing import List
from collections import defaultdict, deque

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dist = [-1] * n
        dist[0] = 0
        val = 0
        q = deque([0])

        while q:
            size = len(q)
            val += 2
            
            for _ in range(size):
                cur = q.popleft()

                for node in graph[cur]:
                    if dist[node] == -1:
                        dist[node] = val
                        q.append(node)
        
        res = 0
        for d, p in zip(dist, patience):
            if p: 
                k = d // p - int(d % p == 0)
                res = max(res, d + k * p)

        return res + 1

        
def main():
    sol = Solution()
    print(sol.networkBecomesIdle(edges = [[0,1],[1,2]], patience = [0,2,1]))
    print(sol.networkBecomesIdle(edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]))

if __name__ == '__main__':
    main()