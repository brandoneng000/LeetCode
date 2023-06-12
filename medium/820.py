from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie, res = {}, 0
        for word in words:
            node = trie
            for c in reversed(word):
                if '#' in node: 
                    res -= node.pop('#')
                node = node.setdefault(c, {})
            if not node:
                node['#'] = len(word) + 1
                res += node['#']
        return res
        # words_set = set(words)

        # for word in words:
        #     for i in range(1, len(word)):
        #         words_set.discard(word[i:])
        
        # return sum(len(word) + 1 for word in words_set)
    

def main():
    sol = Solution()
    print(sol.minimumLengthEncoding(["me", "time"]))
    print(sol.minimumLengthEncoding(["time", "me", "bell"]))
    print(sol.minimumLengthEncoding(["t"]))

if __name__ == '__main__':
    main()