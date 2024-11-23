from typing import List

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        n = len(points)
        coord = []

        for i in range(n):
            coord.append([max(abs(points[i][0]), abs(points[i][1])), s[i]])

        n = len(coord)
        coord.sort()
        res = set()

        for i in range(len(coord)):
            if i < n - 1 and coord[i][0] == coord[i + 1][0]:
                if coord[i][1] == coord[i + 1][1] or coord[i][1] in res or coord[i + 1][1] in res:
                    break

            if coord[i][1] in res:
                break

            res.add(coord[i][1])
            
        return len(res)


def main():
    sol = Solution()
    print(sol.maxPointsInsideSquare(points = [[-2,4],[9,3],[-9,3]], s = "cca"))
    print(sol.maxPointsInsideSquare(points = [[-1,-4],[16,-8],[13,-3],[-12,0]], s = "abda"))
    print(sol.maxPointsInsideSquare(points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"))
    print(sol.maxPointsInsideSquare(points = [[1,1],[-2,-2],[-2,2]], s = "abb"))
    print(sol.maxPointsInsideSquare(points = [[1,1],[-1,-1],[2,-2]], s = "ccd"))

if __name__ == '__main__':
    main()