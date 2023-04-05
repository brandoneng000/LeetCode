class Trie:

    def __init__(self):
        self.letters = {}
        self.end = False

    def insert(self, word: str) -> None:
        temp = self
        for letter in word:
            if letter not in temp.letters:
                temp.letters[letter] = Trie()
                temp = temp.letters[letter]
            else:
                temp = temp.letters[letter]
        temp.end = True

    def search(self, word: str) -> bool:
        temp = self
        for letter in word:
            if letter in temp.letters:
                temp = temp.letters[letter]
            else:
                return False
        
        return temp.end

    def startsWith(self, prefix: str) -> bool:
        temp = self.letters
        for letter in prefix:
            if letter in temp:
                temp = temp[letter].letters
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)