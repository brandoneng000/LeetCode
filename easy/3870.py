class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        return n - 999

def main():
    sol = Solution()
    print(sol.countCommas(1002))
    print(sol.countCommas(998))

if __name__ == '__main__':
    main()