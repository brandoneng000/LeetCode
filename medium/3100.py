from math import sqrt, ceil

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles

        delta = b * b - 4 * a * c
        t = ceil((-b + sqrt(delta)) / (2 * a))
        
        return numBottles + t - 1

    # def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    #     res = 0
    #     empty = 0

    #     while numBottles:
    #         res += numBottles
    #         empty += numBottles
    #         numBottles = 0

    #         while empty >= numExchange:
    #             numBottles += 1
    #             empty -= numExchange
    #             numExchange += 1
            
    #     return res

        
def main():
    sol = Solution()
    print(sol.maxBottlesDrunk(numBottles = 13, numExchange = 6))
    print(sol.maxBottlesDrunk(numBottles = 10, numExchange = 3))

if __name__ == '__main__':
    main()