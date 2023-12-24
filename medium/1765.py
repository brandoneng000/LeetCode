from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        res = [[-1 for j in range(n)] for i in range(m)]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        q = deque([])

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    res[i][j] = 0
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and res[r][c] == -1:
                    res[r][c] = res[row][col] + 1
                    q.append((r, c))
        
        return res

        
def main():
    sol = Solution()
    print(sol.highestPeak([[0,1],[0,0]]))
    print(sol.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))

if __name__ == '__main__':
    main()