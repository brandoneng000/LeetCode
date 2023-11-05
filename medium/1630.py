from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_arith_subarray(nums: List[int]):
            diff = nums[1] - nums[0]

            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] != diff:
                    return False
            
            return True
        
        n = len(l)
        subarray_ranges = list(zip(l, r, range(n)))
        res = []
        
        for left, right, index in subarray_ranges:
            res.append(check_arith_subarray(sorted(nums[left: right + 1])))
        
        return res

        
def main():
    sol = Solution()
    print(sol.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))
    print(sol.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))

if __name__ == '__main__':
    main()