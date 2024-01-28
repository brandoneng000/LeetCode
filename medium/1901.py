from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left = 0
        right = n - 1

        while left <= right:
            max_row = 0
            middle = (left + right) // 2

            for row in range(m):
                max_row = row if (mat[row][middle] >= mat[max_row][middle]) else max_row

            left_larger = middle - 1 >= left and mat[max_row][middle - 1] > mat[max_row][middle]
            right_larger = middle + 1 <= right and mat[max_row][middle + 1] > mat[max_row][middle]

            if (not left_larger) and (not right_larger):
                return [max_row, middle]
            elif right_larger:
                left = middle + 1
            else:
                right = middle - 1
        
        return []


        
def main():
    sol = Solution()
    print(sol.findPeakGrid([[1,4],[3,2]]))
    print(sol.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))

if __name__ == '__main__':
    main()