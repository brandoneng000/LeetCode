from typing import List
from collections import defaultdict, deque
from heapq import heappop, heapify

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def join(self, u, v):
        self.parent[self.find(v)] = self.find(u)

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c + 1)
        online = [True] * (c + 1)
        offline = [0] * (c + 1)
        min_online_stations = {}
        res = []

        for x, y in connections:
            dsu.join(x, y)

        for op, x in queries:
            if op == 2:
                online[x] = False
                offline[x] += 1
            
        for i in range(1, c + 1):
            root = dsu.find(i)

            if root not in min_online_stations:
                min_online_stations[root] = -1

            station = min_online_stations[root]

            if online[i]:
                if station == -1 or station > i:
                    min_online_stations[root] = i
        
        for i in range(len(queries) - 1, -1, -1):
            op, x = queries[i]
            root = dsu.find(x)
            station = min_online_stations[root]

            if op == 1:
                if online[x]:
                    res.append(x)
                else:
                    res.append(station)
            
            if op == 2:
                if offline[x] > 1:
                    offline[x] -= 1
                else:
                    online[x] = True

                    if station == -1 or station > x:
                        min_online_stations[root] = x
            
        return res[::-1]


    # def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
    #     def bfs(station: int):
    #         all_stations = set()
    #         q = deque([station])

    #         while q:
    #             station = q.popleft()

    #             for p in grid[station]:
    #                 if p in visited:
    #                     continue

    #                 visited.add(p)
    #                 q.append(p)
    #                 all_stations.add(p)
            
    #         all_stations = list(all_stations)
    #         for p in all_stations:
    #             grid[p] = all_stations


    #     powerstations = [True] * (c + 1)
    #     grid = defaultdict(list)
    #     visited = set()
    #     res = []

    #     for x, y in connections:
    #         grid[x].append(y)
    #         grid[y].append(x)
        
    #     for station in grid:
    #         if station in visited:
    #             continue

    #         bfs(station)

    #     for powerstation in grid:
    #         heapify(grid[powerstation])
        
    #     for operation, station in queries:
    #         if operation == 1:
    #             if powerstations[station]:
    #                 res.append(station)
    #             else:
    #                 while grid[station] and not powerstations[grid[station][0]]:
    #                     heappop(grid[station])
                    
    #                 if grid[station]:
    #                     res.append(grid[station][0])
    #                 else:
    #                     res.append(-1)

    #         else:
    #             powerstations[station] = False
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.processQueries(c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]))
    print(sol.processQueries(c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]))

if __name__ == '__main__':
    main()