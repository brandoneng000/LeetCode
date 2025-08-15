class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n == (n & -n) and (n - 1) % 3 == 0

    # def isPowerOfFour(self, n: int) -> bool:
    #     # 01010101010101010101010101010101
    #     check = n & 0b01010101010101010101010101010101 == n
    #     only_one = n & n - 1 == 0
    #     return n > 0 and check and only_one

def main():
    sol = Solution()
    print(sol.isPowerOfFour(16))
    print(sol.isPowerOfFour(5))
    print(sol.isPowerOfFour(1))
    print(sol.isPowerOfFour(1431655765))

if __name__ == '__main__':
    main()