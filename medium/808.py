from collections import defaultdict
from functools import cache
from math import ceil

class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def helper(i: int, j: int):
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0
            
            return (
                helper(i - 4, j)
                + helper(i - 3, j - 1)
                + helper(i - 2, j - 2)
                + helper(i - 1, j - 3)
            ) * 0.25
        
        if n >= 4500:
            return 1.0
        
        n = ceil(n / 25)

        return helper(n, n)

    # def soupServings(self, n: int) -> float:
    #     def helper(i: int, j: int):
    #         if i <= 0 and j <= 0:
    #             return 0.5
    #         if i <= 0:
    #             return 1.0
    #         if j <= 0:
    #             return 0.0
    #         if i in dp and j in dp[i]:
    #             return dp[i][j]
            
    #         dp[i][j] = (
    #             helper(i - 4, j)
    #             + helper(i - 3, j - 1)
    #             + helper(i - 2, j - 2)
    #             + helper(i - 1, j - 3)
    #         ) / 4.0

    #         return dp[i][j]

    #     if n >= 4500:
    #         return 1.0

    #     m = ceil(n / 25)
    #     dp = defaultdict(dict)

    #     for k in range(1, m + 1):
    #         if helper(k, k) > 1 - 1e-5:
    #             return 1.0
        
    #     return helper(m, m)


    # def soupServings(self, n: int) -> float:
    #     if n >= 4500:
    #         return 1.0
        
    #     cache = {}
    #     def helper(a: int, b: int):
    #         if (a, b) in cache:
    #             return cache[(a, b)]
            
    #         if a <= 0 and b <= 0:
    #             return 0.5
    #         elif a <= 0:
    #             return 1.0
    #         elif b <= 0:
    #             return 0.0
            
    #         prob = (0.25) * (helper(a - 100, b) + helper(a - 75, b - 25) + helper(a - 50, b - 50) + helper(a - 25, b - 75))
    #         cache[(a, b)] = prob
    #         return cache[(a, b)]
        
    #     return helper(n, n)


def main():
    sol = Solution()
    print(sol.soupServings(50))
    print(sol.soupServings(100))

if __name__ == '__main__':
    main()