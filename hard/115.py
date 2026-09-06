class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        if n < m:
            return 0

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]

def main():
    sol = Solution()
    print(sol.numDistinct(s = "rabbbit", t = "rabbit"))
    print(sol.numDistinct(s = "babgbag", t = "bag"))

if __name__ == '__main__':
    main()