from typing import List
from collections import Counter
# import collections

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_count = Counter()
        res = []

        for word in words2:
            letter_count = Counter(word)

            for letter in letter_count:
                words2_count[letter] = max(words2_count[letter], letter_count[letter])

        for word in words1:
            if not (words2_count - Counter(word)):
                res.append(word)
        
        return res


    # def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    #     words2_counter = [collections.Counter(word) for word in words2]
    #     res = []

    #     full_counter = collections.Counter()

    #     for letter_counter in words2_counter:
    #         for letter in letter_counter:
    #             full_counter[letter] = max(full_counter[letter], letter_counter[letter])

    #     for word in words1:
    #         state = True
    #         word_counter = collections.Counter(word)
    #         for letter in full_counter:
    #             if word_counter[letter] < full_counter[letter]:
    #                 state = False
    #         if state:
    #             res.append(word)

    #     return res

def main():
    sol = Solution()
    print(sol.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))
    print(sol.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]))
    print(sol.wordSubsets(words1 = ["goggle"], words2 = ["lo","eo","oo"]))

if __name__ == '__main__':
    main()