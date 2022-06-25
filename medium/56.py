from operator import itemgetter
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals, key=itemgetter(0))
        start, end = intervals[0][0], intervals[0][1]

        for index, interval in enumerate(intervals):
            if start > interval[0]:
                start = interval[0]
            
            if end >= interval[0] and end < interval[1]:
                end = interval[1]

            if end < interval[0]:
                result.append([start, end])
                start = interval[0]
                end = interval[1]

            if index == len(intervals) - 1:
                result.append([start, end])
            
        return result

def main():
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge([[1,4],[4,5]]))
    print(sol.merge([[1,4],[0,4]]))
    print(sol.merge([[1,4],[0,1]]))
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge([[1,4],[0,0]]))


if __name__ == '__main__':
    main()