class Solution:
    def longestPalindrome(self, s: str) -> int:
        char = {}
        longest = 0
        odd = False

        for letter in s:
            if letter not in char:
                char[letter] = 1
            else:
                char[letter] += 1

        for val in char.values():
            if val > 2 and val % 2 == 1:
                longest += val - 1
                odd = True
            elif val % 2 == 0:
                longest += val
            
            if val % 2 == 1:
                odd = True
        
        return longest + 1 if odd else longest

        
def main():
    sol = Solution()
    print(sol.longestPalindrome("abccccdd"))
    print(sol.longestPalindrome("a"))
    print(sol.longestPalindrome("bb"))

if __name__ == '__main__':
    main()