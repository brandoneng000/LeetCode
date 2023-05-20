from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)

        while left < right:
            middle = (left + right) // 2
            if right - left == 1:
                return nums[middle]
            if middle % 2 == 1:
                if nums[middle - 1] != nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[middle] != nums[middle + 1]:
                    right = middle
                else:
                    left = middle + 2
        
        return nums[right]

def main():
    sol = Solution()
    print(sol.singleNonDuplicate([1,1,2,2,3]))
    print(sol.singleNonDuplicate([1,1,2,3,3]))
    print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))
    print(sol.singleNonDuplicate([3,3,7,7,10,10,11,11,12]))
    print(sol.singleNonDuplicate([1,3,3,7,7,10,10,11,11]))

if __name__ == '__main__':
    main()