from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        size = n * n - 1
        row = col = 0
        cur = 0

        if grid[0][0] != 0:
            return False

        while cur < size:
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if 0 <= r < n and 0 <= c < n and grid[r][c] == cur + 1:
                    cur += 1
                    row = r
                    col = c
                    break
            else:
                return False

        return True
        
def main():
    sol = Solution()
    print(sol.checkValidGrid([[8,3,6],[5,0,1],[2,7,4]]))
    print(sol.checkValidGrid([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]))
    print(sol.checkValidGrid([[0,3,6],[5,8,1],[2,7,4]]))

if __name__ == '__main__':
    main()