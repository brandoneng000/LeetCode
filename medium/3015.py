from typing import List
from collections import deque, defaultdict

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:        
        def bfs(root: int):
            q = deque([(root, 0)])
            visited = set([root])

            while q:
                node, dist = q.popleft()

                if dist > 0:
                    res[dist - 1] += 1
                
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist + 1))


        res = [0] * n
        graph = defaultdict(list)

        for i in range(1, n):
            graph[i].append(i + 1)
            graph[i + 1].append(i)

        graph[x].append(y)
        graph[y].append(x)

        for i in range(1, n + 1):
            bfs(i)

        return res
        
def main():
    sol = Solution()
    print(sol.countOfPairs(n = 3, x = 1, y = 3))
    print(sol.countOfPairs(n = 5, x = 2, y = 4))
    print(sol.countOfPairs(n = 4, x = 1, y = 1))

if __name__ == '__main__':
    main()