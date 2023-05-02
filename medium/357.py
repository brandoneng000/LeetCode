from typing import List

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # res = 1

        # for i in range(1, n + 1):
        #     val = 9
        #     for i in range(9, 10 - i, -1):
        #         val *= i
        #     res += val
        
        # return res
        if n == 0:
            return 1
        
        res = 10
        unique_digit = 9
        available_digits = 9
        while n > 1 and available_digits > 0:
            unique_digit *= available_digits
            res += unique_digit
            n -= 1
            available_digits -= 1
        
        return res

def main():
    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(0))
    print(sol.countNumbersWithUniqueDigits(1))
    print(sol.countNumbersWithUniqueDigits(2))
    print(sol.countNumbersWithUniqueDigits(3))
    print(sol.countNumbersWithUniqueDigits(4))
    print(sol.countNumbersWithUniqueDigits(5))

if __name__ == '__main__':
    main()