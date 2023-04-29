from typing import List
import collections
import string

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        dictionary_counters = {}

        for word in words:
            dictionary_counters[word] = set(word)

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # if  len(dictionary_counters[words[i]] - dictionary_counters[words[j]]) == len(dictionary_counters[words[i]]):
                if not dictionary_counters[words[i]] & dictionary_counters[words[j]]:
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res
        

def main():
    sol = Solution()
    print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
    print(sol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
    print(sol.maxProduct(["a","aa","aaa","aaaa"]))

if __name__ == '__main__':
    main()