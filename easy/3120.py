from collections import Counter

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        visited = set()
        res = 0

        for letter in word_set:
            if letter.upper() in word_set and letter.lower() in word_set and letter not in visited:
                res += 1
                visited.add(letter.upper())
                visited.add(letter.lower())
        
        return res
        

    # def numberOfSpecialChars(self, word: str) -> int:
    #     count = Counter(word)
    #     res = 0

    #     for letter in set(word.lower()):
    #         if count[letter] > 0 and count[letter.upper()] > 0:
    #             res += 1
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.numberOfSpecialChars("aaAbcBC"))
    print(sol.numberOfSpecialChars("abc"))
    print(sol.numberOfSpecialChars("abBCab"))

if __name__ == '__main__':
    main()