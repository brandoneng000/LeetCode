from typing import List
from collections import Counter

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = n // 2
        letter_y = set([(0, 0)])
        count_y = Counter()
        count_grid = Counter()
        r = 0
        total = n * n

        for i in range(3):
            count_y[i] = 0
            count_grid[i] = 0

        while r < center:
            r += 1
            letter_y.add((r, r))
        
        c = r
        while r > 0:
            r -= 1
            c += 1
            letter_y.add((r, c))
        
        r = c = center

        while r < n:
            letter_y.add((r, c))
            r += 1
        
        for i in range(n):
            for j in range(n):
                if (i, j) in letter_y:
                    count_y[grid[i][j]] += 1
                else:
                    count_grid[grid[i][j]] += 1

        return min(total - count_grid[i] - count_y[j] for i in range(3) for j in range(3) if i != j)

        
def main():
    sol = Solution()
    print(sol.minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]]))
    print(sol.minimumOperationsToWriteY([[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]))

if __name__ == '__main__':
    main()