from typing import List
import math

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
        
        res = 0
        cache = {}

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                distance = self.distance_points(points[i], points[j])
                cache[distance] = cache.get(distance, 0) + 1
            
            for val in cache.values():
                res += val * (val - 1)
            cache.clear()
        
        return res

    def distance_points(self, p1: List[int], p2: List[int]):
        return math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2)

    # def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    #     if len(points) < 3:
    #         return 0
        
    #     res = 0
    #     for i in range(len(points)):
    #         for j in range(len(points)):
    #             if i != j:
    #                 for k in range(len(points)):
    #                     if i != j and j != k and i != k:
    #                         distance_i_j = self.distance_points(points[i][0], points[i][1], points[j][0], points[j][1])
    #                         distance_i_k = self.distance_points(points[i][0], points[i][1], points[k][0], points[k][1])
    #                         if distance_i_j == distance_i_k:
    #                             res += 1
        
    #     return res
    # def distance_points(self, x1, y1, x2, y2):
        # return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2- y1, 2))

def main():
    sol = Solution()
    print(sol.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
    print(sol.numberOfBoomerangs([[1,1],[2,2],[3,3]]))
    print(sol.numberOfBoomerangs([[1,1]]))

if __name__ == '__main__':
    main()