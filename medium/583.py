from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[len(word1)][len(word2)]
    # def minDistance(self, word1: str, word2: str) -> int:
    #     res = 0
    #     temp = set(word1) - set(word2)
    #     matching_word1, matching_word2 = [], []
    #     for letter in word1:
    #         if letter not in temp:
    #             matching_word1.append(letter)
    #         else:
    #             res += 1

    #     temp = set(word2) - set(word1)
    #     for letter in word2:
    #         if letter not in temp:
    #             matching_word2.append(letter)
    #         else:
    #             res += 1
        
    #     self.memo = [[0 for i in range(len(matching_word2) + 1)] for j in range(len(matching_word1) + 1)]
    #     common = self.lcs(matching_word1, matching_word2, len(matching_word1), len(matching_word2))
    #     return res + (len(matching_word1) - common) + (len(matching_word2) - common)
    
    # def lcs(self, s1: List[str], s2: List[str], m: int, n: int):
    #     if m == 0 or n == 0:
    #         return 0
    #     if self.memo[m][n] > 0:
    #         return self.memo[m][n]
    #     if s1[m - 1] == s2[n - 1]:
    #         self.memo[m][n] = 1 + self.lcs(s1, s2, m - 1, n - 1)
    #     else:
    #         self.memo[m][n] = max(self.lcs(s1, s2, m - 1, n), self.lcs(s1, s2, m, n - 1))
        
    #     return self.memo[m][n]

def main():
    sol = Solution()
    print(sol.minDistance(word1 = "sea", word2 = "eat"))
    print(sol.minDistance(word1 = "leetcode", word2 = "etco"))

if __name__ == '__main__':
    main()