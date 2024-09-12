class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 1000000007

        for i in range(n):
            x = 2 ** i
            
            if a * b < (a ^ x) * (b ^ x):
                a ^= x
                b ^= x
        
        return (a * b) % mod

    # def maximumXorProduct(self, a: int, b: int, n: int) -> int:
    #     mod = 1000000007

    #     for i in range(n - 1, -1, -1):
    #         mask = 1 << i

    #         if (a & mask) and (b & mask):
    #             continue
    #         elif a & mask:
    #             if a > b:
    #                 a ^= mask
    #                 b |= mask
    #         elif b & mask:
    #             if a < b:
    #                 a |= mask
    #                 b ^= mask
    #         else:
    #             a |= mask
    #             b |= mask
        
    #     a %= mod
    #     b %= mod

    #     return (a * b) % mod

        
def main():
    sol = Solution()
    print(sol.maximumXorProduct(a = 12, b = 5, n = 4))
    print(sol.maximumXorProduct(a = 6, b = 7 , n = 5))
    print(sol.maximumXorProduct(a = 1, b = 6, n = 3))

if __name__ == '__main__':
    main()