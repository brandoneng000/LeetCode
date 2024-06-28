from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = set('aeiou')
        prefix = [0] * (n + 1)
        res = []

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (words[i - 1][0] in vowels and words[i - 1][-1] in vowels)
        
        for l, r in queries:
            res.append(prefix[r + 1] - prefix[l])
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
    print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))

if __name__ == '__main__':
    main()