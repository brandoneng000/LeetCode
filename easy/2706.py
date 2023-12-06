from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        lowest_price = float('inf')
        second_low = float('inf')

        for price in prices:
            if price < lowest_price:
                lowest_price, second_low = price, lowest_price
            elif price < second_low:
                second_low = price
        
        total = lowest_price + second_low
        
        return money - total if money >= total else money


    # def buyChoco(self, prices: List[int], money: int) -> int:
    #     sorted_prices = sorted(prices)
    #     total = sorted_prices[0] + sorted_prices[1]

    #     return money - total if money >= total else money
        
def main():
    sol = Solution()
    print(sol.buyChoco(prices = [1,2,2], money = 3))
    print(sol.buyChoco(prices = [3,2,3], money = 3))

if __name__ == '__main__':
    main()