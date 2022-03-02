class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub = 0

        for letter in t:
            if sub >= len(s):
                return True

            if s[sub] == letter:
                sub += 1

        return sub >= len(s)
        
def main():
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))

if __name__ == '__main__':
    main()