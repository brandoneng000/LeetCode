from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def valid_space(row: int, col: int):
            if 0 <= row < n and 0 <= col < m and (row, col) not in visited and grid[row][col] != 0:
                return True
            return False

        def dfs(row: int, col: int):
            res = grid[row][col]

            for dr, dc in direction:
                r = row + dr
                c = col + dc

                if valid_space(r, c):
                    visited.add((r, c))
                    res += dfs(r, c)

            return res
            

        n, m = len(grid), len(grid[0])
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        res = 0

        for i in range(n):
            for j in range(m):
                if valid_space(i, j):
                    visited.add((i, j))
                    res += 1 if dfs(i, j) % k == 0 else 0

        return res

def main():
    sol = Solution()
    print(sol.countIslands(grid = [[13,0,10],[7,9,0],[0,19,0]], k = 6))
    print(sol.countIslands(grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5))
    print(sol.countIslands(grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3))

if __name__ == '__main__':
    main()