from typing import List
import collections

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        res = 0

        for word in words:
            word_dict[word[0]].append(word)

        for c in s:
            temp = word_dict[c]
            word_dict[c] = []
            for word in temp:
                if len(word) == 1:
                    res += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return res

    # def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    #     res = 0
    #     for word in words:
    #         s_index = 0
    #         for i, c in enumerate(word):
    #             if c in s[s_index:]:
    #                 s_index = s.index(c, s_index) + 1
    #             else:
    #                 break
    #             if i == len(word) - 1:
    #                 res += 1

    #     return res

def main():
    sol = Solution()
    print(sol.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
    print(sol.numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

if __name__ == '__main__':
    main()