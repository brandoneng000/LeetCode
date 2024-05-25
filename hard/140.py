from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(cur_sentence: List[str], index: int):
            if index == n:
                self.res.append(' '.join(cur_sentence))
                return
            
            cur = []
            for i in range(index, n):
                cur.append(s[i])
                word = ''.join(cur)
                if word in words:
                    cur_sentence.append(word)
                    helper(cur_sentence, i + 1)
                    cur_sentence.pop()

        n = len(s)
        words = set(wordDict)
        self.res = []
        helper([], 0)

        return self.res
        
def main():
    sol = Solution()
    print(sol.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
    print(sol.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
    print(sol.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))

if __name__ == '__main__':
    main()