from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        
        return False


def main():
    sol = Solution()
    print(sol.search(nums = [2,5,6,0,0,1,2], target = 0))
    print(sol.search(nums = [2,5,6,0,0,1,2], target = 3))
    print(sol.search(nums = [2,5,6,0,0,1,2], target = 5))
    print(sol.search(nums = [1,0,1,1,1], target = 0))
    print(sol.search(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2))

if __name__ == '__main__':
    main()