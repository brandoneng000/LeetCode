import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = re.sub("[^A-Za-z0-9]", '', s).lower()
        start = 0
        end = len(chars) - 1

        while start < end:
            if chars[start] != chars[end]:
                return False
            else:
                start += 1
                end -= 1
        
        return True

def main():
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))
    print(sol.isPalindrome("0P"))

if __name__ == '__main__':
    main()