from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}
        for index, letter in enumerate(order):
            dictionary[letter] = index

        for word in range(len(words) - 1):
            for letter in range(len(words[word])):
                if letter >= len(words[word + 1]):
                    return False
                if words[word][letter] != words[word + 1][letter]:
                    if dictionary[words[word][letter]] > dictionary[words[word + 1][letter]]:
                        return False
                    break

        return True
        
        
def main():
    sol = Solution()
    print(sol.isAlienSorted(
        ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
    ))
    print(sol.isAlienSorted(
        ["word","world","row"], "worldabcefghijkmnpqstuvxyz"
    ))
    print(sol.isAlienSorted(
        ["apple","app"], "abcdefghijklmnopqrstuvwxyz"
    ))
    print(sol.isAlienSorted(
        ["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"
    ))

if __name__ == '__main__':
    main()