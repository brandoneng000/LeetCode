from typing import List
from collections import Counter
from bisect import bisect_left

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        def found(length: int):
            k = length.bit_length() - 1
            return 1 in Counter(zip(names[k], names[k][length - 2 ** k:])).values()

        n = len(nums)
        names = [nums]

        for k in range(n.bit_length() - 1):
            ids = {}
            names.append([ids.setdefault(pair, len(ids)) for pair in zip(names[k], names[k][2 ** k:])])

        return bisect_left(range(1, n), True, key=found) + 1

def main():
    sol = Solution()
    print(sol.smallestUniqueSubarray([3,3,3]))
    print(sol.smallestUniqueSubarray([2,1,2,3,3]))
    print(sol.smallestUniqueSubarray([1,1,2,2,1]))

if __name__ == '__main__':
    main()