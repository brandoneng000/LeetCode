from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        left = 0
        
        for right in range(n):
            if nums[right] > threshold:
                left = right + 1
            elif left == right or nums[right] % 2 == nums[right - 1] % 2:
                left = right + nums[right] % 2
            
            res = max(res, right - left + 1)
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.longestAlternatingSubarray(nums = [2,2], threshold = 18))
    print(sol.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5))
    print(sol.longestAlternatingSubarray(nums = [1,2], threshold = 2))
    print(sol.longestAlternatingSubarray(nums = [2,3,4,5], threshold = 4))

if __name__ == '__main__':
    main()