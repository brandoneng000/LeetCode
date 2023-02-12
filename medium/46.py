from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def create_permute(nums: List[int], stack: List[int], result: List[List[int]]):
            if len(stack) == len(nums):
                result.append(stack.copy())

            for i in range(len(nums)):
                if nums[i] in stack:
                    continue
                stack.append(nums[i])
                create_permute(nums, stack, result)
                stack.pop()
        
        result = []
        create_permute(nums, [], result)
        return result
        

def main():
    sol = Solution()
    print(sol.permute([1,2,3]))
    print(sol.permute([0,1]))
    print(sol.permute([1]))

if __name__ == '__main__':
    main()