from typing import List
from collections import defaultdict, deque

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        q = deque([1])
        visit_times = defaultdict(list)
        cur_time = 0
        res = -1

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == n:
                    if res != -1:
                        return cur_time
                    res = cur_time
                
                for nei in graph[node]:
                    nei_times = visit_times[nei]
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        nei_times.append(cur_time)
                                
            if (cur_time // change) % 2 == 1:
                cur_time += change - (cur_time % change)

            cur_time += time

        
def main():
    sol = Solution()
    print(sol.secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))
    print(sol.secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2))

if __name__ == '__main__':
    main()