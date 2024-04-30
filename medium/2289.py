from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:        
        n = len(nums)
        dp = [0] * n
        stack = []

        for i, num in enumerate(nums):
            cur = 0
            
            while stack and num >= nums[stack[-1]]:
                cur = max(cur, dp[stack.pop()])

            if stack:
                dp[i] = cur + 1
            
            stack.append(i)
        
        return max(dp)
            

        
def main():
    sol = Solution()
    print(sol.totalSteps([5,3,4,4,7,3,6,11,8,5,11]))
    print(sol.totalSteps([4,5,7,7,13]))

if __name__ == '__main__':
    main()