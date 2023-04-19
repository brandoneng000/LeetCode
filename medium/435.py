from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1: ]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(prev_end, end)
        
        return res
    
def main():
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(sol.eraseOverlapIntervals([[1,2],[2,3]]))
    print(sol.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
    print(sol.eraseOverlapIntervals([[-3035,30075],[1937,6906],[11834,20971],[44578,45600],[28565,37578],[19621,34415], \
                                     [32985,36313],[-8144,1080],[-15279,21851],[-27140,-14703],[-12098,16264],[-36057,-16287], \
                                     [47939,48626],[-15129,-5773],[10508,46685],[-35323,-26257]]))

if __name__ == '__main__':
    main()