from typing import List
from collections import defaultdict, Counter
from math import comb, gcd
from itertools import combinations

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slopes = Counter()
        colinear = Counter()
        midpoints = Counter()
        colinear_midpoints = Counter()

        for (x1, y1), (x2, y2) in combinations(points, 2):
            dx = x2 - x1
            dy = y2 - y1

            g = gcd(dx, dy)

            dx = dx // g
            dy = dy // g

            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            
            b = y1 * dx - dy * x1

            slopes[(dx, dy)] += 1
            colinear[(dx, dy, b)] += 1
            midpoints[(x1 + x2, y1 + y2)] += 1
            colinear_midpoints[(x1 + x2, y1 + y2, dx, dy)] += 1

        res = 0

        res += sum(comb(count, 2) for count in slopes.values())
        res -= sum(comb(count, 2) for count in colinear.values())
        res -= sum(comb(count, 2) for count in midpoints.values())
        res += sum(comb(count, 2) for count in colinear_midpoints.values())

        return res
        
        

    # def countTrapezoids(self, points: List[List[int]]) -> int:
    #     n = len(points)
    #     slopes_intercept = defaultdict(list)
    #     slopes_mid = defaultdict(list)
    #     res = 0

    #     for i in range(n):
    #         x1, y1 = points[i]

    #         for j in range(i + 1, n):
    #             x2, y2 = points[j]
    #             dx = x1 - x2
    #             dy = y1 - y2

    #             if x2 == x1:
    #                 k = float('inf')
    #                 b = x1
    #             else:
    #                 k = (y2 - y1) / (x2 - x1)
    #                 b = (y1 * dx - x1 * dy) / dx
                
    #             mid = (x1 + x2) * 10000 + (y1 + y2)
    #             slopes_intercept[k].append(b)
    #             slopes_mid[mid].append(k)

    #     for s in slopes_intercept.values():
    #         if len(s) == 1:
    #             continue

    #         count = defaultdict(int)

    #         for b_val in s:
    #             count[b_val] += 1
            
    #         total_sum = 0

    #         for c in count.values():
    #             res += total_sum * c
    #             total_sum += c
        
    #     for m in slopes_mid.values():
    #         if len(m) == 1:
    #             continue

    #         count = defaultdict(int)

    #         for k_val in m:
    #             count[k_val] += 1
            
    #         total_sum = 0
    #         for c in count.values():
    #             res -= total_sum * c
    #             total_sum += c
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.countTrapezoids([[83,-25],[74,11],[-65,-25],[33,-25],[17,-25],[1,30],[-84,-25],[1,-25],[1,-92],[-87,13]]))
    print(sol.countTrapezoids([[71,-89],[-75,-89],[-9,11],[-24,-89],[-51,-89],[-77,-89],[42,11]]))
    print(sol.countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]]))
    print(sol.countTrapezoids([[0,0],[1,0],[0,1],[2,1]]))

if __name__ == '__main__':
    main()