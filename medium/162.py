from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                right = middle
            else:
                left = middle + 1
        
        return left

def main():
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1]))
    print(sol.findPeakElement([1,2,1,3,5,6,4]))

if __name__ == '__main__':
    main()