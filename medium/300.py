from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                index = bisect_left(sub, num)
                sub[index] = num
        
        return len(sub)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     nums_dict = {}
    #     res = []
    #     arr = []

    #     for index, num in enumerate(nums):
    #         nums_dict[(num, index)] = nums_dict.get(num, [])
    #         for n in nums_dict:
    #             if n[0] < num:
    #                 nums_dict[n].append((num, index))
        
    #     def recursive(nums_dict, arr: List[int]):
    #         if not nums_dict[arr[-1]]:
    #             return arr.copy()
            
    #         longest = []
    #         for n in nums_dict[arr[-1]]:
    #             arr.append(n)
    #             longest = max(longest, recursive(nums_dict, arr), key=len)
    #             arr.pop()
            
    #         return longest
        
    #     for index, num in enumerate(nums):
    #         arr.append((num, index))
    #         res = max(res, recursive(nums_dict, arr), key=len)
    #         arr.pop()
        
    #     return len(res)

    #     cache = {}
    #     for i in range(len(nums) - 1, -1, -1):
    #         cache[i] = 1
    #         for j in range(i, len(nums)):
    #             if nums[i] < nums[j]:
    #                 cache[i] = max(cache[j] + 1, cache[i])

    #     return max(cache.values())

    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[j] + 1, cache[i])

        return max(cache)

def main():
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLIS([0,1,0,3,2,3]))
    print(sol.lengthOfLIS([7,7,7,7,7,7,7]))
    print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

if __name__ == '__main__':
    main()