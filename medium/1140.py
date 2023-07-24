from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        cache = {}

        def helper(player: int, index: int, m: int):
            if index == n:
                return 0
            if (player, index, m) in cache:
                return cache[(player, index, m)]
            
            res = float('inf') if player == 1 else -1
            s = 0
            for x in range(1, min(2 * m, n - index) + 1):
                s += piles[index + x - 1]
                if player == 0:
                    res = max(res, s + helper(1, index + x, max(m, x)))
                else:
                    res = min(res, helper(0, index + x, max(m, x)))
            cache[((player, index, m))] = res
            return res
        
        return helper(0, 0, 1)



def main():
    sol = Solution()
    print(sol.stoneGameII([2,7,9,4,4]))
    print(sol.stoneGameII([1,2,3,4,5,100]))

if __name__ == '__main__':
    main()