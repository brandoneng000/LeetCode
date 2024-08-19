from typing import List
from collections import Counter

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter()
        left = 0
        freq = 0 

        for right in range(n):
            count[nums[right]] += 1

            freq = max(freq, count[nums[right]])
            if right - left + 1 - freq > k:
                count[nums[left]] -= 1
                left += 1
        
        return freq
        
def main():
    sol = Solution()
    print(sol.longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3))
    print(sol.longestEqualSubarray(nums = [1,1,2,2,1,1], k = 2))

if __name__ == '__main__':
    main()