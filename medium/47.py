from typing import List
import collections

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def create_permute(nums_dict: dict[int], stack: List[int], result: List[List[int]]):
            if len(stack) == len(nums):
                result.append(stack.copy())
            
            for num in nums_dict:
                if nums_dict[num] > 0:
                    stack.append(num)
                    nums_dict[num] -= 1
                    create_permute(nums_dict, stack, result)
                    nums_dict[num] += 1
                    stack.pop()

        
        result = []
        nums_dict = collections.Counter(nums)
        create_permute(nums_dict, [], result)
        return result

def main():
    sol = Solution()
    print(sol.permuteUnique([1,1,2]))
    print(sol.permuteUnique([1,2,3]))

if __name__ == '__main__':
    main()