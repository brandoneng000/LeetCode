class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        empty_bottles = 0

        while numBottles:
            drank += numBottles
            empty_bottles += numBottles
            extra_bottles = empty_bottles % numExchange
            numBottles = empty_bottles // numExchange
            empty_bottles = extra_bottles
        
        return drank

def main():
    sol = Solution()
    print(sol.numWaterBottles(9, 3))
    print(sol.numWaterBottles(15, 4))

if __name__ == '__main__':
    main()