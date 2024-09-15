from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        n = len(coins)
        coins.sort()
        res = cur = 0
        i = 0

        while cur < target:
            if i < n and coins[i] <= cur + 1:
                cur += coins[i]
                i += 1
            else:
                cur += cur + 1
                res += 1
        
        return res


    # def minimumAddedCoins(self, coins: List[int], target: int) -> int:
    #     goal = set(range(1, target + 1))
    #     cur = set()
    #     res = 0

    #     for num in coins:
    #         next = set()
    #         for val in cur:
    #             if val + num <= target:
    #                 next.add(val + num)
            
    #         cur.update(next)
    #         cur.add(num)

    #     while len(cur) < len(goal):
    #         num = min(goal - cur)
    #         next = set()

    #         for val in cur:
    #             if val + num <= target:
    #                 next.add(val + num)
            
    #         cur.update(next)
    #         cur.add(num)
    #         res += 1
        
    #     return res
            
        
def main():
    sol = Solution()
    print(sol.minimumAddedCoins(coins = [1,4,10], target = 19))
    print(sol.minimumAddedCoins(coins = [1,4,10,5,7,19], target = 19))
    print(sol.minimumAddedCoins(coins = [1,1,1], target = 20))

if __name__ == '__main__':
    main()