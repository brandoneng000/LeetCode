class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        alternate = 1

        while n:
            res += n % 10 * alternate
            alternate = -alternate
            n //= 10
        
        return res * -alternate


def main():
    sol = Solution()
    print(sol.alternateDigitSum(521))
    print(sol.alternateDigitSum(111))
    print(sol.alternateDigitSum(886996))
    print(sol.alternateDigitSum(9989))

if __name__ == '__main__':
    main()