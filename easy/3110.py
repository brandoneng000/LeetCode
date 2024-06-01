class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))
        
        return res
        
def main():
    sol = Solution()
    print(sol.scoreOfString("hello"))
    print(sol.scoreOfString("zaz"))

if __name__ == '__main__':
    main()