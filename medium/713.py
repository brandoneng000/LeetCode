from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        cur_val = 1
        res = left = 0

        for right, val in enumerate(nums):
            cur_val *= val
            while cur_val >= k:
                cur_val /= nums[left]
                left += 1
            res += right - left + 1
        
        return res

    
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     res = 0

    #     for i in range(len(nums) - 1, -1, -1):
    #         if nums[i] < k:
    #             temp = 1
    #             for j in range(i, -1, -1):
    #                 if temp * nums[j] < k:
    #                     res += 1
    #                     temp *= nums[j]
    #                 else:
    #                     break
        
    #     return res

def main():
    sol = Solution()
    print(sol.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
    print(sol.numSubarrayProductLessThanK(nums = [1,2,3], k = 0))

if __name__ == '__main__':
    main()