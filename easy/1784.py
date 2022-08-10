class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s

def main():
    sol = Solution()
    print(sol.checkOnesSegment("1001"))
    print(sol.checkOnesSegment("110"))
    print(sol.checkOnesSegment("101010101010101010110"))
    print(sol.checkOnesSegment("10000000"))
    print(sol.checkOnesSegment("1111"))

if __name__ == '__main__':
    main()