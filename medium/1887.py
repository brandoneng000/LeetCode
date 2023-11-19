from typing import List
from collections import Counter

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        operation = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                operation += 1

            res += operation

        return res
        
    # def reductionOperations(self, nums: List[int]) -> int:
    #     count_nums = Counter(nums)
    #     operations = {}

    #     for i, num in enumerate(sorted(count_nums)):
    #         operations[num] = i
        
    #     return sum(operations[num] * count_nums[num] for num in count_nums)

        
def main():
    sol = Solution()
    print(sol.reductionOperations([27664,47570,27664,27664,27664,27664,27664,27664,27664,27664]))
    print(sol.reductionOperations([5,1,3]))
    print(sol.reductionOperations([1,1,1]))
    print(sol.reductionOperations([1,1,2,2,3]))

if __name__ == '__main__':
    main()