from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res, arrow = 0, 0

        for x_start, x_end in points:
            if res == 0 or x_start > arrow:
                res += 1
                arrow = x_end
        
        return res
        
        # points.sort()
        # res = [points[0]]
        
        # for x_start, x_end in points:
        #     overlap = False
        #     if res[-1][0] <= x_start <= res[-1][1] or res[-1][0] <= x_end <= res[-1][1]:
        #         overlap = True
        #         res[-1][0] = max(res[-1][0], x_start)
        #         res[-1][1] = min(res[-1][1], x_end)
        #     if not overlap:
        #         res.append([x_start, x_end])
        
        # return len(res)


def main():
    sol = Solution()
    print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
    print(sol.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))

if __name__ == '__main__':
    main()