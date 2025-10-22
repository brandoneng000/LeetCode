from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        def add_mode(x: int):
            modes.add(x)

            if x - k >= nums[0]:
                modes.add(x - k)
            
            if x + k <= nums[-1]:
                modes.add(x + k)

        n = len(nums)
        nums.sort()
        res = 0
        count = defaultdict(int)
        modes = set()
        last_num_index = 0

        for i in range(n):
            if nums[i] != nums[last_num_index]:
                count[nums[last_num_index]] = i - last_num_index
                res = max(res, i - last_num_index)
                add_mode(nums[last_num_index])
                last_num_index = i
        
        count[nums[last_num_index]] = n - last_num_index
        res = max(res, n - last_num_index)
        add_mode(nums[last_num_index])


        for i in sorted(modes):
            l = bisect_left(nums, i - k)
            r = bisect_right(nums, i + k) - 1

            if i in count:
                temp = min(r - l + 1, count[i] + numOperations)
            else:
                temp = min(r - l + 1, numOperations)
            
            res = max(res, temp)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxFrequency(nums = [1,4,5], k = 1, numOperations = 2))
    print(sol.maxFrequency(nums = [5,11,20,20], k = 5, numOperations = 1))

if __name__ == '__main__':
    main()