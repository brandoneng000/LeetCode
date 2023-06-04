from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = { tuple(mine) for mine in mines }
        grid = [[0 for i in range(n)] for j in range(n)]
        res = 0

        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count + 1
                grid[r][c] = count
            
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                grid[r][c] = min(grid[r][c], count)
        
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count + 1
                grid[r][c] = min(grid[r][c], count)
            
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                grid[r][c] = min(grid[r][c], count)
                res = max(res, grid[r][c])
        return res

def main():
    sol = Solution()
    print(sol.orderOfLargestPlusSign(n = 5, mines = [[4,2]]))
    print(sol.orderOfLargestPlusSign(n = 1, mines = [[0,0]]))

if __name__ == '__main__':
    main()