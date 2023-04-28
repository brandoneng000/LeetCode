from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        state_0 = [0] * len(prices)
        state_1 = [0] * len(prices)
        state_2 = [0] * len(prices)
        state_0[0] = 0
        state_1[0] = -prices[0]
        state_2[0] = -float('inf')

        for i in range(1, len(prices)):
            state_0[i] = max(state_0[i - 1], state_2[i - 1])
            state_1[i] = max(state_1[i - 1], state_0[i - 1] - prices[i])
            state_2[i] = state_1[i - 1] + prices[i]
        
        return max(state_0[len(prices) - 1], state_2[len(prices) - 1])

def main():
    sol = Solution()
    print(sol.maxProfit([1,2,3,0,2]))
    print(sol.maxProfit([1]))

if __name__ == '__main__':
    main()