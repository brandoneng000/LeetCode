from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(word: str) -> bool:
            return word == word[::-1]

        for word in words:
            if is_palindrome(word):
                return word
        
        return ""

def main():
    sol = Solution()
    print(sol.firstPalindrome(["abc","car","ada","racecar","cool"]))
    print(sol.firstPalindrome(["notapalindrome","racecar"]))
    print(sol.firstPalindrome(["def","ghi"]))

if __name__ == '__main__':
    main()