from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            while rides and i == rides[-1][0]:
                start, end, tip = rides.pop()
                dp[i] = max(dp[i], dp[end] + end - start + tip)
        
        return dp[0]
        
def main():
    sol = Solution()
    print(sol.maxTaxiEarnings(n = 5, rides = [[2,5,4],[1,5,1]]))
    print(sol.maxTaxiEarnings(n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]))

if __name__ == '__main__':
    main()