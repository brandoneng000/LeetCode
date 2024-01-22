from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = (set(range(1, n + 1)) - set(nums)).pop()
        
        return [sum(nums) - (sum(range(1, n + 1)) - missing), missing]

    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     from collections import Counter
    #     def sum_of_all(n: int) -> int:
    #         return (n * (n + 1)) // 2

    #     nums_dict = Counter(nums)
        
    #     for num in nums_dict:
    #         if nums_dict[num] == 2:
    #             dupe = num

    #     return [dupe, dupe + (sum_of_all(len(nums)) - sum(nums))]


def main():
    sol = Solution()
    print(sol.findErrorNums(nums = [1,2,2,4]))
    print(sol.findErrorNums(nums = [1,2,4,4]))
    print(sol.findErrorNums(nums = [1,1]))
    print(sol.findErrorNums(nums = [3,2,2]))

if __name__ == '__main__':
    main()