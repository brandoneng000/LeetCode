from typing import List
import collections
import math

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        res = float('inf')
        seen = collections.defaultdict(list)
        for i, (x0, y0) in enumerate(points):
            for x1, y1 in points[i + 1:]:
                center_x = (x0 + x1) / 2
                center_y = (y0 + y1) / 2
                dist_sq = (x0 - x1) ** 2 + (y0 - y1) ** 2
                for x, y in seen.get((center_x, center_y, dist_sq), []):
                    area = math.sqrt(((x0 - x) ** 2 + (y0 - y) ** 2) * ((x1 - x) ** 2 + (y1-y) ** 2))
                    res = min(res, area)
                seen[(center_x, center_y, dist_sq)].append((x0, y0))
                
        return res if res != float('inf') else 0

def main():
    sol = Solution()
    print(sol.minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]))
    print(sol.minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]]))
    print(sol.minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]]))

if __name__ == '__main__':
    main()