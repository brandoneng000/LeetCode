from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        def helper(val: int):
            left_index = bisect_left(nums, val)
            right_index = bisect_right(nums, val)
            left = right = 0

            if left_index > 0:
                left = val * left_index - prefix[left_index]

            if right_index < n:
                right = prefix[n] - prefix[right_index] - val * (n - right_index)

            return left + right
                

        n = len(nums)
        nums.sort()
        prefix = [0] + nums[::]
        res = []

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for val in queries:
            res.append(helper(val))
        
        return res

        
def main():
    sol = Solution()
    print(sol.minOperations(nums = [3,1,6,8], queries = [1,5]))
    print(sol.minOperations(nums = [2,9,6,3], queries = [10]))

if __name__ == '__main__':
    main()