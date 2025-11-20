from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        todo = [2] * (n)
        res = 0

        while intervals:
            start, end = intervals.pop()
            t = todo.pop()

            for p in range(start, start + t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                res += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.intersectionSizeTwo(intervals = [[1,3],[3,7],[8,9]]))
    print(sol.intersectionSizeTwo(intervals = [[1,3],[1,4],[2,5],[3,5]]))
    print(sol.intersectionSizeTwo(intervals = [[1,2],[2,3],[2,4],[4,5]]))

if __name__ == '__main__':
    main()