from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_count = Counter(words)
        used = set()
        center = False
        res = 0

        for word in words_count:
            if word in used:
                continue
            rev_word = word[::-1]

            if word == rev_word:
                res += (words_count[word] // 2) * 4

                if words_count[word] % 2 and not center:
                    res += 2
                    center = True
            elif rev_word in words_count:
                res += min(words_count[word], words_count[rev_word]) * 4
                used.add(rev_word)

        return res
        
def main():
    sol = Solution()
    print(sol.longestPalindrome(words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
    print(sol.longestPalindrome(words = ["lc","cl","gg"]))
    print(sol.longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))
    print(sol.longestPalindrome(words = ["cc","ll","xx"]))

if __name__ == '__main__':
    main()