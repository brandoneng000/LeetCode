from typing import List
from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones_count = Counter(s % 3 for s in stones)
        if stones_count[0] % 2 == 0:
            return stones_count[1] > 0 and stones_count[2] > 0
        
        return abs(stones_count[1] - stones_count[2]) > 2


def main():
    sol = Solution()
    print(sol.stoneGameIX([2,1]))
    print(sol.stoneGameIX([2]))
    print(sol.stoneGameIX([5,1,2,4,3]))

if __name__ == '__main__':
    main()