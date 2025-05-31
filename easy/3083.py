class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        reversed_str = s[::-1]
        
        for i in range(n - 1):
            if s[i:i + 2] in reversed_str:
                return True
        
        return False

        
def main():
    sol = Solution()
    print(sol.isSubstringPresent("leetcode"))
    print(sol.isSubstringPresent("abcba"))
    print(sol.isSubstringPresent("abcd"))

if __name__ == '__main__':
    main()