class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = set(list('aeiou'))
        res = 0

        for i, c in enumerate(word):
            if c in vowels:
                res += (i + 1) * (n - i)
        
        return res

        
        
def main():
    sol = Solution()
    print(sol.countVowels("aba"))
    print(sol.countVowels("abc"))
    print(sol.countVowels("ltcd"))

if __name__ == '__main__':
    main()