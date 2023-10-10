from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = sorted(set(nums))
        res = n

        for i, num in enumerate(new_nums):
            left = num
            right = left + n - 1
            j = bisect.bisect_right(new_nums, right)
            count = j - i
            res = min(res, n - count)
        
        return res


    # def minOperations(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums_set = set(nums)
    #     res = n

    #     for num in nums:
    #         start = max(1, num - n)
    #         end = start + n
    #         cur_set = set(range(start, end))
    #         for x in range(end, end + n + 2):
    #             res = min(res, len(cur_set - nums_set))
    #             cur_set.add(x)
    #             cur_set.remove(start)
    #             start += 1
            
    #         if res == 0:
    #             return 0
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.minOperations([4,2,5,3]))
    print(sol.minOperations([1,2,3,5,6]))
    print(sol.minOperations([1,10,100,1000]))

if __name__ == '__main__':
    main()