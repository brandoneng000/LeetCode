from typing import List

class MagicDictionary:

    def __init__(self):
        self.dictionary = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dictionary[len(word)] = self.dictionary.get(len(word), []) + [word]      

    def search(self, searchWord: str) -> bool:
        for word in self.dictionary.get(len(searchWord), []):
            differences = 0
            for i in range(len(searchWord)):
                if searchWord[i] != word[i]:
                    differences += 1
            
            if differences == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)