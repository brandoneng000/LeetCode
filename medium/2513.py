from math import lcm

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        left, right, g = 0, 10 ** 10, lcm(divisor1, divisor2)

        while left < right:
            middle = (left + right) // 2

            x = middle - middle // divisor1 >= uniqueCnt1
            y = middle - middle // divisor2 >= uniqueCnt2
            z = middle - middle // g >= uniqueCnt1 + uniqueCnt2

            if x and y and z:
                right = middle
            else:
                left = middle + 1
            
        return left
        
        
def main():
    sol = Solution()
    print(sol.minimizeSet(divisor1 = 16, divisor2 = 14, uniqueCnt1 = 12, uniqueCnt2 = 8))
    print(sol.minimizeSet(divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3))
    print(sol.minimizeSet(divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1))
    print(sol.minimizeSet(divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2))

if __name__ == '__main__':
    main()