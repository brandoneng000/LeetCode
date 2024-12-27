class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 1000000007
        dp = [1] * n

        for _ in range(k):
            next_dp = [1]

            for i in range(1, n):
                next_dp.append((next_dp[-1] + dp[i]) % mod)
            
            dp = next_dp
        
        return dp[-1]
        
def main():
    sol = Solution()
    print(sol.valueAfterKSeconds(n = 4, k = 5))
    print(sol.valueAfterKSeconds(n = 5, k = 3))

if __name__ == '__main__':
    main()