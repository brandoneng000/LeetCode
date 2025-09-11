from collections import Counter

class Solution:
    # def sortVowels(self, s: str) -> str:
    #     sorted_vowels = "AEIOUaeiou"
    #     count_vowels = Counter()
    #     res = []

    #     for letter in s:
    #         if letter in sorted_vowels:
    #             count_vowels[letter] += 1
        
    #     j = 0

    #     for letter in s:
    #         if letter not in sorted_vowels:
    #             res.append(letter)
    #         else:
    #             while j < len(sorted_vowels) and count_vowels[sorted_vowels[j]] == 0:
    #                 j += 1

    #             res.append(sorted_vowels[j])
    #             count_vowels[sorted_vowels[j]] -= 1
        
    #     return ''.join(res)

    def sortVowels(self, s: str) -> str:
        res = list(s)
        vowels = []
        vowel_index = []
        
        for index, letter in enumerate(s):
            if letter in "AEIOUaeiou":
                vowel_index.append(index)
                vowels.append(letter)
        
        for index, vowel in zip(vowel_index, sorted(vowels)):
            res[index] = vowel
        
        return "".join(res)


def main():
    sol = Solution()
    print(sol.sortVowels("lEetcOde"))
    print(sol.sortVowels("lYmpH"))

if __name__ == '__main__':
    main()