from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    return False
                if i + 1 < m and grid[i][j] != grid[i + 1][j]:
                    return False

        return True
        
def main():
    sol = Solution()
    print(sol.satisfiesConditions([[1,0,2],[1,0,2]]))
    print(sol.satisfiesConditions([[1,1,1],[0,0,0]]))
    print(sol.satisfiesConditions([[1],[2],[3]]))

if __name__ == '__main__':
    main()