from typing import List
from string import ascii_lowercase
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def word_check(cur: Counter):
            return all(cur[letter] <= letter_count[letter] for letter in ascii_lowercase)
        def get_score(cur: Counter):
            return sum(score[ord(letter) - ord('a')] * cur[letter] for letter in cur)
        def helper(cur: Counter, index: int):
            self.res = max(self.res, get_score(cur))

            for i in range(index, n):
                cur += Counter(words[i])
                if word_check(cur):
                    helper(cur, i + 1)
                cur -= Counter(words[i])

        n = len(words)
        letter_count = Counter(letters)
        self.res = 0
        helper(Counter(), 0)
        return self.res
        
def main():
    sol = Solution()
    print(sol.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
    print(sol.maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
    print(sol.maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))

if __name__ == '__main__':
    main()