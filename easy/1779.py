from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhattan_distance = float('inf')
        result = -1

        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                if abs(x - point[0]) + abs(y - point[1]) < manhattan_distance:
                    manhattan_distance = abs(x - point[0]) + abs(y - point[1])
                    result = index
            
        return result


def main():
    sol = Solution()
    print(sol.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))
    print(sol.nearestValidPoint(x = 3, y = 4, points = [[3,4]]))
    print(sol.nearestValidPoint(x = 3, y = 4, points = [[2,3]]))

if __name__ == '__main__':
    main()