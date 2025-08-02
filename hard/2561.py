from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter()
        m = float('inf')

        for b1 in basket1:
            freq[b1] += 1
            m = min(m, b1)
        
        for b2 in basket2:
            freq[b2] -= 1
            m = min(m, b2)

        merge = []

        for k, c in freq.items():
            if c % 2 != 0:
                return -1
            merge.extend([k] * (abs(c) // 2))

        if not merge:
            return 0
        merge.sort()
        return sum(min(2 * m, x) for x in merge[: len(merge) // 2])
        
def main():
    sol = Solution()
    print(sol.minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2]))
    print(sol.minCost(basket1 = [2,3,4,1], basket2 = [3,2,5,1]))

if __name__ == '__main__':
    main()