from typing import List

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        res = -1

        for i in range(n - 2):
            if points[i][0] != points[i + 1][0]:
                continue

            for j in range(i + 2, n - 1):
                if points[j][1] >= points[i][1] and points[j][1] <= points[i + 1][1]:
                    if (
                        (points[j][0] > points[i][0]) 
                        and (points[j][1] == points[i][1]) 
                        and (points[j][0] == points[j + 1][0]) 
                        and (points[j + 1][1] == points[i + 1][1])
                    ):
                        res = max(res, (points[j][0] - points[i][0]) * (points[j + 1][1] - points[j][1]))
                    break

        return res

def main():
    sol = Solution()
    print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3]]))
    print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3],[2,2]]))
    print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]))

if __name__ == '__main__':
    main()