from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        
        return -1

def main():
    sol = Solution()
    print(sol.search(nums = [-1,0,3,5,9,12], target = 9))
    print(sol.search(nums = [-1,0,3,5,9,12], target = 2))
    print(sol.search(nums = [5], target = 5))

if __name__ == '__main__':
    main()