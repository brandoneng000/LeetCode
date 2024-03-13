from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.count = defaultdict(list)

        for i, num in enumerate(arr):
            self.count[num].append(i)
        

    def query(self, left: int, right: int, value: int) -> int:        
        return bisect_right(self.count[value], right) - bisect_left(self.count[value], left) 
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)