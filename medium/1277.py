from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        
        return sum(sum(row) for row in matrix)

def main():
    sol = Solution()
    print(sol.countSquares([[0,1,1,1],
                            [1,1,1,1],
                            [0,1,1,1]]))
    print(sol.countSquares([[1,0,1],
                            [1,1,0],
                            [1,1,0]]))

if __name__ == '__main__':
    main()