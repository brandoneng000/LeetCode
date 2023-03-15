from typing import List
import collections

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # words1_count = collections.Counter(words1)
        # words2_count = collections.Counter(words2)
        # words = set(words1 + words2)
        # result = 0
        # for word in words:
        #     if words1_count.get(word, 0) == 1 and words2_count.get(word, 0) == 1:
        #         result += 1
        
        # return result
        words1_count = collections.Counter(words1)
        for word in words2:
            if word in words1_count and words1_count[word] < 2:
                words1_count[word] -= 1
        
        return sum(words1_count[word] == 0 for word in words1_count)


def main():
    sol = Solution()
    print(sol.countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]))
    print(sol.countWords(words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]))
    print(sol.countWords(words1 = ["a","ab"], words2 = ["a","a","a","ab"]))

if __name__ == '__main__':
    main()