from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)
        row = None
        while top <= bottom and top < len(matrix) and bottom >= 0:
            middle = (top + bottom) // 2

            if matrix[middle][0] <= target <= matrix[middle][-1]:
                row = matrix[middle]
                break
            elif matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][-1] < target:
                top = middle + 1

        if not row:
            return False
        left, right = 0, len(row)
        
        while left <= right:
            middle = (left + right) // 2

            if row[middle] == target:
                return True
            elif row[middle] > target:
                right = middle - 1
            elif row[middle] < target:
                left = middle + 1
        
        return False



def main():
    sol = Solution()
    print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 11))
    print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
    print(sol.searchMatrix(matrix = [[1]], target = 0))
    print(sol.searchMatrix(matrix = [[1]], target = 1))
    print(sol.searchMatrix(matrix = [[1]], target = 2))

if __name__ == '__main__':
    main()