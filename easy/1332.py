class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2

def main():
    sol = Solution()
    print(sol.removePalindromeSub("ababababababbabbabababbababbababbabbabbabbab"))
    print(sol.removePalindromeSub("abbaaaba"))

if __name__ == '__main__':
    main()