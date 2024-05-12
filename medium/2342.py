from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = {}
        res = -1

        for num in nums:
            temp = num
            digit_sum = 0

            while temp:
                digit_sum += temp % 10
                temp //= 10
            
            if digit_sum in digits:
                res = max(res, digits[digit_sum] + num)

            digits[digit_sum] = max(digits.get(digit_sum, 0), num)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumSum([18,43,36,13,7]))
    print(sol.maximumSum([10,12,19,14]))

if __name__ == '__main__':
    main()