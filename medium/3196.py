from typing import List

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        res_add = nums[0]
        res_sub = nums[0]

        for i in range(1, n):
            temp_add = max(res_add, res_sub) + nums[i]
            temp_sub = res_add - nums[i]

            res_add = temp_add
            res_sub = temp_sub
        
        return max(res_add, res_sub)


        
def main():
    sol = Solution()
    print(sol.maximumTotalCost([1,-2,3,4]))
    print(sol.maximumTotalCost([1,-1,1,-1]))
    print(sol.maximumTotalCost([0]))
    print(sol.maximumTotalCost([1,-1]))

if __name__ == '__main__':
    main()