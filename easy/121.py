from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 100000000
        for price in prices:
            if price - buy > profit:
                profit = price - buy
            if buy > price:
                buy = price

        return profit


def main():
    sol = Solution()
    prices_one = [7,1,5,3,6,4]
    prices_two = [7,6,4,3,1]
    prices_three = [5, 100, 1, 90, 23]
    print(sol.maxProfit(prices_one))
    print(sol.maxProfit(prices_two))
    print(sol.maxProfit(prices_three))

if __name__ == '__main__':
    main()