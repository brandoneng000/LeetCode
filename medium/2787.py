from collections import Counter

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 1000000007
        dp = Counter()
        dp[0] = 1

        for i in range(1, n + 1):
            num = i ** x

            if num > n:
                break

            next_dp = Counter()

            for j in sorted(dp):
                if num + j > n:
                    break
                next_dp[num + j] = (next_dp[num + j] + dp[j]) % mod
            
            dp.update(next_dp)
        
        return dp[n] % mod
        
def main():
    sol = Solution()
    print(sol.numberOfWays(n = 50, x = 2))
    print(sol.numberOfWays(n = 10, x = 2))
    print(sol.numberOfWays(n = 4, x = 1))

if __name__ == '__main__':
    main()