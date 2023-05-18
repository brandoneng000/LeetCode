from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""

        for word in dictionary:
            check = self.check_word(s, word)
            if check and len(res) < len(word):
                res = word
            elif check and len(res) == len(word):
                res = min(res, word)

        return res

    
    def check_word(self, s: str, word: str) -> bool:
        index = 0
        
        for i in range(len(s)):
            if index < len(word) and s[i] == word[index]:
                index += 1

        return index == len(word)

def main():
    sol = Solution()
    print(sol.findLongestWord(s = "bapple", dictionary = ["apple", "bpple"]))
    print(sol.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))
    print(sol.findLongestWord(s = "abpcplea", dictionary = ["a","b","c"]))

if __name__ == '__main__':
    main()