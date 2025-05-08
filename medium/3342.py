from typing import List
from heapq import heappush, heappop

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        goal = (m - 1, n - 1)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = 0
        heap = []
        heappush(heap, (0, 0, 0))

        while heap:
            time, row, col = heappop(heap)

            if visited[row][col]:
                continue

            if (row, col) == goal:
                break
            
            visited[row][col] = True

            for dr, dc in directions:
                r = row + dr
                c = col + dc
                
                if 0 <= r < m and 0 <= c < n:
                    dist = max(distance[row][col], moveTime[r][c]) + (row + col) % 2 + 1

                    if distance[r][c] > dist:
                        distance[r][c] = dist
                        heappush(heap, (dist, r, c))
        
        return distance[m - 1][n - 1]
        
def main():
    sol = Solution()
    print(sol.minTimeToReach([[0,4],[4,4]]))
    print(sol.minTimeToReach([[0,0,0,0],[0,0,0,0]]))
    print(sol.minTimeToReach([[0,1],[1,2]]))

if __name__ == '__main__':
    main()