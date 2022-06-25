from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_begin, row_end = 0, len(matrix) - 1
        column_begin, column_end = 0, len(matrix[0]) - 1
        order = []

        while(row_begin <= row_end and column_begin <= column_end):
            # Go right
            for index in range(column_begin, column_end + 1):
                order.append(matrix[row_begin][index])
            row_begin += 1
            
            # Go down
            for index in range(row_begin, row_end + 1):
                order.append(matrix[index][column_end])
            column_end -= 1

            # Go left
            if row_begin <= row_end:
                for index in range(column_end, column_begin - 1, -1):
                    order.append(matrix[row_end][index])
                row_end -= 1
            
            # Go up
            if column_begin <= column_end:
                for index in range(row_end, row_begin - 1, -1):
                    order.append(matrix[index][column_begin])
                column_begin += 1

        return order
          

def main():
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == '__main__':
    main()