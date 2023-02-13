from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        for index in range(len(prices)):
            for discount in range(index + 1, len(prices)):
                if prices[discount] <= prices[index]:
                    prices[index] -= prices[discount]
                    break
        
        return prices

def main():
    sol = Solution()
    print(sol.finalPrices([8,4,6,2,3]))
    print(sol.finalPrices([1,2,3,4,5]))
    print(sol.finalPrices([10,1,1,6]))

if __name__ == '__main__':
    main()