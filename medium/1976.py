from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 1000000007
        graph = defaultdict(list)
        
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        times = [float('inf') for _ in range(n)]
        ways = [0 for _ in range(n)]

        times[0] = 0
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            prev_time, node = heappop(heap)

            for next, time in graph[node]:
                new_time = time + prev_time

                if new_time < times[next]:
                    times[next] = new_time
                    ways[next] = ways[node]
                    heappush(heap, (new_time, next))
                elif new_time == times[next]:
                    ways[next] += ways[node]
        
        return ways[n - 1] % mod

        
def main():
    sol = Solution()
    print(sol.countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
    print(sol.countPaths(n = 2, roads = [[1,0,10]]))

if __name__ == '__main__':
    main()