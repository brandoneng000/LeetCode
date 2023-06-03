from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        heap = [(0, k)]
        visited = set()

        for source, target, weight in times:
            graph[source].append((weight, target))

        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)

            if len(visited) == n:
                return travel_time
            
            for time, dest in graph[node]:
                if dest not in visited:
                    heapq.heappush(heap, (travel_time + time, dest))
        
        return -1
        

                
        
def main():
    sol = Solution()
    print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
    print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
    print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))

if __name__ == '__main__':
    main()