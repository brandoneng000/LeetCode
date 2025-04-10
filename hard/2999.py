from typing import List

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(num: int, limit: int, s: str):
            num_str = str(num)
            n = len(num_str) - len(s)

            if n < 0:
                return 0
            
            dp = [[0] * 2 for _ in range(n + 1)]

            dp[n][0] = 1
            dp[n][1] = int(num_str[n:] >= s)

            for i in range(n - 1, -1, -1):
                digit = int(num_str[i])

                dp[i][0] = (limit + 1) * dp[i + 1][0]

                if digit <= limit:
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = (limit + 1) * dp[i + 1][0]
            
            return dp[0][1]

        return count(finish, limit, s) - count(start - 1, limit, s)
        
def main():
    sol = Solution()
    print(sol.numberOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124"))
    print(sol.numberOfPowerfulInt(start = 15, finish = 215, limit = 6, s = "10"))
    print(sol.numberOfPowerfulInt(start = 1000, finish = 2000, limit = 4, s = "3000"))

if __name__ == '__main__':
    main()