class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        return s[-1] + self.shortestPalindrome(s[:-1]) + s[-1]
        
def main():
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))
    print(sol.shortestPalindrome("abcd"))

if __name__ == '__main__':
    main()