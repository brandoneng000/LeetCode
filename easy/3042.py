from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                res += words[j].startswith(words[i]) and words[j].endswith(words[i])
        
        return res
        
def main():
    sol = Solution()
    print(sol.countPrefixSuffixPairs(["a","aba","ababa","aa"]))
    print(sol.countPrefixSuffixPairs(["pa","papa","ma","mama"]))
    print(sol.countPrefixSuffixPairs(["abab","ab"]))

if __name__ == '__main__':
    main()