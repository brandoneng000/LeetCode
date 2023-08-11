from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res, right = 0, 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        for i, j in intervals:
            res += j > right
            right = max(right, j)

        return res

    # def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key=lambda x: (x[0], -x[1]))
    #     overlap = set()

    #     for i in range(len(intervals)):
    #         for j in range(i + 1, len(intervals)):
    #             if intervals[i][0] <= intervals[j][0] and intervals[j][1] <= intervals[i][1] and j not in overlap:
    #                 overlap.add(j)
    #             else:
    #                 break
        
    #     return len(intervals) - len(overlap)

def main():
    sol = Solution()
    print(sol.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
    print(sol.removeCoveredIntervals([[1,4],[2,3]]))

if __name__ == '__main__':
    main()