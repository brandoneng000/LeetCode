from string import ascii_uppercase

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0

        for letter in ascii_uppercase:
            first_upper = 0
            last_lower = 0

            if letter in word:
                first_upper = word.find(letter)
                lower_letter = letter.lower()

                if lower_letter in word:
                    last_lower = word.rfind(lower_letter)

                    if first_upper > last_lower:
                        res += 1
        
        return res


    # def numberOfSpecialChars(self, word: str) -> int:
    #     n = len(word)
    #     last_index = {}
    #     first_index = {}
    #     res = 0

    #     for i in range(n):
    #         if word[i] not in first_index:
    #             first_index[word[i]] = i

    #         last_index[word[i]] = i
        
    #     for letter in set(word.lower()):
    #         if last_index.get(letter, float('inf')) < first_index.get(letter.upper(), -1):
    #             res += 1
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.numberOfSpecialChars("aaAbcBC"))
    print(sol.numberOfSpecialChars("abc"))
    print(sol.numberOfSpecialChars("AbBCab"))

if __name__ == '__main__':
    main()