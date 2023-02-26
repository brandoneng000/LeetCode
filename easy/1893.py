from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()

        for range in ranges:
            while range[0] <= left <= range[1] and left <= right:
                left += 1

        return left > right


def main():
    sol = Solution()
    print(sol.isCovered(ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5))
    print(sol.isCovered([[1,10],[10,20]], left = 21, right = 21))

if __name__ == '__main__':
    main()