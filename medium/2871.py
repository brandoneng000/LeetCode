from typing import List

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        stack = [nums[0]]

        for i in range(1, n):
            if stack[-1] == 0:
                stack.append(nums[i])
            else:
                stack[-1] &= nums[i]
        
        return len(stack) if stack[-1] == 0 or len(stack) == 1 else len(stack) - 1
            
        
def main():
    sol = Solution()
    print(sol.maxSubarrays([1,0,2,0,1,2]))
    print(sol.maxSubarrays([5,7,1,3]))

if __name__ == '__main__':
    main()