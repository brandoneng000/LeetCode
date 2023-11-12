from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)

        for i, route in enumerate(routes):
            for j in route:
                graph[j].add(i)

        q = deque([source])
        visited = set([source])
        bus = 0

        while q:
            size = len(q)

            for _ in range(size):
                cur_bus = q.popleft()

                if cur_bus == target:
                    return bus

                for i in graph[cur_bus]:
                    for j in routes[i]:
                        if j not in visited:
                            q.append(j)
                            visited.add(j)

                    routes[i] = []

            bus += 1
                
        return -1
        
def main():
    sol = Solution()
    print(sol.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
    print(sol.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12))

if __name__ == '__main__':
    main()