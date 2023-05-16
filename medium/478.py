from typing import List
import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        radius = self.radius * math.sqrt(random.uniform(0, 1))
        radians = random.uniform(0, 2 * math.pi)
        x = self.x + radius * math.cos(radians)
        y = self.y + radius * math.sin(radians)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()