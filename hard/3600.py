from typing import List
from heapq import heappush, heappop

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return False
            
            components[0] -= 1

            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
            
            return True
        
        INF = 10 ** 33
        parent = list(range(n))
        size = [1] * n
        components = [n]

        must = []
        flex = []

        for e in edges:
            if e[3] == 1:
                must.append(e)
            else:
                flex.append(e)
        
        mini = INF

        for u, v, w, t in must:
            mini = min(mini, w)

            if not union(u, v):
                return -1
            
        flex.sort(key=lambda x: -x[2])
        heap = []

        for u, v, w, t in flex:
            if union(u, v):
                heappush(heap, w)
        
        while k > 0 and heap:
            x = heappop(heap)
            mini = min(mini, 2 * x)
            k -= 1
        
        if components[0] != 1:
            return -1
        
        if heap:
            return min(mini, heap[0])

        return mini
        

def main():
    sol = Solution()
    print(sol.maxStability(n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1))
    print(sol.maxStability(n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2))
    print(sol.maxStability(n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0))

if __name__ == '__main__':
    main()