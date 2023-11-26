from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
            
            cur_row = sorted(matrix[i], reverse=True)
            for j in range(n):
                res = max(res, cur_row[j] * (j + 1))
        
        return res

        
def main():
    sol = Solution()
    print(sol.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
    print(sol.largestSubmatrix([[1,0,1,0,1]]))
    print(sol.largestSubmatrix([[1,1,0],[1,0,1]]))

if __name__ == '__main__':
    main()