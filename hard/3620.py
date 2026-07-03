from typing import List
from heapq import heappop, heappush

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        def check(mid: int) -> bool:
            dis = [INF] * n
            pq = [(0, 0)]
            dis[0] = 0

            while pq:
                d, u = heappop(pq)

                if d > k:
                    return False
                if u == n - 1:
                    return True
                if d > dis[u]:
                    continue

                for v, w in graph[u]:
                    if w < mid:
                        continue
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heappush(pq, (dis[v], v))
            
            return False

        n = len(online)
        INF = 10 ** 33
        graph = [[] for _ in range(n)]
        l, r = INF, 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            graph[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        if not check(l):
            return -1
        
        while l <= r:
            middle = (l + r) // 2

            if check(middle):
                l = middle + 1
            else:
                r = middle - 1
        
        return r

        
def main():
    sol = Solution()
    print(sol.findMaxPathScore(edges = [[0,1,0],[0,2,7],[1,3,9],[0,4,7],[2,4,9],[3,4,2],[0,3,5],[2,3,3],[1,4,6],[1,2,0]], online = [True,True,True,True,True], k = 5))
    print(sol.findMaxPathScore(edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [True,True,True,True], k = 10))
    print(sol.findMaxPathScore(edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [True,True,True,False,True], k = 12))

if __name__ == '__main__':
    main()