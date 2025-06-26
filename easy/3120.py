from collections import Counter

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = Counter(word)
        res = 0

        for letter in set(word.lower()):
            if count[letter] > 0 and count[letter.upper()] > 0:
                res += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.numberOfSpecialChars("aaAbcBC"))
    print(sol.numberOfSpecialChars("abc"))
    print(sol.numberOfSpecialChars("abBCab"))

if __name__ == '__main__':
    main()