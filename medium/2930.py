class Solution:
    def stringCount(self, n: int) -> int:
        if n < 4:
            return 0

        mod = 1000000007

        res = pow(26, n, mod)

        # l = 0
        sub = pow(25, n, mod)

        # t = 0
        sub += pow(25, n, mod)

        # e = 0 and e = 1
        sub += (pow(25, n, mod) + n * pow(25, n - 1, mod)) % mod

        # l = 0 and t = 0
        sub -= pow(24, n, mod)

        # l = 0 and e < 2
        sub -= (pow(24, n, mod) + n * pow(24, n - 1, mod)) % mod

        # t = 0 and e < 2
        sub -= (pow(24, n, mod) + n * pow(24, n - 1, mod)) % mod

        # t = 0 and l = 0 and e < 2
        sub += (pow(23, n, mod) + n * pow(23, n - 1, mod)) % mod


        return (res - sub) % mod


def main():
    sol = Solution()
    print(sol.stringCount(4))
    print(sol.stringCount(10))

if __name__ == '__main__':
    main()