class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [c == '0' for c in s]

        pre = 0

        for i in range(1, n):
            if i >= minJump:
                pre += dp[i - minJump]
            if i > maxJump:
                pre -= dp[i - maxJump - 1]
            dp[i] &= pre > 0
        
        return dp[-1]

        
def main():
    sol = Solution()
    print(sol.canReach(s = "0101010101001010101001010010101010101", minJump = 2, maxJump = 3))
    print(sol.canReach(s = "011010", minJump = 2, maxJump = 3))
    print(sol.canReach(s = "01101110", minJump = 2, maxJump = 3))

if __name__ == '__main__':
    main()