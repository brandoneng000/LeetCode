from typing import List
from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        a = b = c = 0

        for s in stones:
            r = s % 3

            if r == 0:
                a += 1
            elif r == 1:
                b += 1
            else:
                c += 1

        if a % 2 == 0:
            return b > 0 and c > 0

        return abs(b - c) > 2

    # def stoneGameIX(self, stones: List[int]) -> bool:
    #     stones_count = Counter(s % 3 for s in stones)
    #     if stones_count[0] % 2 == 0:
    #         return stones_count[1] > 0 and stones_count[2] > 0
        
    #     return abs(stones_count[1] - stones_count[2]) > 2


def main():
    sol = Solution()
    print(sol.stoneGameIX([2,1]))
    print(sol.stoneGameIX([2]))
    print(sol.stoneGameIX([5,1,2,4,3]))

if __name__ == '__main__':
    main()