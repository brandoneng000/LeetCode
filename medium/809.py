from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def helper(word: str, s: str):
            j = 0
            for i in range(len(s)):
                if j < len(word) and s[i] == word[j]:
                    j += 1
                elif s[i - 1: i + 2] != s[i] * 3 != s[i - 2: i + 1]:
                    return False
            return j == len(word)

        return sum(helper(word, s) for word in words)



def main():
    sol = Solution()
    print(sol.expressiveWords(s = "heeellooo", words = ["hello", "hi", "helo"]))
    print(sol.expressiveWords(s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]))

if __name__ == '__main__':
    main()