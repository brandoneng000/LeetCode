from typing import List

class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     return min(nums)

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle
            else:
                right -= 1
        
        return nums[left]

        
def main():
    sol = Solution()
    print(sol.findMin([1,3,5]))
    print(sol.findMin([2,2,2,0,1]))
    print(sol.findMin([3,4,5,1,2]))
    print(sol.findMin([4,5,6,7,0,1,2]))
    print(sol.findMin([11,13,15,17]))
    print(sol.findMin([6, 7, 1, 2, 3, 4, 5]))

if __name__ == '__main__':
    main()