from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()
            
            if len(stack) < k:
                stack.append(num)
        
        return stack

    # def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    #     def find_min_index(nums: List[int], start_index: int):
    #         return nums.index(min(nums)) + start_index
        
    #     res = [-1]
    #     n = len(nums)

    #     for end in range(k - 1, -1, -1):
    #         res.append(find_min_index(nums[res[-1] + 1: n - end], res[-1] + 1))
        
    #     return [nums[i] for i in res[1:]]
        
def main():
    sol = Solution()
    print(sol.mostCompetitive(nums = [3,5,2,6], k = 2))
    print(sol.mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4))

if __name__ == '__main__':
    main()