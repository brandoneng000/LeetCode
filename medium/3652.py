from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        profit_sum = [0] * (n + 1)
        price_sum = [0] * (n + 1)

        for i in range(n):
            profit_sum[i + 1] = profit_sum[i] + prices[i] * strategy[i]
            price_sum[i + 1] = price_sum[i] + prices[i]
        
        res = profit_sum[n]

        for i in range(k - 1, n):
            left_profit = profit_sum[i - k + 1]
            right_profit = profit_sum[n] - profit_sum[i + 1]
            change_profit = price_sum[i + 1] - price_sum[i - k // 2 + 1]
            res = max(res, left_profit + change_profit + right_profit)
        
        return res


def main():
    sol = Solution()
    print(sol.maxProfit(prices = [4,2,8], strategy = [-1,0,1], k = 2))
    print(sol.maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2))

if __name__ == '__main__':
    main()