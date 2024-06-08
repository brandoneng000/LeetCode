from collections import Counter

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 1000000007
        dp = Counter([0])

        for i in range(min(zero, one), high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % mod
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % mod

        return sum(dp[i] for i in range(low, high + 1)) % mod
        

def main():
    sol = Solution()
    print(sol.countGoodStrings(low = 3, high = 3, zero = 1, one = 1))
    print(sol.countGoodStrings(low = 2, high = 3, zero = 1, one = 2))

if __name__ == '__main__':
    main()