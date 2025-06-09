class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = 0
        temp = x

        while temp:
            temp, r = divmod(temp, 10)
            sum_digits += r
        
        return sum_digits if x % sum_digits == 0 else -1
        
def main():
    sol = Solution()
    print(sol.sumOfTheDigitsOfHarshadNumber(18))
    print(sol.sumOfTheDigitsOfHarshadNumber(23))

if __name__ == '__main__':
    main()