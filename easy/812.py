from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(first: List[int], second: List[int], third: List[int]) -> float:
            # Formula for calculating area of a triangle on a coordinate plane 
            return abs(1 / 2 * (first[0] * (second[1] - third[1]) + second[0] * (third[1] - first[1]) + third[0] * (first[1] - second[1])))
        
        area = 0
        for first_point in range(len(points) - 2):
            for second_point in range(1, len(points) - 1):
                for third_point in range(2, len(points)): 
                    area = max(area, triangleArea(points[first_point], points[second_point], points[third_point]))
        
        return area


def main():
    sol = Solution()
    print(sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
    print(sol.largestTriangleArea([[1,0],[0,0],[0,1]]))
    print(sol.largestTriangleArea([[4,6],[6,5],[3,1]]))

if __name__ == '__main__':
    main()