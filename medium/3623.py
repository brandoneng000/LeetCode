from typing import List
from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 1_000_000_007
        same_y_level = Counter()
        total = 0
        res = 0
        
        for x, y in points:
            same_y_level[y] += 1

        for y in same_y_level.values():
            edge = y * (y - 1) // 2
            res = (res + edge * total) % mod
            total = (total + edge) % mod
        
        return res

        
def main():
    sol = Solution()
    print(sol.countTrapezoids([[1,0],[2,0],[3,0],[4,0],[2,2],[3,2]]))
    print(sol.countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]]))
    print(sol.countTrapezoids([[0,0],[1,0],[0,1],[2,1]]))

if __name__ == '__main__':
    main()