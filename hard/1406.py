from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def max_diff(i: int):
            if i == n:
                return 0
            if i in dp:
                return dp[i]

            a = b = c = -INF

            if i < n:
                a = stoneValue[i] - max_diff(i + 1)
            if i + 1 < n:
                b = stoneValue[i] + stoneValue[i + 1] - max_diff(i + 2)
            if i + 2 < n:
                c = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - max_diff(i + 3)

            dp[i] = max(a, b, c)
            return dp[i]

        n = len(stoneValue)
        INF = 10 ** 33
        dp = {}
        d = max_diff(0)

        if d > 0:
            return "Alice"
        elif d < 0:
            return "Bob"
        else:
            return "Tie"


def main():
    sol = Solution()
    print(sol.stoneGameIII([1,2,3,7]))
    print(sol.stoneGameIII([1,2,3,-9]))
    print(sol.stoneGameIII([1,2,3,6]))

if __name__ == '__main__':
    main()