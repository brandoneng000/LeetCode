from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        res = 0
        cur = 0

        for right in range(n):
            target = nums[right]
            cur += target

            while (right - left + 1) * target - cur > k:
                cur -= nums[left]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxFrequency(nums = [1,2,4], k = 5))
    print(sol.maxFrequency(nums = [1,4,8,13], k = 5))
    print(sol.maxFrequency(nums = [3,9,6], k = 2))

if __name__ == '__main__':
    main()