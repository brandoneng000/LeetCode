from typing import List
from heapq import heappush, heappop

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        INF = 10 ** 33
        g = [[] for _ in range(n)]

        for u, v, w in edges:
            g[u].append((v, w))

        dis = [[INF] * (k + 1) for _ in range(n)]
        heap = []

        dis[0][1] = 0
        heappush(heap, (0, 0, 1))

        while heap:
            d, x, cnt = heappop(heap)

            if d > dis[x][cnt]:
                continue

            if x == n - 1:
                return d

            for y, w in g[x]:
                new_cnt = cnt + 1 if labels[x] == labels[y] else 1

                if new_cnt > k:
                    continue

                nd = d + w

                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt] = nd
                    heappush(heap, (nd, y, new_cnt))

        return -1

def main():
    sol = Solution()
    print(sol.shortestPath(n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1))
    print(sol.shortestPath(n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2))
    print(sol.shortestPath(n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2))

if __name__ == '__main__':
    main()