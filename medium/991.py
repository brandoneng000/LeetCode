class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
        
        return res + startValue - target


def main():
    sol = Solution()
    print(sol.brokenCalc(startValue = 2, target = 3))
    print(sol.brokenCalc(startValue = 5, target = 8))
    print(sol.brokenCalc(startValue = 3, target = 10))

if __name__ == '__main__':
    main()