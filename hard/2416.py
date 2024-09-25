from typing import List

class Trie:
    def __init__(self) -> None:
        self.child = {}
        self.count = 0

def insert_word(root: Trie, word: str):
    cur = root

    for letter in word:
        if letter not in cur.child:
            cur.child[letter] = Trie()

        cur = cur.child[letter]
        cur.count += 1

def count_word(root: Trie, word: str):
    cur = root
    res = 0

    for letter in word:
        cur = cur.child[letter]
        res += cur.count
    
    return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()

        for word in words:
            insert_word(root, word)
        
        return [count_word(root, word) for word in words]

        
def main():
    sol = Solution()
    print(sol.sumPrefixScores(words = ["abc","ab","bc","b"]))
    print(sol.sumPrefixScores(words = ["abcd"]))

if __name__ == '__main__':
    main()