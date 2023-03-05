from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                result[c][r] = matrix[r][c]
        
        return result


def main():
    sol = Solution()
    print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.transpose([[1,2,3],[4,5,6]]))

if __name__ == '__main__':
    main()