from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (values[i] * values[j] * values[k]))

                # dp[i][j] = min(dp[i][k] + dp[k][j] + (values[i] * values[j] * values[k]) for k in range(i + 1, j))
        
        return dp[0][n - 1]


def main():
    sol = Solution()
    print(sol.minScoreTriangulation([1,2,3]))
    print(sol.minScoreTriangulation([3,7,4,5]))
    print(sol.minScoreTriangulation([1,3,1,4,1,5]))

if __name__ == '__main__':
    main()