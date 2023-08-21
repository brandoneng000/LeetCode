class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        dupe = s + s
        return s in dupe[1:-1]

    # def repeatedSubstringPattern(self, s: str) -> bool:
    #     sub_string = ""

    #     for letter in s:
    #         sub_string += letter
    #         if len(sub_string) > len(s) / 2:
    #             return False
    #         temp = sub_string
    #         while(len(sub_string) < len(s)):
    #             sub_string += temp
    #         if sub_string == s:
    #             return True
    #         sub_string = temp
        
    #     return False
        
def main():
    sol = Solution()
    print(sol.repeatedSubstringPattern("babbabbabbabbab"))
    print(sol.repeatedSubstringPattern("abac"))
    print(sol.repeatedSubstringPattern("abab"))
    print(sol.repeatedSubstringPattern("aba"))
    print(sol.repeatedSubstringPattern("abcabcabcabc"))

if __name__ == '__main__':
    main()