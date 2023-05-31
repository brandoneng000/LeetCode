from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        hold, free = [0] * size, [0] * size
        hold[0] = -prices[0]
        for i in range(1, size):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
        
        return free[-1]

def main():
    sol = Solution()
    print(sol.maxProfit(prices = [1,3,2,8,4,9], fee = 2))
    print(sol.maxProfit(prices = [1,3,7,5,10,3], fee = 3))

if __name__ == '__main__':
    main()