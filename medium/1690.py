from typing import List
from functools import lru_cache

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        def get_sum(left: int, right: int):
            return prefix[right + 1] - prefix[left]
        
        n = len(stones)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(2000)
        def dp(left: int, right: int, alice_turn: bool):
            if left == right:
                return 0
            
            if alice_turn:
                a = dp(left + 1, right, not alice_turn) + get_sum(left + 1, right)
                b = dp(left, right - 1, not alice_turn) + get_sum(left, right - 1)
                return max(a, b)
            else:
                a = dp(left + 1, right, not alice_turn) - get_sum(left + 1, right)
                b = dp(left, right - 1, not alice_turn) - get_sum(left, right - 1)
                return min(a, b)
        
        return dp(0, n - 1, True)

        
def main():
    sol = Solution()
    print(sol.stoneGameVII([5,3,1,4,2]))
    print(sol.stoneGameVII([7,90,5,1,100,10,10,2]))

if __name__ == '__main__':
    main()