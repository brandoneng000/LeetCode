from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0], prices[0]] for _ in range(k + 1)]

        for day in range(1, n):
            cur_price = prices[day]

            for transaction in range(k, 0, -1):
                prev_profit = dp[transaction - 1][0]
                dp[transaction][0] = max(dp[transaction][0], dp[transaction][1] + cur_price, dp[transaction][2] - cur_price)
                dp[transaction][1] = max(dp[transaction][1], prev_profit - cur_price)
                dp[transaction][2] = max(dp[transaction][2], prev_profit + cur_price)

        return dp[k][0]
        
def main():
    sol = Solution()
    print(sol.maximumProfit(prices = [1,7,9,8,2], k = 2))
    print(sol.maximumProfit(prices = [12,16,19,19,8,1,19,13,9], k = 3))

if __name__ == '__main__':
    main()