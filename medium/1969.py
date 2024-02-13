class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 1000000007
        right = pow(2, p) - 1

        return right * pow(right - 1, right // 2, mod) % mod
        
def main():
    sol = Solution()
    print(sol.minNonZeroProduct(1))
    print(sol.minNonZeroProduct(2))
    print(sol.minNonZeroProduct(3))

if __name__ == '__main__':
    main()