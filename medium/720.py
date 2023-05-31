from typing import List

class Trie:
    def __init__(self) -> None:
        self.end = False
        self.letters = {}
    
    def insert_word(self, word: str):
        temp = self
        for letter in word:
            if letter not in temp.letters:
                temp.letters[letter] = Trie()
            temp = temp.letters[letter]
        temp.end = True
    
    def get_longest_word(self) -> str:
        def dfs(trie: Trie, char: str):
            longest_word = char
            for letter in trie.letters:
                if trie.letters[letter].end:
                    temp_word = char + dfs(trie.letters[letter], letter)
                    if len(temp_word) == len(longest_word):
                        longest_word = min(longest_word, temp_word)
                    else:
                        longest_word = max(longest_word, temp_word, key=len)
            
            return longest_word
            
        longest = ""
        for letter in self.letters:
            if self.letters[letter].end:
                    temp_word = dfs(self.letters[letter], letter)
                    if len(temp_word) == len(longest):
                        longest = min(longest, temp_word)
                    else:
                        longest = max(longest, temp_word, key=len)
        return longest

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert_word(word)
        
        return trie.get_longest_word()

def main():
    sol = Solution()
    print(sol.longestWord(words = ["w","wo","wor","worl","world"]))
    print(sol.longestWord(["a","banana","app","appl","ap","apply","apple"]))

if __name__ == '__main__':
    main()