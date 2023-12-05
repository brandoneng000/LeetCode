class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        string = list(s)

        for i in range(n // 2):
            if string[i] == string[n - i - 1]:
                continue
            min_letter = min(string[i], string[n - i - 1])
            string[i] = string[n - i - 1] = min_letter
        
        return "".join(string)


def main():
    sol = Solution()
    print(sol.makeSmallestPalindrome("egcfe"))
    print(sol.makeSmallestPalindrome("abcd"))
    print(sol.makeSmallestPalindrome("seven"))

if __name__ == '__main__':
    main()