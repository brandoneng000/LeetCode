class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)

        if n < 3:
            return False
        
        vowels = "aeiou"
        consonants = "qwrtypsdfghjklzxcvbnm"
        nums = "0123456789"
        found_vowel = False
        found_consonant = False

        for char in word.lower():
            if char in vowels:
                found_vowel = True
            elif char in consonants:
                found_consonant = True
            elif char in nums:
                pass
            else:
                return False
        
        return found_vowel and found_consonant

def main():
    sol = Solution()
    print(sol.isValid("234Adas"))
    print(sol.isValid("b3"))
    print(sol.isValid("a3$e"))

if __name__ == '__main__':
    main()