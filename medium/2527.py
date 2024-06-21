from typing import List

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res

    # def xorBeauty(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     vals = set()

    #     for i in range(n):
    #         for j in range(n):
    #             for k in range(n):
    #                 val = (nums[i] | nums[j]) & nums[k]

    #                 if val in vals:
    #                     vals.remove(val)
    #                 else:
    #                     vals.add(val)
        
    #     res = 0
    #     for val in vals:
    #         res ^= val
        
    #     return res
        
        
def main():
    sol = Solution()
    print(sol.xorBeauty([1,4]))
    print(sol.xorBeauty([15,45,20,2,34,35,5,44,32,30]))

if __name__ == '__main__':
    main()