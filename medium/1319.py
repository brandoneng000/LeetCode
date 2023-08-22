from typing import List
import collections

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def traverse(node: int):
            for i in network[node]:
                if i not in visited:
                    visited.add(i)
                    traverse(i)
        
        if n - 1 > len(connections):
            return -1
        
        network = collections.defaultdict(list)
        visited = set()
        res = 0

        for a, b in connections:
            network[a].append(b)
            network[b].append(a)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                traverse(i)
                res += 1

        return res - 1

def main():
    sol = Solution()
    print(sol.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))
    print(sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
    print(sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]))

if __name__ == '__main__':
    main()