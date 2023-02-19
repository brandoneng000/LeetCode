from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        end = len(mat)

        for index in range(end):
            result += mat[index][index]
            result += mat[index][end - 1 - index]

        if end % 2 == 1:
            result -= mat[end // 2][end // 2]

        return result

def main():
    sol = Solution()
    print(sol.diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))
    print(sol.diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))
    print(sol.diagonalSum([[5]]))

if __name__ == '__main__':
    main()