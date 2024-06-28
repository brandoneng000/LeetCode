from typing import List

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        def dfs(row: int, col: int):
            if (row, col) == (m - 1, n - 1):
                return True

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if 0 <= r < m and 0 <= c < n and (r, c) not in visited and grid[r][c] == 1:
                    visited.add((r, c))
                    path.add((r, c))
                    if dfs(r, c):
                        return True
                    path.remove((r, c))
                    
            return False

        m, n = len(grid), len(grid[0])
        visited = set([(0, 0)])
        path = set([(0, 0)])
        directions = ((1, 0), (0, 1))

        if not dfs(0, 0):
            return True
        
        path.discard((0, 0))
        path.discard((m - 1, n - 1))

        for r, c in path:
            grid[r][c] = 0

        visited = set([(0, 0)])
        temp = dfs(0, 0)
        return not temp


def main():
    sol = Solution()
    print(sol.isPossibleToCutPath([[1,1,1],[1,0,0],[1,1,1]]))
    print(sol.isPossibleToCutPath([[1,1,1],[1,0,1],[1,1,1]]))

if __name__ == '__main__':
    main()