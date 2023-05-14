
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        prev = s[0]
        cache = { s[0]: 1 }
        streak = 1
        for letter in s[1:]:
            if (26 + ord(letter) - ord(prev)) % 26 == 1:
                streak += 1
            else:
                streak = 1
            cache[letter] = max(cache.get(letter, 0), streak)
            prev = letter
        
        return sum(cache.values())
    
def main():
    sol = Solution()
    print(sol.findSubstringInWraproundString('abczbcde'))
    print(sol.findSubstringInWraproundString('a'))
    print(sol.findSubstringInWraproundString("cac"))
    print(sol.findSubstringInWraproundString("zab"))

if __name__ == '__main__':
    main()