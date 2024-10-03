from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(lambda: float('inf'))
        res = -float('inf')
        cur = 0

        for num in nums:
            prefix[num] = min(prefix[num], cur)
            cur += num

            if num - k in prefix:
                res = max(res, cur - prefix[num - k])
            
            if num + k in prefix:
                res = max(res, cur - prefix[num + k])
        
        return res if res != -float('inf') else 0


    # def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     prefix = [0]
    #     indexes = defaultdict(list)
    #     res = -float('inf')

    #     for num in nums:
    #         prefix.append(prefix[-1] + num)

    #     for i, num in enumerate(nums):
    #         indexes[num].append(i)
        
    #     for i in range(n):
    #         for j in indexes[nums[i] + k]:
    #             if i < j:
    #                 res = max(res, prefix[j + 1] - prefix[i])

    #         for j in indexes[nums[i] - k]:
    #             if i < j:
    #                 res = max(res, prefix[j + 1] - prefix[i])
        
    #     return res if res != -float('inf') else 0



def main():
    sol = Solution()
    print(sol.maximumSubarraySum(nums = [1,2,3,4,5,6], k = 1))
    print(sol.maximumSubarraySum(nums = [-1,3,2,4,5], k = 3))
    print(sol.maximumSubarraySum(nums = [-1,-2,-3,-4], k = 2))

if __name__ == '__main__':
    main()