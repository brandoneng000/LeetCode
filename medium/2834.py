class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 1000000007
        
        half_target = target // 2

        if n <= half_target:
            return (n * (1 + n) // 2) % mod

        res = half_target * (1 + target // 2) // 2
        n -= half_target

        return (res + (n * (target + target + n - 1) // 2)) % mod

        
def main():
    sol = Solution()
    print(sol.minimumPossibleSum(n = 2, target = 3))
    print(sol.minimumPossibleSum(n = 3, target = 3))
    print(sol.minimumPossibleSum(n = 1, target = 1))

if __name__ == '__main__':
    main()