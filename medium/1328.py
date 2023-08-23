class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
            
        return palindrome[:-1] + 'b' if palindrome[:-1] else ''

    # def breakPalindrome(self, palindrome: str) -> str:
    #     if len(palindrome) == 1:
    #         return ""
        
    #     if set(palindrome) == set('a'):
    #         return palindrome[:-1] + 'b'
        
    #     flag = False
    #     for index, char in enumerate(palindrome):
    #         if char != 'a' and index != len(palindrome) // 2:
    #             return palindrome[:index] + 'a' + palindrome[index + 1:]
    #         elif char != 'a':
    #             flag = True
            
    #         if flag:
    #             return palindrome[:-1] + 'b'

def main():
    sol = Solution()
    print(sol.breakPalindrome("aba"))
    print(sol.breakPalindrome("abba"))
    print(sol.breakPalindrome("abccba"))
    print(sol.breakPalindrome("a"))

if __name__ == '__main__':
    main()