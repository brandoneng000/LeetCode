class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        s = 1 if k > 0 else 0

        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]

        return sum(dp[k:])

def main():
    sol = Solution()
    print(sol.new21Game(n = 10, k = 1, maxPts = 10))
    print(sol.new21Game(n = 6, k = 1, maxPts = 10))
    print(sol.new21Game(n = 21, k = 17, maxPts = 10))

if __name__ == '__main__':
    main()