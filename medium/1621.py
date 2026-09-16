from math import comb

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1, 2 * k) % 1_000_000_007

    # def numberOfSets(self, n: int, k: int) -> int:
    #     mod = 1000000007
    #     res = 1

    #     for i in range(1, k * 2 + 1):
    #         res *= n + k - i
    #         res //= i
        
    #     return res % mod
        
def main():
    sol = Solution()
    print(sol.numberOfSets(n = 4, k = 2))
    print(sol.numberOfSets(n = 3, k = 1))
    print(sol.numberOfSets(n = 30, k = 7))

if __name__ == '__main__':
    main()