from typing import List
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter()
        left = 0
        chars_over_k = 0

        for right in range(n):
            freq[nums[right]] += 1

            if freq[nums[right]] == k + 1:
                chars_over_k += 1

            if chars_over_k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == k:
                    chars_over_k -= 1
                left += 1

        return n - left

    # def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     count = Counter()
    #     left = 0
    #     res = 0

    #     for right in range(n):
    #         count[nums[right]] += 1

    #         while count[nums[right]] > k:
    #             count[nums[left]] -= 1
    #             left += 1
            
    #         res = max(res, right - left + 1)
        
    #     return res
            


def main():
    sol = Solution()
    print(sol.maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))
    print(sol.maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1))
    print(sol.maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4))

if __name__ == '__main__':
    main()