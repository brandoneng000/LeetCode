from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        word2_count = Counter(word2)
        res = 0
        matches = len(word2_count)
        j = 0

        for i, letter in enumerate(word1):
            word2_count[letter] -= 1
            matches -= word2_count[letter] == 0

            while matches == 0:
                matches += word2_count[word1[j]] == 0
                word2_count[word1[j]] += 1
                j += 1
            res += j
        
        return res
        

        
def main():
    sol = Solution()
    print(sol.validSubstringCount(word1 = "aabbcc", word2 = "abc"))
    print(sol.validSubstringCount(word1 = "bcca", word2 = "abc"))
    print(sol.validSubstringCount(word1 = "abcabc", word2 = "abc"))
    print(sol.validSubstringCount(word1 = "abcabc", word2 = "aaabc"))

if __name__ == '__main__':
    main()