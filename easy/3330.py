class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        prev = ''
        
        for letter in word:
            if letter == prev:
                res += 1
            
            prev = letter
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.possibleStringCount("abbcccc"))
    print(sol.possibleStringCount("abcd"))
    print(sol.possibleStringCount("aaaa"))

if __name__ == '__main__':
    main()