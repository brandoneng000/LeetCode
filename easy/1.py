from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index in range(len(nums)):
            nums_dict[nums[index]] = index
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in nums_dict and nums_dict[diff] != index:
                return [index, nums_dict[diff]]


def main():
    sol = Solution()
    test_one = [2, 7, 11, 15]
    test_two = [3, 2, 4]
    test_three = [3,3]
    target_one = 9
    target_two = 6
    target_three =6
    print(sol.twoSum(test_one, target_one))
    print(sol.twoSum(test_two, target_two))
    print(sol.twoSum(test_three, target_three))

if __name__ == '__main__':
    main()