from typing import List
import collections

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)

        for node in range(len(graph)):
            if colors[node] != 0:
                continue

            q = collections.deque([node])
            colors[node] = 1

            while q:
                cur = q.popleft()

                for n in graph[cur]:
                    if colors[n] == 0:
                        colors[n] = -colors[cur]
                        q.append(n)
                    elif colors[n] != -colors[cur]:
                        return False
        return True


def main():
    sol = Solution()
    print(sol.isBipartite([[1],[0,3],[3],[1,2]]))
    print(sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    print(sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]))

if __name__ == '__main__':
    main()