from typing import List

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0]

        for i in range(m - 1):
            dp_next = [float('inf')] * n
            
            for j in range(n):
                for k in range(n):
                    dp_next[k] = min(dp_next[k], dp[j] + moveCost[grid[i][j]][k] + grid[i + 1][k])
            
            dp = dp_next
        
        return min(dp)
        
def main():
    sol = Solution()
    print(sol.minPathCost(grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]))
    print(sol.minPathCost(grid = [[5,1,2],[4,0,3]], moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]))

if __name__ == '__main__':
    main()