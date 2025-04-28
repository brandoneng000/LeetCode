from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        total = 0
        left = 0

        for right in range(n):
            total += nums[right]

            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            
            res += right - left + 1

        return res

        
def main():
    sol = Solution()
    print(sol.countSubarrays(nums = [2,1,4,3,5], k = 10))
    print(sol.countSubarrays(nums = [1,1,1], k = 5))

if __name__ == '__main__':
    main()