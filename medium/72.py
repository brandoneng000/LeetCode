class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        
        for i in range(len(dp[0])):
            dp[0][i] = i
        for i in range(len(dp)):
            dp[i][0] = i
        
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word1[j] != word2[i]:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
                else:
                    dp[i + 1][j + 1] = dp[i][j]

        return dp[len(word2)][len(word1)]


def main():
    sol = Solution()
    print(sol.minDistance(word1 = "horse", word2 = "ros"))
    print(sol.minDistance(word1 = "intention", word2 = "execution"))

if __name__ == '__main__':
    main()