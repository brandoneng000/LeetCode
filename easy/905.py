from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     while left < len(nums) and nums[left] % 2 == 0:
        #         left += 1
        #     while right > -1 and nums[right] % 2 == 1:
        #         right -= 1

        #     if left == len(nums) or right == 0 or left > right:
        #         break

        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1

        # return nums
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1
        
        return nums

def main():
    sol = Solution()
    print(sol.sortArrayByParity([3,1,2,4]))
    print(sol.sortArrayByParity([0]))
    print(sol.sortArrayByParity([0, 2]))
    print(sol.sortArrayByParity([0, 2, 1]))

if __name__ == '__main__':
    main()