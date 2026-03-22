from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = "aeiou"
        res = 0

        for left in range(n):
            vowel_count = Counter()
            consonants = 0
            
            for right in range(left, n):
                if word[right] in vowels:
                    vowel_count[word[right]] += 1
                else:
                    consonants += 1
                
                if consonants > k:
                    break

                if consonants == k and len(vowel_count) == 5:
                    res += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.countOfSubstrings(word = "aeioqq", k = 1))
    print(sol.countOfSubstrings(word = "aeiou", k = 0))
    print(sol.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))

if __name__ == '__main__':
    main()