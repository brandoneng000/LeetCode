from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set(list('aeiou'))
        return sum(words[i][0] in vowels and words[i][-1] in vowels for i in range(left, right + 1))

def main():
    sol = Solution()
    print(sol.vowelStrings(words = ["are","amy","u"], left = 0, right = 2))
    print(sol.vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4))

if __name__ == '__main__':
    main()