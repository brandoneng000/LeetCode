from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[right] < nums[left]:
                if nums[left] < nums[middle]:
                    left = middle
                elif nums[left] > nums[middle]:
                    right = middle
                if right - left == 1:
                    return min(nums[left], nums[right])
            else:
                return nums[left]
        
        return nums[middle]
        
def main():
    sol = Solution()
    print(sol.findMin([3,4,5,1,2]))
    print(sol.findMin([4,5,6,7,0,1,2]))
    print(sol.findMin([11,13,15,17]))
    print(sol.findMin([6, 7, 1, 2, 3, 4, 5]))

if __name__ == '__main__':
    main()