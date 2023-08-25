from typing import List
import collections

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        res = { sum(d <= distanceThreshold for d in dist[i]): i for i in range(n) }
        
        return res[min(res)]

    # def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    #     def bfs(city: int, threshold: int):
    #         q = collections.deque([(city, threshold)])
    #         visited = [-1] * n
    #         visited[city] = float('inf')

    #         while q:
    #             size = len(q)

    #             for _ in range(size):
    #                 c, cur_w = q.popleft()

    #                 for nei, w in graph[c]:
    #                     if visited[nei] < cur_w - w:
    #                         visited[nei] = cur_w - w
    #                         q.append((nei, visited[nei]))

    #         return sum(v != -1 and v != float('inf') for v in visited)
        
    #     graph = collections.defaultdict(list)

    #     for a, b, w in edges:
    #         graph[a].append((b, w))
    #         graph[b].append((a, w))

    #     res = 0
    #     connections = float('inf')
    #     for i in range(n):
    #         cur = bfs(i, distanceThreshold)
    #         if cur <= connections:
    #             res = max(res, i)
    #             connections = cur
        
    #     return res

def main():
    sol = Solution()
    print(sol.findTheCity(n = 6, edges = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], distanceThreshold = 20))
    print(sol.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
    print(sol.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))

if __name__ == '__main__':
    main()