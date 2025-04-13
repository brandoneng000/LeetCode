class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        return pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod) % mod

    # def countGoodNumbers(self, n: int) -> int:
    #     mod = 1000000007
    #     res = 5 ** (n % 2)
    #     x = 20
    #     i = n // 2

    #     while i > 0:
    #         if i % 2 == 1:
    #             res = res * x % mod
    #         x = x * x % mod
    #         i //= 2
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.countGoodNumbers(1))
    print(sol.countGoodNumbers(4))
    print(sol.countGoodNumbers(50))

if __name__ == '__main__':
    main()