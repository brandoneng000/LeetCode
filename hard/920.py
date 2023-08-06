class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 1000000007
        dp = [[0 for i in range(n + 1)] for j in range(goal + 1)]

        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % mod
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod
        
        return dp[goal][n]


def main():
    sol = Solution()
    print(sol.numMusicPlaylists(n = 10, goal = 15, k = 1))
    print(sol.numMusicPlaylists(n = 3, goal = 3, k = 1))
    print(sol.numMusicPlaylists(n = 2, goal = 3, k = 0))
    print(sol.numMusicPlaylists(n = 2, goal = 3, k = 1))

if __name__ == '__main__':
    main()