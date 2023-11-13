class Solution:
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