class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return s[start:end][::-1] == s[start:end] or s[start + 1: end + 1][::-1] == s[start + 1: end + 1]
            else:
                start += 1
                end -= 1
    
        return True
        
def main():
    sol = Solution()
    print(sol.validPalindrome("aba"))
    print(sol.validPalindrome("abca"))
    print(sol.validPalindrome("abc"))
    print(sol.validPalindrome("abbba"))
    print(sol.validPalindrome("abbbcda"))
    print(sol.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))

if __name__ == '__main__':
    main()