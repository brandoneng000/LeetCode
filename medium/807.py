from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        north = [max(grid[j][i] for j in range(len(grid))) for i in range(len(grid))]
        west = [max(grid[i]) for i in range(len(grid))]
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                res += min(north[j], west[i]) - grid[i][j]

        return res

def main():
    sol = Solution()
    print(sol.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
    print(sol.maxIncreaseKeepingSkyline([[0,0,0],[0,0,0],[0,0,0]]))

if __name__ == '__main__':
    main()