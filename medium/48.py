from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        
    def transpose(self, matrix):
        size = len(matrix)

        for row in range(size):
            for column in range(row + 1, size):
                matrix[column][row], matrix[row][column] = matrix[row][column], matrix[column][row]
    
    def reflect(self, matrix):
        size = len(matrix)

        for row in range(size):
            for column in range(size // 2):
                matrix[row][column], matrix[row][-column - 1] = matrix[row][-column - 1], matrix[row][column]

            
def main():
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix)
    print(matrix)
    sol.rotate(matrix)
    print(matrix)

if __name__ == '__main__':
    main()