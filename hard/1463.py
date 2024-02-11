from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = {}

        def dfs(row: int, c1: int, c2: int):
            if (row, c1, c2) in cache:
                return cache[(row, c1, c2)]
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == n:
                return 0
            if row == m - 1:
                return grid[row][c1] + grid[row][c2]
            
            res = 0

            for c1_d in [-1, 0, 1]:
                for c2_d in [-1, 0, 1]:
                    res = max(res, dfs(row + 1, c1 + c1_d, c2 + c2_d))
            
            cache[(row, c1, c2)] = res + grid[row][c1] + grid[row][c2]
            return cache[(row, c1, c2)]
        
        return dfs(0, 0, n - 1)
            


        
def main():
    sol = Solution()
    print(sol.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
    print(sol.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))

if __name__ == '__main__':
    main()