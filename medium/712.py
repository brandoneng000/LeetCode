class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        
        m, n = len(s1), len(s2)
        dp = [0] * (n + 1)

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])
        
        for i in range(1, m + 1):
            prev_diag = dp[0]
            dp[0] += ord(s1[i - 1])

            for j in range(1, n + 1):
                temp = dp[j]

                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev_diag
                else:
                    dp[j] = min(
                        dp[j - 1] + ord(s2[j - 1]),
                        temp + ord(s1[i - 1])
                    )
                prev_diag = temp
        
        return dp[n]
        

    # def minimumDeleteSum(self, s1: str, s2: str) -> int:
    #     dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        
    #     for i in range(len(s1) - 1, -1, -1):
    #         dp[i][len(s2)] = dp[i + 1][len(s2)] + ord(s1[i])
    #     for i in range(len(s2) - 1, -1, -1):
    #         dp[len(s1)][i] = dp[len(s1)][i + 1] + ord(s2[i])
        
    #     for i in range(len(s1) - 1, -1, -1):
    #         for j in range(len(s2) - 1, -1, -1):
    #             if s1[i] == s2[j]:
    #                 dp[i][j] = dp[i + 1][j + 1]
    #             else:
    #                 dp[i][j] = min(dp[i + 1][j] + ord(s1[i]), dp[i][j + 1] + ord(s2[j]))
        
    #     return dp[0][0]

def main():
    sol = Solution()
    print(sol.minimumDeleteSum(s1 = "sea", s2 = "eat"))
    print(sol.minimumDeleteSum(s1 = "delete", s2 = "leet"))

if __name__ == '__main__':
    main()