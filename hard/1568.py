from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands():
            visited = set()
            islands = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        islands += 1
                        visited.add((i, j))
                        visit(i, j, visited)
            
            return islands

        def visit(row: int, col: int, visited: set):
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    visit(r, c, visited)

        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        if count_islands() != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2
        
        
def main():
    sol = Solution()
    print(sol.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
    print(sol.minDays([[1,1]]))

if __name__ == '__main__':
    main()