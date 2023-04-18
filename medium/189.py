from typing import List
import collections

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # while k:
        #     k -= 1
        #     val = nums.pop()
        #     nums.insert(0, val)

        def reverse(nums: List[int], start: int, end: int):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        
        k %= len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


def main():
    sol = Solution()
    nums, k = [1,2,3,4,5,6,7], 3
    sol.rotate(nums, k)
    print(nums)
    nums, k = [-1,-100,3,99], 2
    sol.rotate(nums, k)
    print(nums)

if __name__ == '__main__':
    main()