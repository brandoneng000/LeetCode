from typing import List
from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = { i: [] for i in range(n) }
        res = [[] for _ in range(n)]

        for x, y in edges:
            graph[y].append(x)
                
        for i in range(n):
            q = deque(graph[i])
            cur = set()

            while q:
                node = q.popleft()

                cur.add(node)

                for next_node in graph[node]:
                    if next_node not in cur:
                        q.append(next_node)

            res[i] = sorted(cur)
        
        return res


def main():
    sol = Solution()
    print(sol.getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    print(sol.getAncestors(n = 5, edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))

if __name__ == '__main__':
    main()