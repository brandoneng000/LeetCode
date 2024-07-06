from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        return sum(nums[i] > 0 for i in range(n))
        
def main():
    sol = Solution()
    print(sol.maxScore(nums = [2,-1,0,1,-3,3,-3]))
    print(sol.maxScore(nums = [-2,-3,0]))

if __name__ == '__main__':
    main()