from typing import List
from collections import defaultdict, deque

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        size = []
        res = 0

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(n):
            if i in visited:
                continue
            
            count = 1
            q = deque([i])
            visited.add(i)

            while q:
                node = q.popleft()

                for next in graph[node]:
                    if next not in visited:
                        visited.add(next)
                        q.append(next)
                        count += 1
            size.append(count)
        
        m = n
        for i in range(len(size) - 1):
            m -= size[i]
            res += size[i] * m

        return res


        
def main():
    sol = Solution()
    print(sol.countPairs(n = 3, edges = [[0,1],[0,2],[1,2]]))
    print(sol.countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]))

if __name__ == '__main__':
    main()