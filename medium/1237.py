from typing import List
import bisect

#    This is the custom function interface.
#    You should not implement it, or speculate about its implementation
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass
  

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        j = 1000

        for i in range(1, 1001):
            while j > 1 and customfunction.f(i, j) > z:
                j -= 1
            if customfunction.f(i, j) == z:
                res.append([i, j])
        
        return res

    # def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    #     res = []

    #     for i in range(1, 1001):
    #         for j in range(1, 1001):
    #             if customfunction.f(i, j) == z:
    #                 res.append([i, j])
        
    #     return res