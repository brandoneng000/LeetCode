from typing import List
from collections import Counter

class DetectSquares:

    def __init__(self):
        self.coord = Counter()
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.coord[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        query_x, query_y = point
        res = 0

        for x, y in self.coord:
            if abs(query_x - x) == 0 or abs(query_x - x) != abs(query_y - y):
                continue
            res += self.coord[x, y] * self.coord[query_x, y] * self.coord[x, query_y]

        return res

        
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)