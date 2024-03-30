from typing import List
from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(nums: List[int], k: int):
            n = len(nums)
            count = Counter()
            res = left = 0

            for right in range(n):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                
                res += right - left + 1

            return res

        return at_most_k(nums, k) - at_most_k(nums, k - 1)

        
def main():
    sol = Solution()
    print(sol.subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))
    print(sol.subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3))

if __name__ == '__main__':
    main()