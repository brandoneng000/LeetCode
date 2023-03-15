from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if target not in nums:
            return []

        def binary_search(nums, target, lower=True) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                if target == nums[middle]:
                    if lower:
                        if left == middle or nums[middle] != nums[middle - 1]:
                            return middle
                        else:
                            right = middle - 1
                    else:
                        if middle == right or nums[middle] != nums[middle + 1]:
                            return middle
                        else:
                            left = middle + 1
                elif target < nums[middle]:
                    right = middle - 1
                elif target > nums[middle]:
                    left = middle + 1
            return -1

        left = binary_search(nums, target)
        right = binary_search(nums, target, False)

        return range(left, right + 1)

def main():
    sol = Solution()
    print(sol.targetIndices(nums = [1,2,5,2,3], target = 2))
    print(sol.targetIndices(nums = [1,2,5,2,3], target = 3))
    print(sol.targetIndices(nums = [1,2,5,2,3], target = 5))
    print(sol.targetIndices(nums = [48,90,9,21,31,35,19,69,29,52,100,54,21,86,6,45,42,5,62,77,15,38], target = 6))

if __name__ == '__main__':
    main()