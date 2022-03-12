class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_center(s: str, left: int, right: int) -> int:
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return right - left - 1
        
        if not s:
            return ""
        
        start, end = 0, 0

        for index in range(len(s)):
            len_one = expand_center(s, index, index)
            len_two = expand_center(s, index, index + 1)
            length = max(len_one, len_two)
            if length > end - start:
                start = index - (length - 1) // 2
                end = index + length // 2

        return s[start: end + 1]
            
        
def main():
    sol = Solution()
    print(sol.longestPalindrome("aacabdkacaa"))
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbd"))

if __name__ == '__main__':
    main()