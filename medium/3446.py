from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            x = i
            y = 0
            cur = []
            
            while x < n and y < m:
                cur.append(grid[x][y])
                x += 1
                y += 1
            
            cur.sort(reverse=True)
            x, y = i, 0
            index = 0

            while x < n and y < m:
                grid[x][y] = cur[index]
                x += 1
                y += 1
                index += 1

        for j in range(1, m):
            x, y = 0, j
            cur = []

            while x < n and y < m:
                cur.append(grid[x][y])
                x += 1
                y += 1
            
            cur.sort()
            x, y = 0, j
            index = 0

            while x < n and y < m:
                grid[x][y] = cur[index]
                x += 1
                y += 1
                index += 1

        return grid
        
def main():
    sol = Solution()
    print(sol.sortMatrix([[1,7,3],[9,8,2],[4,5,6]]))
    print(sol.sortMatrix([[0,1],[1,2]]))
    print(sol.sortMatrix([[1]]))

if __name__ == '__main__':
    main()