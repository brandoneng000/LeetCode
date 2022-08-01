class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowel(s: str) -> dict:
            count = 0
            
            for letter in s:
                if letter in 'aeiouAEIOU':
                    count += 1
            
            return count
        
        s1 = s[: len(s) // 2]
        s2 = s[len(s) // 2:]

        return count_vowel(s1) == count_vowel(s2)

def main():
    sol = Solution()
    print(sol.halvesAreAlike("book"))
    print(sol.halvesAreAlike("textbook"))
    print(sol.halvesAreAlike("BOOK"))
    print(sol.halvesAreAlike("AbCdEfGh"))

if __name__ == '__main__':
    main()