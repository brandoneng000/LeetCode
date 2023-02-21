class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1

def main():
    sol = Solution()
    print(sol.numberOfMatches(7))
    print(sol.numberOfMatches(14))

if __name__ == '__main__':
    main()