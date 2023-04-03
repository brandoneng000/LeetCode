class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = {}
        for letter in set(s):
            if letter in letters:
                letters[letter] = True
            if letter.isupper():
                letters[letter.lower()] = False
            else:
                letters[letter.upper()] = False
        
        letters = [letter.upper() for letter in letters if letters[letter]]
        return max(letters) if letters else ""

            

def main():
    sol = Solution()
    print(sol.greatestLetter("lEeTcOdE"))
    print(sol.greatestLetter("arRAzFif"))
    print(sol.greatestLetter("AbCdEfGhIjK"))

if __name__ == '__main__':
    main()