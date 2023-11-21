from typing import List
from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num: int):
            return int(str(num)[::-1])

        mod = 1000000007
        arr = []
        diff_nums = Counter()
        res = 0

        for n in nums:
            arr.append(n - rev(n))
        
        for n in arr:
            res = (res + diff_nums[n]) % mod
            diff_nums[n] += 1
        
        return res
    
    # def countNicePairs(self, nums: List[int]) -> int:
    #     def rev(num: int):
    #         return int(str(num)[::-1])

    #     mod = 1000000007
    #     diff_nums = Counter()
    #     res = 0

    #     for n in nums:
    #         diff_nums[n - rev(n)] += 1
        
    #     for diff in diff_nums:
    #         res += diff_nums[diff] * (diff_nums[diff] - 1)
        
    #     return res // 2 % mod
        
def main():
    sol = Solution()
    print(sol.countNicePairs([42,11,1,97]))
    print(sol.countNicePairs([13,10,35,24,76]))

if __name__ == '__main__':
    main()