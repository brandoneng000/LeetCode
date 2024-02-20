from typing import List
from collections import Counter

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = Counter()
        res = 0

        for width, height in rectangles:
            r = width / height
            res += ratio[r]
            ratio[r] += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]]))
    print(sol.interchangeableRectangles([[4,5],[7,8]]))

if __name__ == '__main__':
    main()