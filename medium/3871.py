class Solution:
    def countCommas(self, n: int) -> int:
        thousand = max(n - (1_000 - 1), 0)
        million = max(n - (1_000_000 - 1), 0)
        billion = max(n - (1_000_000_000 - 1), 0)
        trillion = max(n - (1_000_000_000_000 - 1), 0)
        quadrillion = max(n - (1_000_000_000_000_000 - 1), 0)

        return thousand + million + billion + trillion + quadrillion


def main():
    sol = Solution()
    print(sol.countCommas(1002))
    print(sol.countCommas(998))

if __name__ == '__main__':
    main()