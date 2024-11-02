from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        cur_start = -1
        cur_end = -1
        res = 0

        for x, y in points:
            if cur_start <= x <= cur_end:
                continue
            else:
                res += 1
                cur_start = x
                cur_end = x + w
        
        return res
        
def main():
    sol = Solution()
    print(sol.minRectanglesToCoverPoints(points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1))
    print(sol.minRectanglesToCoverPoints(points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2))
    print(sol.minRectanglesToCoverPoints(points = [[2,3],[1,2]], w = 0))

if __name__ == '__main__':
    main()