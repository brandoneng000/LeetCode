class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if ord(c) - ord('a') not in curr.children:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]
        
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for char in curr.children:
                    if char != None and curr.children[char].search(word[i + 1:]):
                        return True
                return False

            if ord(c) - ord('a') not in curr.children:
                return False
            curr = curr.children[ord(c) - ord('a')]
        
        return curr != None and curr.end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)