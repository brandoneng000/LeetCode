from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        def dp(index: int):
            if index >= n:
                return 0
            
            if index in cache:
                return cache[index]
            
            res = float('inf')

            for i in range(index + 1, 2 * index + 3):
                res = min(res, dp(i))

            cache[index] = prices[index] + res
            return cache[index]

        n = len(prices)
        cache = {}

        return dp(0)

        
def main():
    sol = Solution()
    print(sol.minimumCoins([3,1,2]))
    print(sol.minimumCoins([1,10,1,1]))
    print(sol.minimumCoins([26,18,6,12,49,7,45,45]))

if __name__ == '__main__':
    main()