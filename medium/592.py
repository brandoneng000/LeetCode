class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = []
        denominator = []
        cur_num = ""

        for i in range(len(expression) - 1, -1, -1):
            if expression[i] == "/":
                denominator.append(int(cur_num))
                cur_num = ""
            elif expression[i] == "-":
                numerator.append(-int(cur_num))
                cur_num = ""
            elif expression[i] == "+" and cur_num:
                numerator.append(int(cur_num))
                cur_num = ""
            else:
                cur_num = expression[i] + cur_num

            if i == 0 and expression[i] != '-':
                numerator.append(int(cur_num))
        
        total_num = 0
        total_denom = self.lcm(denominator)
        for i in range(len(numerator)):
            total_num += numerator[i] * (total_denom // denominator[i])
        
        if total_num == 0: return "0/1"
        divisor = self.gcd(total_num, total_denom)
        while divisor != 0 and divisor != 1:
            total_num, total_denom = total_num // divisor, total_denom // divisor
            divisor = self.gcd(total_num, total_denom)
        
        return f"{total_num}/{total_denom}"

    def lcm(self, nums: list):
        common = nums[0]
        for i in range(1, len(nums)):
            common = abs(common) * (abs(nums[i]) // self.gcd(common, nums[i]))

        return common

    def gcd(self, num1: int, num2: int):
        if num2 == 0:
            return self.gcd(num2, num1)
        if num1 == 0:
            return num2
        return self.gcd(num2, num1 % num2)


def main():
    sol = Solution()
    print(sol.fractionAddition("-1/2+1/2"))
    print(sol.fractionAddition("-1/2+1/2+1/3"))
    print(sol.fractionAddition("1/3-1/2"))

if __name__ == '__main__':
    main()