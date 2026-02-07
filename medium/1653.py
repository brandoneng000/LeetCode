class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        count = 0

        for c in s:
            if c == 'b':
                count += 1
            else:
                res = min(res + 1, count)
        
        return res

    # def minimumDeletions(self, s: str) -> int:
    #     n = len(s)
    #     dp = [0] * (n + 1)
    #     count_b = 0

    #     for i, letter in enumerate(s):
    #         if letter == 'a':
    #             dp[i + 1] = min(dp[i] + 1, count_b)
    #         else:
    #             dp[i + 1] = dp[i]
    #             count_b += 1
        
    #     return dp[-1]
        
def main():
    sol = Solution()
    print(sol.minimumDeletions("aababbab"))
    print(sol.minimumDeletions("bbaaaaabb"))

if __name__ == '__main__':
    main()