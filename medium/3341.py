from typing import List
# from collections import deque
from heapq import heappush, heappop

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        goal = (m - 1, n - 1)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = 0
        heap = []
        heappush(heap, (0, 0, 0))

        while heap:
            time, row, col = heappop(heap)

            if (row, col) == goal:
                return time
            
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if 0 <= r < m and 0 <= c < n:
                    if visited[r][c] == -1:
                        visited[r][c] = max(visited[r][c], time + 1, moveTime[r][c] + 1)
                        heappush(heap, (visited[r][c], r, c))


def main():
    sol = Solution()
    print(sol.minTimeToReach([[0,4],[4,4]]))
    print(sol.minTimeToReach([[0,0,0],[0,0,0]]))
    print(sol.minTimeToReach([[0,1],[1,2]]))

if __name__ == '__main__':
    main()