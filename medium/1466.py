from typing import List
import collections
import heapq

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        q = collections.deque([0])
        visited = set([0])
        res = 0

        for a, b in connections:
            outdegree[a].add(b)
            indegree[b].add(a)
        
        while q:
            node = q.popleft()

            for adj in indegree[node]:
                if adj not in visited:
                    q.append(adj)
                    visited.add(adj)
            
            for adj in outdegree[node]:
                if adj not in visited:
                    res += 1
                    q.append(adj)
                    visited.add(adj)
        
        return res
            
            
        
        
def main():
    sol = Solution()
    print(sol.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
    print(sol.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
    print(sol.minReorder(n = 3, connections = [[1,0],[2,0]]))

if __name__ == '__main__':
    main()