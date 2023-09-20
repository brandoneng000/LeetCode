from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target == 0:
            return n
        
        max_length = 0
        left = 0
        cur_sum = 0

        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum == target:
                max_length = max(max_length, right - left + 1)
        
        return n - max_length if max_length else -1
        
def main():
    sol = Solution()
    print(sol.minOperations(nums = [1,1,4,2,3], x = 5))
    print(sol.minOperations(nums = [5,6,7,8,9], x = 4))
    print(sol.minOperations(nums = [3,2,20,1,1,3], x = 10))

if __name__ == '__main__':
    main()