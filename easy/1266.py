from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        for i in range(n - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            time = max(abs(x2 - x1), abs(y2 - y1))

            res += time

        return res


    # def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    #     x, y = points.pop(0)
    #     result = 0

    #     for point in points:
    #         large_x = max(point[0], x)
    #         large_y = max(point[1], y)
    #         small_x = min(point[0], x)
    #         small_y = min(point[1], y)
    #         diag = min(large_x - small_x, large_y - small_y)
    #         straight = max(large_x - (small_x + diag), large_y - (small_y + diag))
    #         result += diag + straight
    #         x, y = point
        
    #     return result
    
    # def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    #     result = 0

    #     for index in range(1, len(points)):
    #         straight = max(abs(points[index - 1][0] - points[index][0]), abs(points[index - 1][1] - points[index][1]))
    #         result += straight
        
    #     return result

def main():
    sol = Solution()
    print(sol.minTimeToVisitAllPoints([[1,1],[0, 0]]))
    print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
    print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))

if __name__ == '__main__':
    main()