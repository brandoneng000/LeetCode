from typing import List
from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(node: int, parent: int):
            count = 1

            for next in graph[node]:
                if next == parent:
                    continue
                    
                count += dfs(next, node)
            
            if node != 0:
                self.res += (count + (seats - 1)) // seats
            
            return count

        graph = defaultdict(list)
        self.res = 0

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        dfs(0, -1)
        return self.res
        
def main():
    sol = Solution()
    print(sol.minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5))
    print(sol.minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2))
    print(sol.minimumFuelCost(roads = [], seats = 1))

if __name__ == '__main__':
    main()