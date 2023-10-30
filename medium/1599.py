from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ridden = 0
        waiting = 0
        max_profit = 0
        res = -1

        for runs, cust in enumerate(customers, 1):
            ridden += min(cust + waiting, 4)
            waiting = max(cust + waiting - 4, 0)
            cur_profit = ridden * boardingCost - runs * runningCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                res = runs

        while waiting > 0:
            ridden += min(waiting, 4)
            waiting -= 4
            runs += 1
            cur_profit = ridden * boardingCost - runs * runningCost

            if cur_profit > max_profit:
                max_profit = cur_profit
                res = runs

        return res


        
def main():
    sol = Solution()
    print(sol.minOperationsMaxProfit(customers = [8,3], boardingCost = 5, runningCost = 6))
    print(sol.minOperationsMaxProfit(customers = [10,9,6], boardingCost = 6, runningCost = 4))
    print(sol.minOperationsMaxProfit(customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92))

if __name__ == '__main__':
    main()