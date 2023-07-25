import collections

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = collections.defaultdict(int)

        for i in range(len(text1)):
            for j in range(len(text2)):
                dp[i + 1, j + 1] = dp[i, j] + 1 if text1[i] == text2[j] else max(dp[i + 1, j], dp[i, j + 1])
        
        return dp[len(text1), len(text2)]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     def check_words(shorter: str, longer: str):
    #         index = 0
    #         for letter in longer:
    #             if index < len(shorter) and shorter[index] == letter:
    #                 index += 1
    #             elif index == len(shorter):
    #                 break
            
    #         return index == len(shorter)

    #     def generate_subsequence(cur: List[str], index: int, size: int, string: str):
    #         if len(cur) == size:
    #             self.subsequences.add("".join(cur))
    #             return
            
    #         for i in range(index, len(string)):
    #             cur.append(string[i])
    #             generate_subsequence(cur, i + 1, size, string)
    #             cur.pop()

    #     shorter = min(text1, text2, key=len)
    #     longer = max(text2, text1, key=len)

    #     for size in range(len(shorter), 0, -1):
    #         self.subsequences = set()
    #         generate_subsequence([], 0, size, shorter)
    #         for subseq in self.subsequences:
    #             if check_words(subseq, longer):
    #                 return size
        
    #     return 0

        
def main():
    sol = Solution()
    print(sol.longestCommonSubsequence(text1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
                                       text2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" ))
    print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
    print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(sol.longestCommonSubsequence(text1 = "abc", text2 = "def"))

if __name__ == '__main__':
    main()