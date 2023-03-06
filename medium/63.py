from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # destination = len(obstacleGrid) * len(obstacleGrid[0])
        
        # def move(row: int, col: int, obstacleGrid: List[List[int]]):
        #     if row >= len(obstacleGrid) or col >= len(obstacleGrid[0]):
        #         return 0
        #     elif obstacleGrid[row][col] == 1:
        #         return 0
        #     elif (row + 1) * (col + 1) == destination:
        #         return 1
            
        #     return move(row + 1, col, obstacleGrid) + move(row, col + 1, obstacleGrid)

        # return move(0, 0, obstacleGrid)

        row_size = len(obstacleGrid)
        col_size = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1

        for i in range(1, row_size):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        for j in range(1, col_size):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        
        for i in range(1, row_size):
            for j in range(1, col_size):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[row_size - 1][col_size - 1]

def main():
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))
    print(sol.uniquePathsWithObstacles([[0,0],[0,1]]))

if __name__ == '__main__':
    main()