from typing import List

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        max_prod = 1
        remainder = n % 3
        num_list = [3] * (n // 3)
        if remainder == 1:
            num_list[-1] += remainder
        elif remainder == 2:
            num_list.append(remainder)

        for n in num_list:
            max_prod *= n

        return max_prod


def main():
    sol = Solution()
    print(sol.integerBreak(2))
    print(sol.integerBreak(4))
    print(sol.integerBreak(10))

if __name__ == '__main__':
    main()