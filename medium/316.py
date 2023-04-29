from typing import List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters = []
        last_index = {}
        letter_check = set()
        
        for index, letter in enumerate(s):
            last_index[letter] = index

        for index, letter in enumerate(s):
            if letter in letter_check:
                continue
            while letters and letter < letters[-1] and letters[-1] in s[index + 1:]:
                letter_check.remove(letters.pop())
        
            letters.append(letter)
            letter_check.add(letter)
        
        return "".join(letters)

def main():
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"))
    print(sol.removeDuplicateLetters("cbacdcbc"))

if __name__ == '__main__':
    main()