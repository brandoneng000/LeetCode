from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
        
def main():
    sol = Solution()
    print(sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
    print(sol.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
    print(sol.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))

if __name__ == '__main__':
    main()