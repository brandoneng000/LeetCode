from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for j in range(n)] for i in range(m)]
        res = m * n - len(walls) - len(guards)

        for r, c in walls:
            grid[r][c] = 1
        
        for row, col in guards:
            grid[row][col] = 2

        for row, col in guards:
            for c in range(col - 1, -1, -1):
                if grid[row][c] == 0:
                    res -= 1
                elif grid[row][c] == 1 or grid[row][c] == 2:
                    break
                grid[row][c] = 3
            
            for c in range(col + 1, n):
                if grid[row][c] == 0:
                    res -= 1
                elif grid[row][c] == 1 or grid[row][c] == 2:
                    break
                grid[row][c] = 3
            
            for r in range(row - 1, -1, -1):
                if grid[r][col] == 0:
                    res -= 1
                elif grid[r][col] == 1 or grid[r][col] == 2:
                    break
                grid[r][col] = 3
            
            for r in range(row + 1, m):
                if grid[r][col] == 0:
                    res -= 1
                elif grid[r][col] == 1 or grid[r][col] == 2:
                    break
                grid[r][col] = 3

        return res
            

def main():
    sol = Solution()
    print(sol.countUnguarded(m = 8, n = 9, guards = [[5,8],[5,5],[4,6],[0,5],[6,5]], walls = [[4,1]]))
    print(sol.countUnguarded(m = 2, n = 7, guards = [[1,5],[1,1],[1,6],[0,2]], walls = [[0,6],[0,3],[0,5]]))
    print(sol.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))
    print(sol.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]))


if __name__ == '__main__':
    main()