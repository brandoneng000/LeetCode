from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        up, up_prev = 1, 0
        res = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up += 1
            else:
                up_prev = up
                up = 1
            
            half = up >> 1
            m = min(up, up_prev)
            candidate = max(half, m)

            if candidate > res:
                res = candidate
            
        return res
        
        
def main():
    sol = Solution()
    print(sol.maxIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1]))
    print(sol.maxIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7]))

if __name__ == '__main__':
    main()