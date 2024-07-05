from typing import List

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 1000000007
        prev = -1
        res = 0

        for left, right in sorted(ranges):
            res += prev < left
            prev = max(prev, right)
        
        return pow(2, res, mod)

def main():
    sol = Solution()
    print(sol.countWays(ranges = [[6,10],[5,15]]))
    print(sol.countWays(ranges = [[1,3],[10,20],[2,5],[4,8]]))

if __name__ == '__main__':
    main()