from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()

        for index_row, row in enumerate(matrix):
            for index_column, column in enumerate(row):
                if column == 0:
                    zero_rows.add(index_row)
                    zero_columns.add(index_column)

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if row in zero_rows or column in zero_columns:
                    matrix[row][column] = 0

def main():
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(sol.setZeroes(matrix))
    print(matrix)

if __name__ == '__main__':
    main()