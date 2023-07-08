from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        n = max(days_set)
        DAY, WEEK, MONTH = 0, 1, 2
        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i not in days_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[DAY], dp[max(0, i - 7)] + costs[WEEK], dp[max(0, i - 30)] + costs[MONTH])
        
        return dp[n]
            
def main():
    sol = Solution()
    print(sol.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
    print(sol.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))

if __name__ == '__main__':
    main()