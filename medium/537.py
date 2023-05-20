import re

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = self.get_nums(num1)
        r2, i2 = self.get_nums(num2)
        real_res = r1 * r2 + -(i1 * i2)
        imaginary_res = r1 * i2 + r2 * i1
        return f"{real_res}+{imaginary_res}i"


    def get_nums(self, nums: str) -> tuple:
        num = [int(n) for n in re.findall(r'(\d+)', nums)]
        if nums[0] == '-':
            num[0] *= -1
        
        if nums[1:].count('-') == 1:
            num[1] *= -1
        return num


def main():
    sol = Solution()
    print(sol.complexNumberMultiply(num1 = "1+1i", num2 = "1+15i"))
    print(sol.complexNumberMultiply(num1 = "1+1i", num2 = "1+1i"))
    print(sol.complexNumberMultiply(num1 = "1+-1i", num2 = "1+-1i"))
    print(sol.complexNumberMultiply(num1 = "1--1i", num2 = "1-1i"))

if __name__ == '__main__':
    main()