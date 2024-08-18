from typing import List
from collections import defaultdict

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        m = defaultdict(list)

        for start, end, gold in offers:
            m[end].append([start, gold])

        for end in range(1, n + 1):
            dp[end] = dp[end - 1]

            for start, gold in m[end - 1]:
                dp[end] = max(dp[end], dp[start] + gold)

        return dp[-1]
        
def main():
    sol = Solution()
    print(sol.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]))
    print(sol.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]))

if __name__ == '__main__':
    main()