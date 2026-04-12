class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(p: int, q: int):
            x1, y1 = divmod(p, 6)
            x2, y2 = divmod(q, 6)
            
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        INF = 10 ** 30
        dp = [[[INF] * 26 for _ in range(26)] for _ in range(n)]

        for i in range(26):
            dp[0][i][ord(word[0]) - 65] = 0
            dp[0][ord(word[0]) - 65][i] = 0

        for i in range(1, n):
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            dist = get_dist(prev, cur)

            for j in range(26):
                dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][prev][j] + dist)
                dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][prev] + dist)

                if prev == j:
                    for k in range(26):
                        d0 = get_dist(k, cur)
                        dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][k][j] + d0)
                        dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][k] + d0)
        
        return min(min(dp[n - 1][x]) for x in range(26))
        
def main():
    sol = Solution()
    print(sol.minimumDistance("CAKE"))
    print(sol.minimumDistance("HAPPY"))

if __name__ == '__main__':
    main()