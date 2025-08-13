class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

    # def isPowerOfThree(self, n: int) -> bool:
    #     while n % 3 == 0 and n >= 3:
    #         n //= 3

    #     return n == 1

def main():
    sol = Solution()
    print(sol.isPowerOfThree(27))
    print(sol.isPowerOfThree(0))
    print(sol.isPowerOfThree(9))
    print(sol.isPowerOfThree(-9))

if __name__ == '__main__':
    main()