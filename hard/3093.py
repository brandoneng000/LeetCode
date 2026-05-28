from typing import List

INF = 10 ** 33

class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_len = INF
        self.idx = INF

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s: str, idx: int):
        node = self.root

        if len(s) < node.min_len:
            node.min_len = len(s)
            node.idx = idx

        for ch in s:
            c = ch

            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

            if len(s) < node.min_len:
                node.min_len = len(s)
                node.idx = idx
    
    def query(self, s: str):
        node = self.root

        for ch in s:
            if ch in node.children:
                node = node.children[ch]
            else:
                break
        
        return node.idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        res = []

        for i, word in enumerate(wordsContainer):
            reverse_word = word[::-1]
            trie.insert(reverse_word, i)

        for query in wordsQuery:
            reverse_query  = query[::-1]
            res.append(trie.query(reverse_query))
        
        return res

        
def main():
    sol = Solution()
    print(sol.stringIndices(wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]))
    print(sol.stringIndices(wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]))

if __name__ == '__main__':
    main()