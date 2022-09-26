class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = 0
        zeroes = 0
        cur_one = 0
        cur_zero = 0
        
        for digit in s:
            if digit == '1':
                cur_zero = 0
                cur_one += 1
                ones = max(ones, cur_one)
            else:
                cur_one = 0
                cur_zero += 1
                zeroes = max(zeroes, cur_zero)

        return ones > zeroes
        
def main():
    sol = Solution()
    print(sol.checkZeroOnes("1101"))
    print(sol.checkZeroOnes("111000"))
    print(sol.checkZeroOnes("110100010"))

if __name__ == '__main__':
    main()