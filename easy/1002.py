from typing import List
from collections import Counter
from string import ascii_lowercase

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])

        for word in words:
            res &= Counter(word)
        
        return list(res.elements())
        
    # def commonChars(self, words: List[str]) -> List[str]:
    #     res = Counter(ascii_lowercase)

    #     for letter in res:
    #         res[letter] = 100
        
    #     for word in words:
    #         count = Counter(word)
    #         for letter in res:
    #             res[letter] = min(res[letter], count[letter])

    #     return list(res.elements())


    # def commonChars(self, words: List[str]) -> List[str]:
    #     dictionary = {}
    #     result = []
        
    #     for letter in words[0]:
    #         if letter not in dictionary:
    #             dictionary[letter] = 1
    #         else:
    #             dictionary[letter] += 1

    #     for index in range(1, len(words)):
    #         for letter in dictionary:
    #             if letter not in words[index]:
    #                 dictionary[letter] = 0
    #             elif dictionary[letter] > words[index].count(letter):
    #                 dictionary[letter] = words[index].count(letter)
        
    #     for letter in dictionary:
    #         result += [letter] * dictionary[letter]

    #     return result
                    
def main():
    sol = Solution()
    print(sol.commonChars(["bella", "label", "roller"]))
    print(sol.commonChars(["cool","lock","cook"]))
    print(sol.commonChars(["lllllllllllllllllllllllll", "l"]))

if __name__ == '__main__':
    main()