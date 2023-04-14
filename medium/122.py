from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # i = 0
        # peak, valley = prices[0], prices[0]

        # while i < len(prices) - 1:
        #     while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
        #         i += 1
        #     valley = prices[i]
        #     while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
        #         i += 1
        #     peak = prices[i]
        #     profit += peak - valley
        
        # return profit
    
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit
        

def main():
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([1,2,3,4,5]))
    print(sol.maxProfit([7,6,4,3,1]))

if __name__ == '__main__':
    main()