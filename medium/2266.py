class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        mod = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i - 2 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] += dp[i - 2]
            if i - 3 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3]:
                dp[i] += dp[i - 3]
            
            if pressedKeys[i - 1] in { "7", "9" }:
                if i - 4 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3] == pressedKeys[i - 4]:
                    dp[i] += dp[i - 4]
            
            dp[i] %= mod
        
        return dp[-1] % mod
        
def main():
    sol = Solution()
    print(sol.countTexts("22233"))
    print(sol.countTexts("222222222222222222222222222222222222"))

if __name__ == '__main__':
    main()