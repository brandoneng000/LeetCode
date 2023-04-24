from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # top, bottom = 0, len(matrix)

        # for r in range(len(matrix[0])):
        #     top, bottom = 0, len(matrix)
        #     while top <= bottom:
        #         middle = (top + bottom) // 2
        #         if middle >= len(matrix):
        #             break
        #         if matrix[middle][r] == target:
        #             return True
        #         elif matrix[middle][r] > target:
        #             bottom = middle - 1
        #         else:
        #             top = middle + 1
            
        # return False

        row, col = 0, len(matrix[0]) - 1

        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False

def main():
    sol = Solution()
    print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
    print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))

if __name__ == '__main__':
    main()