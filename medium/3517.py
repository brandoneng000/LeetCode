from collections import Counter
from string import ascii_lowercase

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt_letters = Counter(s)
        center = ""
        left = []

        for letter in ascii_lowercase:
            if cnt_letters[letter] % 2 == 1:
                center = letter

            left.extend([letter] * (cnt_letters[letter] // 2))

        return ''.join(left + [center] + left[::-1])

def main():
    sol = Solution()
    print(sol.smallestPalindrome("z"))
    print(sol.smallestPalindrome("babab"))
    print(sol.smallestPalindrome("daccad"))

if __name__ == '__main__':
    main()