class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1_000_000_007
        a = b = 6

        for _ in range(2, n + 1):
            a, b = (2 * a + 2 * b) % mod, (2 * a + 3 * b) % mod

        return (a + b) % mod
        
def main():
    sol = Solution()
    print(sol.numOfWays(1))
    print(sol.numOfWays(5000))

if __name__ == '__main__':
    main()