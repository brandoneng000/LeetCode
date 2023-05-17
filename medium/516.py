class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def construct_palindrome(left, right):
            if (left, right) in cache:
                return cache[(left, right)]
            if left > right:
                return 0
            if left == right:
                return 1
            
            if s[left] == s[right]:
                cache[(left, right)] = construct_palindrome(left + 1, right - 1) + 2
            else:
                cache[(left, right)] = max(construct_palindrome(left + 1, right), construct_palindrome(left, right - 1))
            
            return cache[(left, right)]
        
        return construct_palindrome(0, len(s) - 1)
    
    
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     if self.is_palindrome(s):
    #         return len(s)
        
    #     self.res = 1
    #     def construct(index: int, cur_s: str):
    #         if index == len(s):
    #             if self.is_palindrome(cur_s):
    #                 self.res = max(self.res, len(cur_s))
    #             return
            
    #         construct(index + 1, cur_s)
    #         construct(index + 1, cur_s + s[index])
        
    #     construct(0, "")
    #     return self.res

    # def is_palindrome(self, s: str):
    #     return s == s[::-1]

def main():
    sol = Solution()
    print(sol.longestPalindromeSubseq("abcdabcdabcdabcd"))
    print(sol.longestPalindromeSubseq("bbbab"))
    print(sol.longestPalindromeSubseq("cbbd"))

if __name__ == '__main__':
    main()