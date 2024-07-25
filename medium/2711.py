from typing import List
from collections import Counter

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        def helper(row: int, col: int):
            above = Counter()
            below = Counter()
            r, c = row, col

            while r < m and c < n:
                below[grid[r][c]] += 1
                r += 1
                c += 1
            
            r, c = row, col

            while r < m and c < n:
                below[grid[r][c]] -= 1
                if below[grid[r][c]] == 0:
                    below.pop(grid[r][c])

                res[r][c] = abs(len(above) - len(below))
                above[grid[r][c]] += 1
                r += 1
                c += 1

        m, n = len(grid), len(grid[0])
        res = [[-1 for j in range(n)] for i in range(m)]

        for j in range(n):
            helper(0, j)
            
        for i in range(1, m):
            helper(i, 0)
            
        return res
        
def main():
    sol = Solution()
    print(sol.differenceOfDistinctValues([[1,2,3],[3,1,5],[3,2,1]]))
    print(sol.differenceOfDistinctValues([[1]]))

if __name__ == '__main__':
    main()