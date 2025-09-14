class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)

        for i in range(n - 1):
            if int(s[i]) % 2 == int(s[i + 1]) % 2 and s[i] > s[i + 1]:
                return s[:i] + s[i + 1] + s[i] + s[i + 2:]

        return s
        
def main():
    sol = Solution()
    print(sol.getSmallestString("45320"))
    print(sol.getSmallestString("001"))

if __name__ == '__main__':
    main()