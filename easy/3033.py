from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        col_max = [max(col) for col in zip(*matrix)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]
        
        return matrix

def main():
    sol = Solution()
    print(sol.modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))
    print(sol.modifiedMatrix([[3,-1],[5,2]]))

if __name__ == '__main__':
    main()