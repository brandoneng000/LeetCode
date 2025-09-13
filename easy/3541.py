from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        vowels = set("aeiou")
        max_vowel = 0
        max_consonant = 0

        for letter in count:
            if letter in vowels:
                max_vowel = max(max_vowel, count[letter])
            else:
                max_consonant = max(max_consonant, count[letter])
        
        return max_vowel + max_consonant
        
def main():
    sol = Solution()
    print(sol.maxFreqSum("successes"))
    print(sol.maxFreqSum("aeiaeia"))

if __name__ == '__main__':
    main()