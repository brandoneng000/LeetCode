from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = float('inf')
        top = sum(grid[0])
        bottom = 0

        for i in range(n):
            top -= grid[0][i]
            res = min(res, max(top, bottom))
            bottom += grid[1][i]
        
        return res
        
def main():
    sol = Solution()
    print(sol.gridGame([[2,5,4],[1,5,1]]))
    print(sol.gridGame([[3,3,1],[8,5,2]]))
    print(sol.gridGame([[1,3,1,15],[1,3,3,1]]))

if __name__ == '__main__':
    main()