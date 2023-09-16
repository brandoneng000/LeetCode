from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        goal = (m - 1, n - 1)
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            weight, cur_r, cur_c = heapq.heappop(heap)

            if weight > dist[cur_r][cur_c]:
                continue

            if (cur_r, cur_c) == goal:
                return weight

            for dr, dc in directions:
                r, c = cur_r + dr, cur_c + dc

                if 0 <= r < m and 0 <= c < n:
                    new_dist = max(weight, abs(heights[cur_r][cur_c] - heights[r][c]))
                    if dist[r][c] > new_dist:
                        dist[r][c] = new_dist
                        heapq.heappush(heap, (dist[r][c], r, c))



def main():
    sol = Solution()
    print(sol.minimumEffortPath([[1,10,6,7,9,10,4,9]]))
    print(sol.minimumEffortPath([[3]]))
    print(sol.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
    print(sol.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))

if __name__ == '__main__':
    main()