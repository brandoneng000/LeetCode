from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        start, end = 0, len(nums) - 1
        middle = (end + start) // 2

        while start <= end:
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle
                while start >= 0 and nums[start] == target:
                    start -= 1
                start += 1
                
                end = middle
                while end < len(nums) and nums[end] == target:
                    end += 1
                end -= 1
                return [start, end]
            middle = (end + start) // 2

        if nums[0] == target:
            return[0, 0]

        return [-1, -1]
        
def main():
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([5,7,7,8,8,10], 6))
    print(sol.searchRange([2,2], 2))
    print(sol.searchRange([1,4], 4))

if __name__ == '__main__':
    main()