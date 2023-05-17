from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]

    # def change(self, amount: int, coins: List[int]) -> int:
        # self.res = set()
        # def helper(cur: List[int]):
        #     if sum(cur) == amount:
        #         self.res.add(tuple(sorted(cur)))
        #     if sum(cur) > amount:
        #         return
            
        #     for i in range(len(coins)):
        #         cur.append(coins[i])
        #         helper(cur)
        #         cur.pop()
        
        # helper([])
        # return len(self.res)
            
def main():
    sol = Solution()
    print(sol.change(amount = 5, coins = [1,2,5]))
    print(sol.change(amount = 3, coins = [2]))
    print(sol.change(amount = 10, coins = [10]))

if __name__ == '__main__':
    main()