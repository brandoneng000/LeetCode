class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 1000000007
        dp = [[0], [0, 0]]
        cur_size = 1
        dp[0][0] = 1

        for i in range(steps):
            for j in range(cur_size):
                if j == 0:
                    dp[1][j] += dp[0][j]
                    dp[1][j + 1] += dp[0][j]
                elif j == arrLen - 1:
                    dp[1][j] += dp[0][j]
                    dp[1][j - 1] += dp[0][j]
                else:
                    dp[1][j] += dp[0][j]
                    dp[1][j + 1] += dp[0][j]
                    dp[1][j - 1] += dp[0][j]
            
            if cur_size < arrLen:
                cur_size += 1

            dp[0] = dp[1] + [0]
            dp[1] = [0] * (cur_size + 1)
            
        
        return dp[0][0] % mod
                    
        
def main():
    sol = Solution()
    print(sol.numWays(steps = 3, arrLen = 2))
    print(sol.numWays(steps = 2, arrLen = 4))
    print(sol.numWays(steps = 4, arrLen = 2))

if __name__ == '__main__':
    main()