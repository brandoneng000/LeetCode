from math import gcd

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for step in range(61):
            target = num1 - num2 * step

            if target >= 0 and target.bit_count() <= step <= target:
                return step
        
        return -1

    # def makeTheIntegerZero(self, num1: int, num2: int) -> int:
    #     if num1 < num2:
    #         return -1
        
    #     for steps in range(61):
    #         diff = num1 - num2 * steps
    #         bits = bin(diff).count('1')

    #         if bits <= steps and steps <= diff:
    #             return steps
        
    #     return -1

        
def main():
    sol = Solution()
    print(sol.makeTheIntegerZero(num1 = 3, num2 = -2))
    print(sol.makeTheIntegerZero(num1 = 5, num2 = 7))

if __name__ == '__main__':
    main()