from typing import List
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        q = deque([1])
        res = float('inf')
        visited = set()

        for a, b, dist in roads:
            graph[a][b] = dist
            graph[b][a] = dist
        
        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                res = min(res, graph[node][neighbor])
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return res


def main():
    sol = Solution()
    print(sol.minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
    print(sol.minScore(n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]))

if __name__ == '__main__':
    main()