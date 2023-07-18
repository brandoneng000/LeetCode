from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], start: int):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        swap_old = len(nums) - 2

        while swap_old >= 0 and nums[swap_old + 1] <= nums[swap_old]:
            swap_old -= 1
        
        if swap_old >= 0:
            swap_new = len(nums) - 1
            while nums[swap_new] <= nums[swap_old]:
                swap_new -= 1
            nums[swap_old], nums[swap_new] = nums[swap_new], nums[swap_old]

        reverse(nums, swap_old + 1)

def main():
    sol = Solution()
    val = [1,2,3]
    sol.nextPermutation(val)
    print(val)
    val = [3,2,1]
    sol.nextPermutation(val)
    print(val)
    val = [1,1,5]
    sol.nextPermutation(val)
    print(val)

if __name__ == '__main__':
    main()