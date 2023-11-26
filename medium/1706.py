from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [-1] * n

        for ball in range(n):
            col = ball
            for row in range(m + 1):
                if row == m:
                    res[ball] = col
                    break
                
                temp = grid[row][col]
                if col == 0 and grid[row][col] == -1:
                    break

                if col == n - 1 and grid[row][col] == 1:
                    break
                
                if grid[row][col] == 1:
                    if grid[row][col] != grid[row][col + 1]:
                        break
                        
                if grid[row][col] == -1:
                    if grid[row][col] != grid[row][col - 1]:
                        break

                col += grid[row][col]

        return res

        
def main():
    sol = Solution()
    print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    print(sol.findBall([[-1]]))
    print(sol.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))

if __name__ == '__main__':
    main()