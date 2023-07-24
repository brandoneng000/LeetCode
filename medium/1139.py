from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        top, left = [row[:] for row in grid], [row[:] for row in grid]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i:
                        top[i][j] = top[i - 1][j] + 1
                    if j:
                        left[i][j] = left[i][j - 1] + 1
        
        for r in range(min(m, n), 0, -1):
            for i in range(m - r + 1):
                for j in range(n - r + 1):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1], 
                           left[i][j + r - 1], left[i + r - 1][j + r - 1]) >= r:
                        return r * r
        
        return 0

def main():
    sol = Solution()
    print(sol.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))
    print(sol.largest1BorderedSquare([[1,1,0,0]]))

if __name__ == '__main__':
    main()