from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:        
        for j in range(k):
            for i in range(k // 2):
                temp = grid[x + i][y + j]
                grid[x + i][y + j] = grid[x + k - i - 1][y + j]
                grid[x + k - i - 1][y + j] = temp

        return grid
        

def main():
    sol = Solution()
    print(sol.reverseSubmatrix(grid = [[6,16,14],[1,2,19],[14,17,15],[18,7,6],[14,12,5]], x = 2, y = 1, k = 2))
    print(sol.reverseSubmatrix(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3))
    print(sol.reverseSubmatrix(grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2))

if __name__ == '__main__':
    main()