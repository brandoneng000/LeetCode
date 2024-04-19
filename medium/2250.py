from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = 101
        height = [[] for _ in range(n)]
        res = []

        for l, h in rectangles:
            height[h].append(l)
        
        for i in range(n):
            height[i].sort()
        
        for x, y in points:
            cur = 0

            for h in range(y, n):
                if len(height[h]) == 0:
                    continue
                index = bisect.bisect_left(height[h], x)
                cur += len(height[h]) - index
            
            res.append(cur)
        
        return res


    # def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
    #     grid = defaultdict(int)

    #     for l, h in rectangles:
    #         for i in range(l + 1):
    #             for j in range(h + 1):
    #                 grid[(i, j)] += 1
        
    #     return [grid[(i, j)] for i, j in points]

        
def main():
    sol = Solution()
    print(sol.countRectangles(rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]))
    print(sol.countRectangles(rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]))

if __name__ == '__main__':
    main()