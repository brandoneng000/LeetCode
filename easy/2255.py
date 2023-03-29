from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # return sum(s.startswith(word) for word in words)
        # print(list(map(s.startswith, words)))
        return sum(map(s.startswith, words))

def main():
    sol = Solution()
    print(sol.countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc"))
    print(sol.countPrefixes(words = ["a","a"], s = "aa"))

if __name__ == '__main__':
    main()