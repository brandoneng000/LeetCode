from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        count = Counter()

        for w in words:
            for c in w:
                count[c] += 1
        
        return all(count[l] % n == 0 for l in count)

def main():
    sol = Solution()
    print(sol.makeEqual(["a", "b"]))
    print(sol.makeEqual(["abc","aabc","bc"]))
    print(sol.makeEqual(["ab","a"]))

if __name__ == '__main__':
    main()