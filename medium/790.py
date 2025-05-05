class Solution:
    def numTilings(self, n: int) -> int:
        if n < 2:
            return n
        
        mod = 1000000007
        dp = [1] * (n + 1)
        dp[1] = 2
        for i in range(2, n):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]

        return dp[n - 1] % mod

def main():
    sol = Solution()
    print(sol.numTilings(5))
    print(sol.numTilings(4))
    print(sol.numTilings(3))
    print(sol.numTilings(1))

if __name__ == '__main__':
    main()