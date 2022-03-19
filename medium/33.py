from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle

            if nums[start] <= nums[middle]:
                if nums[start] <= target <= nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if nums[middle] <= target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1

        return -1
    
def main():
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))

if __name__ == '__main__':
    main()