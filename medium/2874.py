from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_i = max_ij = 0

        for num in nums:
            res = max(res, max_ij * num)
            max_ij = max(max_ij, max_i - num)
            max_i = max(max_i, num)
        
        return res
        
    # def maximumTripletValue(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     res = 0

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             for k in range(j + 1, n):
    #                 res = max(res, (nums[i] - nums[j]) * nums[k])
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.maximumTripletValue([12,6,1,2,7]))
    print(sol.maximumTripletValue([1,10,3,4,19]))
    print(sol.maximumTripletValue([1,2,3]))

if __name__ == '__main__':
    main()