from typing import List
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        count = {}
        left = 0
        cur = 0

        for right in range(n):
            count[nums[right]] = count.get(nums[right], 0) + 1
            cur += count[nums[right]] - 1
            
            while cur >= k:
                res += n - right
                cur -= count[nums[left]] - 1
                count[nums[left]] -= 1
                left += 1
        
        return res

    # def countGood(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     res = 0
    #     count = Counter()
    #     left = 0

    #     for right in range(n):
    #         k -= count[nums[right]]
    #         count[nums[right]] += 1

    #         while k <= 0:
    #             count[nums[left]] -= 1
    #             k += count[nums[left]]
    #             left += 1

    #         res += left
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.countGood(nums = [1,1,1,1,1], k = 10))
    print(sol.countGood(nums = [3,1,4,3,2,2,4], k = 2))

if __name__ == '__main__':
    main()