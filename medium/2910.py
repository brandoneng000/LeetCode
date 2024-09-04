from typing import List
from collections import Counter

class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        def test_size(count: Counter, size: int):
            res = 0

            for b in count:
                g, r = divmod(count[b], size)

                if r == 0:
                    res += g
                elif g >= size - r - 1:
                    res += g + 1
                else:
                    return 0
            
            return res

        n = len(balls)
        count = Counter(balls)
        min_size = min(count.values()) + 1

        for size in range(min_size, 0, -1):
            g = test_size(count, size)

            if g > 0:
                return g
            
        return n
        
def main():
    sol = Solution()
    print(sol.minGroupsForValidAssignment([1,1,3,3,1,1,2,2,3,1,3,2]))
    print(sol.minGroupsForValidAssignment([3,2,3,2,3]))
    print(sol.minGroupsForValidAssignment([10,10,10,3,1,1]))

if __name__ == '__main__':
    main()