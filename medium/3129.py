class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 1000000007
        dp = [[[0] * 2 for _ in range(zero + 1)] for _ in range(one + 1)]
        dp[0][0][0] = dp[0][0][1] = 1

        for i in range(one + 1):
            for j in range(zero + 1):
                for k in range(1, limit + 1):
                    if i - k >= 0:
                        dp[i][j][1] = (dp[i][j][1] + dp[i - k][j][0]) % mod
                    
                    if j - k >= 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i][j - k][1]) % mod

        return (dp[one][zero][0] + dp[one][zero][1]) % mod
        
def main():
    sol = Solution()
    print(sol.numberOfStableArrays(zero = 1, one = 1, limit = 2))
    print(sol.numberOfStableArrays(zero = 1, one = 2, limit = 1))
    print(sol.numberOfStableArrays(zero = 3, one = 3, limit = 2))

if __name__ == '__main__':
    main()