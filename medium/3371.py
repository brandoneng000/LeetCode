from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        res = -10 ** 33

        for num in nums:
            outlier = total - num - num
            if count[outlier] > (outlier == num):
                res = max(res, outlier)

        return res

def main():
    sol = Solution()
    print(sol.getLargestOutlier([2,3,5,10]))
    print(sol.getLargestOutlier([-2,-1,-3,-6,4]))
    print(sol.getLargestOutlier([1,1,1,1,1,5,5]))

if __name__ == '__main__':
    main()