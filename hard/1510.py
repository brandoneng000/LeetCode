class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1

            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]

def main():
    sol = Solution()
    print(sol.winnerSquareGame(1))
    print(sol.winnerSquareGame(2))
    print(sol.winnerSquareGame(4))

if __name__ == '__main__':
    main()