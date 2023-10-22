from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(row: int, col: int, length: int, value: str, parent_r: int, parent_c: int):
            if (row, col) in visited and length >= 4:
                return True
            
            visited.add((row, col))
            for dx, dy in directions:
                r = row + dx
                c = col + dy

                if 0 <= r < m and 0 <= c < n and (r, c) != (parent_r, parent_c) and grid[r][c] == value:
                    if dfs(r, c, length + 1, value, row, col):
                        return True

            return False
        
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visited = set()

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and dfs(i, j, 1, grid[i][j], -1, -1):
                    return True
        
        return False

        
def main():
    sol = Solution()
    print(sol.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
    print(sol.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
    print(sol.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]))

if __name__ == '__main__':
    main()