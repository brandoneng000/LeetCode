from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    res += dp[i + 1][j + 1]
        
        return res

    # def countSquares(self, matrix: List[List[int]]) -> int:
    #     for i in range(1, len(matrix)):
    #         for j in range(1, len(matrix[0])):
    #             matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        
    #     return sum(sum(row) for row in matrix)

def main():
    sol = Solution()
    print(sol.countSquares([[0,1,1,1],
                            [1,1,1,1],
                            [0,1,1,1]]))
    print(sol.countSquares([[1,0,1],
                            [1,1,0],
                            [1,1,0]]))

if __name__ == '__main__':
    main()