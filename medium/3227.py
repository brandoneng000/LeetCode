from typing import List

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        str_set = set(s)
        return any(vowel in str_set for vowel in "aeiou")

    # def doesAliceWin(self, s: str) -> bool:
    #     return sum(letter in "aeiou" for letter in s) != 0

    # def doesAliceWin(self, s: str) -> bool:
    #     vowels = set("aeiou")
    #     vowel_count = 0

    #     for letter in s:
    #         vowel_count += letter in vowels
        
    #     return vowel_count != 0
        
        
def main():
    sol = Solution()
    print(sol.doesAliceWin("leetcoder"))
    print(sol.doesAliceWin("bbcd"))

if __name__ == '__main__':
    main()