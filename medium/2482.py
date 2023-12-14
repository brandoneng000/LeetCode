from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        ones_row = []
        ones_col = []

        for row in grid:
            ones_row.append(sum(row))
        
        for i in range(n):
            total = 0
            for j in range(m):
                total += grid[j][i]
            ones_col.append(total)
        
        for r in ones_row:
            cur = []
            for c in ones_col:
                cur.append(r + c - (n - r) - (m - c))
            res.append(cur)
        
        return res

        
def main():
    sol = Solution()
    print(sol.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))
    print(sol.onesMinusZeros([[1,1,1],[1,1,1]]))

if __name__ == '__main__':
    main()