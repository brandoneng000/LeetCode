from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]
        
def main():
    sol = Solution()
    print(sol.findWordsContaining(words = ["leet","code"], x = "e"))
    print(sol.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "a"))
    print(sol.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "z"))

if __name__ == '__main__':
    main()