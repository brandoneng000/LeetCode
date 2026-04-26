from typing import List
from collections import deque

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        q = deque([])
        

        for x in range(n):
            for y in range(m):
                if (x, y) in visited:
                    continue
                
                val = grid[x][y]
                visited.add((x, y))
                q.append((x, y, -1, -1))

                while q:
                    row, col, pr, pc = q.popleft()

                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc

                        if not (0 <= r < n and 0 <= c < m):
                            continue

                        if grid[r][c] != grid[x][y]:
                            continue

                        if r == pr and c == pc:
                            continue

                        if (r, c) in visited:
                            return True
                        
                        visited.add((r, c))
                        q.append((r, c, row, col))

        
        return False


    # def containsCycle(self, grid: List[List[str]]) -> bool:
    #     def dfs(row: int, col: int, length: int, value: str, parent_r: int, parent_c: int):
    #         if (row, col) in visited and length >= 4:
    #             return True
            
    #         visited.add((row, col))
    #         for dx, dy in directions:
    #             r = row + dx
    #             c = col + dy

    #             if 0 <= r < m and 0 <= c < n and (r, c) != (parent_r, parent_c) and grid[r][c] == value:
    #                 if dfs(r, c, length + 1, value, row, col):
    #                     return True

    #         return False
        
    #     m, n = len(grid), len(grid[0])
    #     directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    #     visited = set()

    #     for i in range(m):
    #         for j in range(n):
    #             if (i, j) not in visited and dfs(i, j, 1, grid[i][j], -1, -1):
    #                 return True
        
    #     return False

        
def main():
    sol = Solution()
    print(sol.containsCycle([["b","a","c"],["c","a","c"],["d","d","c"],["b","c","c"]]))
    print(sol.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
    print(sol.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
    print(sol.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]))

if __name__ == '__main__':
    main()