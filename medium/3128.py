from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [sum(grid[i]) for i in range(m)]
        cols = [0] * n
        res = 0
        
        for i in range(m):
            for j in range(n):
                cols[j] += grid[i][j]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += (rows[i] - 1) * (cols[j] - 1)
        
        return res
        
        

def main():
    sol = Solution()
    print(sol.numberOfRightTriangles(grid = [[0,1,0],[0,1,1],[0,1,0]]))
    print(sol.numberOfRightTriangles(grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]))
    print(sol.numberOfRightTriangles([[1,0,1],[1,0,0],[1,0,0]]))

if __name__ == '__main__':
    main()