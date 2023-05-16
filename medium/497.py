from typing import List
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rectangles = rects
        self.areas = []

        for rect in rects:
            bl_x, bl_y, tr_x, tr_y = rect
            x = tr_x - bl_x + 1
            y = tr_y - bl_y + 1
            area = x * y
            self.areas.append(area)


    def pick(self) -> List[int]:
        rect = random.choices(self.rectangles, self.areas).pop()
        bl_x, bl_y, tr_x, tr_y = rect
        x = random.randint(bl_x, tr_x)
        y = random.randint(bl_y, tr_y)
        
        return [x, y]
    
    # def __init__(self, rects: List[List[int]]):
    #     self.rectangles = rects
    #     self.areas = []

    #     for rect in rects:
    #         bl_x, bl_y, tr_x, tr_y = rect
    #         x = tr_x - bl_x + 1
    #         y = tr_y - bl_y + 1
    #         area = x * y
    #         self.areas.append(area)


    # def pick(self) -> List[int]:
    #     points = []

    #     for rect in self.rectangles:
    #         bl_x, bl_y, tr_x, tr_y = rect
    #         x = random.randint(bl_x, tr_x)
    #         y = random.randint(bl_y, tr_y)
    #         points.append([x, y])
        
    #     return random.choices(points, self.areas).pop()

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()