from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        cache[len(s)] = True

        for index in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (index + len(word)) <= len(s) and s[index: index + len(word)] == word:
                    cache[index] = cache[index + len(word)]
                if cache[index]:
                    break

        return cache[0]
        
def main():
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet","code"]))
    print(sol.wordBreak("applepenapple", ["apple","pen"]))
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

if __name__ == '__main__':
    main()