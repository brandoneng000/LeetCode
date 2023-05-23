from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left, right = len(nums) - 1, 0

        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)
        
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)
        
        return right - left + 1 if right - left > 0 else 0

        # sorted_nums = sorted(nums)
        # left, right = 0, len(nums) - 1

        # while right >= 0 and sorted_nums[right] == nums[right]:
        #     right -= 1
        
        # if right == -1: return 0

        # while left < len(nums) and sorted_nums[left] == nums[left]:
        #     left += 1
        
        # return right - left + 1

def main():
    sol = Solution()
    print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))
    print(sol.findUnsortedSubarray([1,2,3,4]))
    print(sol.findUnsortedSubarray([1]))

if __name__ == '__main__':
    main()