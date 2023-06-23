from typing import List
import collections

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_count = self.pattern_counter(pattern)
        res = []
        
        for word in words:
            word_count = self.pattern_counter(word)
            same = True
            for p, w in zip(pattern_count.keys(), word_count.keys()):
                if pattern_count[p] != word_count[w]:
                    same = False
                if not same:
                    break
            if same:
                res.append(word)
        
        return res
    
    def pattern_counter(self, word: str):
        res = collections.OrderedDict()
        count = 0
        cur = word[0]
        start = 0
        for index, letter in enumerate(word):
            if cur == letter:
                count += 1
            else:
                res.setdefault(cur, []).append((start, count))
                cur = letter
                start = index
                count = 1
        res.setdefault(cur, []).append((start, count))
        
        return res

def main():
    sol = Solution()
    print(sol.findAndReplacePattern(words = ["zwfvzhrucv"], pattern = "zdqmjnczma"))
    print(sol.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
    print(sol.findAndReplacePattern(words = ["a","b","c"], pattern = "a"))

if __name__ == '__main__':
    main()